import csv
import requests

# CUCM authentication credentials
username = '<your_cucm_username>'
password = '<your_cucm_password>'

# URL of the API to add phone to Cisco Call Manager
url = 'https://<your_cisco_call_manager_url>/api/phones/'

# Create a session object to handle authentication
session = requests.Session()
session.auth = (username, password)

# Open the CSV file containing the list of phones
with open('phone_list.csv', newline='') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the phone details from the CSV row
        phone_name = row[0]
        phone_ip = row[1]
        phone_model = row[2]

        # Print the phone details to the console
        print(f"Phone Name: {phone_name}, IP Address: {phone_ip}, Model: {phone_model}")
