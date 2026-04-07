import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of a member in your organization
member_id = '<MEMBER_ID>'

# Request a member's custom field assignments in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/member/{member_id}/custom-fields', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request a member's custom field assignments in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/member-custom-field-assignment/?user_object={member_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])
