import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of a custom field in your organization
custom_field_id = '<CUSTOM_FIELD_ID>'

# Request a custom field's select options in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/custom-field/{custom_field_id}/select-options', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request a custom field's select options in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/custom-field-group-assignment/?custom_field={custom_field_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])
