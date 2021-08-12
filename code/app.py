import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.sql import exists

from flask import Flask, json, jsonify

#####################################
engine = create_engine("sqlite:///resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)


@app.route("/")
def home():
    #Homepage
    #List of all routes available
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Convert the query results to a dictionary using date as the key and prcp as the value.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    print(year_ago)
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).order_by(Measurement.date).all()
    prcp_data_dict = dict(prcp_data)
    #Return the JSON representation of your dictionary.
    return jsonify(prcp_data_dict)

@app.route("/api/v1.0/stations")
def stations():
    #Return a JSON list of stations from the dataset.
    all_stations = session.query(Station.station, Station.name).all()
    all_stations_list = list(all_stations)
    return jsonify(all_stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    #Query the dates and temperature observations of the most active station for the last year of data.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, (Measurement.tobs)).filter(Measurement.date >= year_ago).\
        filter(Measurement.station =="USC00519281").order_by(Measurement.date).all()
    tobs_data_list = list(tobs_data)
    #Return a JSON list of temperature observations (TOBS) for the previous year.
    return jsonify(tobs_data_list)

@app.route("/api/v1.0/<start>")
def start_day(start):
    #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    start_day = session.query(Measurement.date, func.min(Measurement.tobs),\
        func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).\
            group_by(Measurement.date).all()
    #Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    start_day_list = list(start_day)
    return jsonify(start_day_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start, end):
    #Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    start_end_day = session.query(Measurement.date, func.min(Measurement.tobs),\
        func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).\
            filter(Measurement.date <= end).group_by(Measurement.date).all()

    #When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    start_end_day_list = list(start_end_day)
    return jsonify(start_end_day_list) 
if __name__ == "__main__":
    app.run(debug=True)
