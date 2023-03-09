import csv
import requests

# URL of the API to add phone to Cisco Call Manager
url = 'https://<your_cisco_call_manager_url>/api/phones/'

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

        # Create a dictionary of phone details to add to Cisco Call Manager
        phone_data = {
            'name': phone_name,
            'ip_address': phone_ip,
            'phone_model': phone_model
        }

        # Send a POST request to the Cisco Call Manager API to add the phone
        response = requests.post(url, json=phone_data)

        # Check if the request was successful
        if response.status_code == 201:
            print(f"Phone '{phone_name}' added successfully.")
        else:
            print(f"Failed to add phone '{phone_name}'. Error: {response.text}")

