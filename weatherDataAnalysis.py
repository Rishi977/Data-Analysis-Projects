#import the required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 #%matplotlib inline  this line will only be use when code editor is Jyupiter notebook.

data = pd.read_csv(r"D:\Rishikesh\Projects\Project-1_Weather_Data\Weather_Data.csv") #r is used to remove the unicode error.
orignal_data = data.copy()   #we have created a copy of orignal data.
#print(orignal_data)

#print(data)
#print(data.head())    #top 5 rows
# print(data.tail())   #last 5 rows
#print(data.info())  #to give the information related to null values datatype of the data.
#print(data.index)
#print(data.columns)   #to give the column name
#print(data.dtypes)   #provide the data type of the column
#print(data['Weather'].unique())   #it shows the unique value of a particular given column.
#print(data.nunique())   #it will provide the unique row count of each column.
#print(data.count())    #it shows the total no. of non-null values in each columns
#print(data['Weather'].value_counts())


# Now here is the Question?

# 1. Find all the unique "Wind Speed" values in the data?
#print(data.head(10))
#print(data['Wind Speed_km/h'].unique)
#print(data['Wind Speed_km/h'].nunique())c

print("Q1. Find all the unique 'Wind Speed' values in the data?")

wind_speed = data['Wind Speed_km/h'].unique()   #WindSpeed is a variable

wind_Speed_array = np.array(wind_speed)

for value in wind_Speed_array:
     print(value)

print("Answer: These are the all unique wind speeds:",wind_Speed_array,"\n")

# 2. Find the number of times when the 'Weather is exactly Clear'?

#print("These are the columnsdata.columns)

print("Q2. Find the number of times when the 'Weather is exactly Clear'?")

clear_count = data[data.Weather == 'Clear'].shape[0]

print("Answer: Clear weather is exactly:",clear_count, "times")

print(data.groupby('Weather').get_group('Clear'))  #it will provide all the records where Weather is clear.

# 3. Find the number of times when the 'Wind Speed was exactly 4km/h?
print("Q3. Find the number of times when the 'Wind Speed was exactly 4km/h?")
windspeed_data = data[data['Wind Speed_km/h'] == 4].shape[0]
print("Answer: Wind Speed is exactly 4km/h is ",windspeed_data,"times")


# 4. Find out all the Null Values in the data.
print("Q4. Find out all the Null Values in the data?")
null_counts = data.isnull().sum()
null_values = null_counts.sum()
print("Answer: Total Number of null values is:",null_values)


# 5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'?
new_column = data.rename(columns={'Weather':'Weather Condition'}, inplace=True)
print(new_column)

# 6. What is the mean 'Visibility'?

print("Q6. What is the mean of 'Visibility'?")
visibility_mean = data['Visibility_km'].mean()
print("Answer: The mean of 'Visibility' is: ",round(visibility_mean,2))

# 7. What is the Standard Deviation of 'Pressure' in this data?

print("Q7. What is the Standard Deviation of 'Pressure' in this data?")
sd = data.Press_kPa.std()

print("Answer: Standard Deviation of Pressure is: ",round(sd,2))

# 8. What is the variance of 'Relative Humidity' in this data?

print("Q8. What is the variance of 'Relative Humidity' in this data?")
data_variance = data['Rel Hum_%'].var()
print("Answer: Variance of Relative Humidity is: ",round(data_variance,2))

# 9. Find all instances when 'Snow' was recorded.?

print(data.columns)
snow_details = data[data['Weather Condition'] == 'Snow']

print(snow_details)

# 10. Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'?

print("Q10. Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'?")
filtered_all_instances = data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]

print("Answer: All Instances while Wind Speed is having more than 24 and Visibility is having 25: ",filtered_all_instances)
    
# 11. WHat is the Mean value of each column against each 'Weather Condition'?

# numeric_data = data.select_dtypes(include=np.number)

#data_mean = numeric_data.groupby('Weather Condition').mean()

#print(data_mean)

# selected_columns = data.select_dtypes(include=np.number)
# numeric_and_weather = data[selected_columns]

# data_mean = selected_columns.mean()


# print(data_mean)
# #print(weather_condition)


# 12. What is the Minimum & Maximum value of each column against each 'Weather Condition'?

print(data.head(2))

max_data = data.groupby('Weather Condition').max()
min_data = data.groupby('Weather Condition').min()

print(max_data,min_data)


# 13. Show all the Records where Weather Condition is Fog.

fog_data = data[data['Weather Condition'] == 'Fog']
print(fog_data)



# 14. Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

filtered_clear_data = data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]

print(filtered_clear_data)

# 15. Find all instances when:
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'

# or

# B. 'Visibility is above 40'

#print(data.head(2))
filter_Data = data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]

print(filter_Data.head(10))

