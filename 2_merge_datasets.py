import pandas as pd

# Reading the csv files
crime_df = pd.read_csv('data/crime_data.csv')
demo_df = pd.read_csv('data/demographic_data.csv')

# Merge on dbn column 
merged_df = pd.merge(crime_df, demo_df, on='dbn', how='inner')

# Fixing the order of columns
merged_df = merged_df[['dbn', 'school_name', 'address', 'tot_crime', 'male', 'female', 'white', 'black', 'asian', 'hispanic', 'other']]

# Saving to csv file
merged_df.to_csv('data/brooklyn_school_master.csv', index=False)


