### Date created
Project creation date: 7/15/2020

### Project Title
Bike Share Data Analysis

### Description
In this project, Python was used to explore data (provided by Motivate) related to bike share systems for three major cities in the United States - Chicago, New York City, and Washington. The script takes in raw input to create an interactive experience in the terminal to present statistics for a requested city.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
Gender
Birth Year

These are the statistics computed:

1 Popular times of travel (i.e., occurs most often in the start time) of the following:
most common month
most common day of week
most common hour of day

2 Popular stations and trip of the following:
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

3 Trip duration of the following:
total travel time
average travel time

4 User info of the following:
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used
bikeshare.py is the main script. This project also uses three city dataset files: chicago.csv, new_york_city.csv, and washington.csv

### Credits
https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python
http://www.datasciencemadesimple.com/mode-function-python-pandas-dataframe-row-column-wise-mode/
https://www.geeksforgeeks.org/python-pandas-dataframe-idxmax/
https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm
