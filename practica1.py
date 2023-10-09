import requests
import csv

# URL of the CSV file you want to download
csv_url = "https://raw.githubusercontent.com/Sergio-Gtz-V/DataMining/main/games_updated.csv"

# Define the local file where you want to save the CSV data
local_file_path = "downloaded_file.csv"

try:
    # Send an HTTP GET request to the CSV URL
    response = requests.get(csv_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the content to the local file
        with open(local_file_path, "wb") as file:
            file.write(response.content)
        print(f"CSV file downloaded successfully and saved as {local_file_path}")
    else:
        print(f"Failed to download CSV file. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
except IOError as e:
    print(f"An error occurred while writing the file: {e}")