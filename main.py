from funcs  import *
import time
import pandas as pd

# Read the existing data from the Excel file into a DataFrame
df = pd.read_excel(r"setadiran-scraper\data\data.xlsx", index_col=0)

# Create a loop that continuously fetches new data
while True:
    # Call the fetch_data function and pass in the existing DataFrame
    fetch_data(df)
    
    # Pause the program for 900 seconds (15 minutes)
    time.sleep(900)