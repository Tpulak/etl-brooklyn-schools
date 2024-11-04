import pandas as pd
import sqlite3

# Read the merged CSV file
merged_df = pd.read_csv('data/brooklyn_school_master.csv')

# Loading the dataframe to SQL
conn = sqlite3.connect('data/brooklyn_school.db')
merged_df.to_sql('schools', conn, if_exists='replace', index=False)
conn.close()

