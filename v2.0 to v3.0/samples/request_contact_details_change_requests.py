import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of an address in your organization
contact_details_id = '<CONTACT_DETAILS_ID>'

# =========================================
# Request the change requests of an address
# =========================================

# In API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/contact-details/{contact_details_id}/change-requests', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# In API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/contact-details-change-request/?address={contact_details_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])

# =======================================
# Add a new change request for an address
# =======================================

# In API version `stable`
data_for_post_stable = {
    'fieldName': 'iban',
    'fieldValue': 'DE02120300000000202051'
}
request_stable = requests.post(f'https://easyverein.com/api/stable/contact-details/{contact_details_id}/change-request', json=data_for_post_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["id"], request_stable_json["contactDetails"], request_stable_json["fieldName"], request_stable_json["fieldValue"])

# In API version `latest`
data_for_post_latest = {
    'field_name': 'iban',
    'field_value': 'DE02120300000000202051',
    'contact_details': contact_details_id
}
request_latest = requests.post(f'https://easyverein.com/api/latest/contact-details-change-request', json=data_for_post_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["id"], request_latest_json["contact_details"], request_latest_json["field_name"], request_latest_json["field_value"])
