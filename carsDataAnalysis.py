# import libraries

import pandas as pd
import numpy as np


car_data = pd.read_csv(r'D:\Rishikesh\Projects\Project-2_Car_Data\Cars.csv')
#orignal_Data = car_data.copy()

#print(car_data.head(2))
#print(car_data.shape)

# 1. Instruction (For Data Cleaning)
    # a) Find all Null Value in the dataset. If there is any null value in any column, then fill it with the mean of that column.

null_Data = car_data.isnull().sum()

#print(null_Data)

# 1. to fill the null value present in Cylinders column with the mean value of this column.
null_Data = car_data['Cylinders'].fillna(car_data['Cylinders'].mean(), inplace=True)

print(null_Data)
#print(car_data.isnull().sum())

# 2. Question (Based on Values Counts)
    # Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of 
    #each Make in the data?
# print(car_data.head(2))

# unique_make = car_data['Make'].unique()

make_count = car_data['Make'].value_counts()

print(make_count)

# 3. Instruction (Filtering)
    # Show all the records where Origin is Asia or Europe

# print(car_data.head(2))

#origin_Data = car_data[(car_data['Origin'] == 'Asia') | (car_data['Origin'] == 'Europe')]
origin_Data = car_data[car_data['Origin'].isin(['Asia','Europe'])]

print(origin_Data)

# Additional question is that total MSRP of each make or brand

car_data['MSRP'] = car_data['MSRP'].str.replace('[\$,]','', regex=True).astype(float)
make_msrp = car_data.groupby('Make')['MSRP'].sum()

make_msrp_formatted = make_msrp.apply(lambda x: '${:,.0f}'.format(x))

print("Make\t\tTotal_MSRP")

for make, total_msrp in make_msrp_formatted.items():
    print(f"{make.ljust(15)}{total_msrp}")

# 4. Instruction (Removing unwanted records)
    # Remove all the records (rows) where Weight is above 4000.

weight_Data = car_data[~(car_data['Weight'] > 4000)]

print(weight_Data)

# 5. Instruction (Applying function on a column)
    # Increase all the values of 'MPG_City' column by 3.

#print(car_data.head(2))

car_data['MPG_City'] = car_data['MPG_City'].apply(lambda x:x+3)
print(car_data)
