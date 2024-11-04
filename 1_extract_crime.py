import pandas as pd
from sodapy import Socrata
from dotenv import load_dotenv
import os

load_dotenv()
app_token = os.getenv('APP_TOKEN')
data_url = 'data.cityofnewyork.us'
client = Socrata(data_url, app_token)
safety_data_set_id = 'qybk-bjjc'

# Extracting crime rates for schools in Brooklyn in year 2014-2015
results = client.get(
    safety_data_set_id, 
    where="borough_name='BROOKLYN ' AND school_year='2014-15'",  
    select="dbn, school_year, address, major_n, oth_n, nocrim_n"
)
df = pd.DataFrame.from_records(results)

# Convert text columns into numeric ones
df['major_n'] = pd.to_numeric(df['major_n'], errors='coerce').fillna(0)
df['oth_n'] = pd.to_numeric(df['oth_n'], errors='coerce').fillna(0)
df['nocrim_n'] = pd.to_numeric(df['nocrim_n'], errors='coerce').fillna(0)

# Adding all crime columns into a new total crime column
df['tot_crime'] = df[['major_n', 'oth_n', 'nocrim_n']].sum(axis=1).astype(int)

# Fixing order of columns
df = df[['dbn', 'address', 'tot_crime']]

# Saving to csv file
df.to_csv('data/crime_data.csv', index=False)

