import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of an inventory object in your organization
inventory_object_id = '<INVENTORY_OBJECT_ID>'

# Request an inventory object's custom field assignments in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/inventory-object/{inventory_object_id}/custom-fields', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request an inventory object's custom field assignments in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/inventory-object-custom-field-assignment/?inventory_object={inventory_object_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])
