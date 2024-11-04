import pandas as pd
from sodapy import Socrata
from dotenv import load_dotenv
import os

load_dotenv()
app_token = os.getenv('APP_TOKEN')
data_url = 'data.cityofnewyork.us'
client = Socrata(data_url, app_token)
demo_data_set_id = '5cd6-v74i'

# Extracting demographic for schools in Brooklyn
results = client.get(
    demo_data_set_id,
    where="dbn LIKE '%K%'",
    select="dbn, school_name, male, female, white, black, asian, hispanic, other"
)
df = pd.DataFrame.from_records(results)

# Cleaning percentage columns
percentage_columns = ['male', 'female', 'white', 'black', 'asian', 'hispanic', 'other']
for column in percentage_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')
    df[column] = (df[column] * 100).round(1).astype(str) + '%'

# Saving to csv file
df.to_csv('data/demographic_data.csv', index=False)
