
import requests
import pandas as pd

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in funds.items():

    print("\n" + "=" * 60)
    print(f"Fetching {fund_name}")
    print("=" * 60)

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    file_path = f"data/raw/{fund_name}.csv"

    nav_df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")

print("\nAll 5 funds downloaded successfully!")


#import requests
#import pandas as pd

#amfi_code = 125497

#url = f"https://api.mfapi.in/mf/{amfi_code}"  #This is the API endpoint.

#response = requests.get(url)  #Sends an HTTP GET request.

#data = response.json()  #converts json to python dictionary

#print("Scheme Name:")
#print(data["meta"]["scheme_name"]) #Prints fund name.

#print("\nFirst NAV Records:")

#nav_df = pd.DataFrame(data["data"])  #Converts NAV records into a DataFrame.

#print(nav_df.head())

#nav_df.to_csv(
 #   "data/raw/hdfc_top100_live_nav.csv",
  #  index=False
#)

#print("\nCSV Saved Successfully")



#The script fetched mutual fund NAV data from the MFAPI API using the Requests library, 
# converted the JSON response into a Pandas DataFrame, and stored it as a CSV file for 
# further analysis