import requests

# URL of the API to retrieve phone details from Cisco Call Manager
url = 'https://<your_cisco_call_manager_url>/api/phones/'

# Send a GET request to the Cisco Call Manager API to retrieve the list of phones
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the phone data from the API response
    phone_data = response.json()

    # Loop through each phone and print its details
    for phone in phone_data:
        phone_name = phone['name']
        phone_ip = phone['ip_address']
        phone_model = phone['phone_model']
        print(f"Phone Name: {phone_name}, IP Address: {phone_ip}, Model: {phone_model}")
else:
    print(f"Failed to retrieve phone list. Error: {response.text}")

