import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of an address in your organization
contact_details_id = '<CONTACT_DETAILS_ID>'

# Request custom field assignments for an address in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/contact-details/{contact_details_id}/custom-fields', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request custom field assignments for an address in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/contact-details-custom-field-assignment/?address_object={contact_details_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])
