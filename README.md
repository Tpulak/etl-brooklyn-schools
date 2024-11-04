# ETL Project: Analyzing Brooklyn Public Schools Crime Rates and Demographics
## Project Overview
This project is an ETL initiative that utilizes datasets from NYC OpenData.Specifically, NYC public school crime rates and demographics. By analyzing this data, we can gain valuable insights into how various factors impact crime rates in schools. Understanding the correlation between crime rates and demographics in schools is crucial for identifying trends and developing effective strategies to enhance school safety and community well-being.

## Datasets 
- [NYC Public School Crime Rates (2010-2016)](https://data.cityofnewyork.us/Education/2010-2016-School-Safety-Report/qybk-bjjc/about_data)
- [NYC Public School Demographic Data (2014-2015)](https://data.cityofnewyork.us/Education/2014-15-Guidance-Counselor-Bill-Demographic-Data/5cd6-v74i/about_data)

## ETL Process
1. **`1_extract_crime.py`**: This script extracts crime data specifically for schools in Brooklyn for the 2014-2015 school year (focusing on the same time frame as the demographics), pulling relevant data points necessary for further analysis.

2. **`1_extract_demographic.py`**: Similarly, this script extracts demographic data for Brooklyn schools.

3. **`2_merge_datasets.py`**: This script transforms and merges the datasets obtained from the crime rates and demographics.

4. **`3_load_to_sql.py`**: The final script loads the merged csv file into an SQL database. Storing data in an SQL database is beneficial as it allows for efficient querying and analysis of datasets. 

## Installation Requirements

To run the scripts in this project, ensure you have Python installed. You will need to install the following packages:

```bash
pip3 install pandas sodapy python-dotenv
