# Surfs Up
![laura](https://user-images.githubusercontent.com/62668061/129294696-186b3705-b049-4655-a4a5-d3918dda7590.jpeg)

### Description

This project analyzes weather data from various weather stations in Hawaii to estimate a potential trip. The python code is written in Jupyter Notebooks as well as a Flask app that utilizes thr sqlite database to also showcase my data retrieval. 
use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis
Start by finding the most recent date in the data set.

Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.

Starting off with the most recent date available, I retrieved precipitation data for 12 months prior.
![precipitation_plt](https://user-images.githubusercontent.com/62668061/129277918-61db968a-540b-4ff0-a1af-3d0a8298a0a5.png)

### Station Analysis
I then designed a query to find the most active weather stations filtering by temperature observation data
![tempvsfreq](https://user-images.githubusercontent.com/62668061/129277928-0695b5e2-1def-44fa-a462-b57976c128b7.png)














