# This script creates a data set consisting of county-year observations of pollutants

# Importing required modules

import pandas as pd

# Defining the directory in which the data resides

path = r'C:\Users\User\Documents\Data\PMxCounty\conreport'

# Initializing the data structure

data = pd.read_csv(path + '1980.csv')

# Adding a column to indcate the year

year = pd.Series([1980]*len(data), name = 'Year')
data = pd.concat([year, data], axis = 1)

# Reading in the remaining data and creating a combined data set

for yr in range(1981,2020):

    # Read in the next year of data
    temp = pd.read_csv(path + str(yr) + '.csv')
    
    # Create a year indicator
    year = pd.Series([yr]*len(temp), name = 'Year')
    
    # Concatenating year and temp
    temp = pd.concat([year, temp], axis = 1)
    
    # Concatenating data and temp
    data = pd.concat([data, temp], axis = 0)

# Formatting change: '.' to ''

data = data.replace('.', '')

# Write data to a new file

data.to_csv(path[0:42] + 'raw_pollution_data.csv', index = False)

