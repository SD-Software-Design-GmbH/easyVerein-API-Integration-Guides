import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of a member in your organization
member_id = '<MEMBER_ID>'
# Replace this by a valid ID of a member custom field assignment in your organization
custom_field_assignment_id = '<CUSTOM_FIELD_ASSIGNMENT_ID>'

# Request a member custom field assignment's change requests in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/member/{member_id}/custom-fields/{custom_field_assignment_id}/change-requests', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request a member custom field assignment's change requests in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/member-custom-field-assignment-change-request/?user_custom_field={custom_field_assignment_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])

# Alternatively, request all custom field assignment change requests of a member in API version `latest`
request_for_member_latest = requests.get(f'https://easyverein.com/api/latest/member-custom-field-assignment-change-request/?user_custom_field__user_object={member_id}', headers=header)
request_for_member_latest_json = request_for_member_latest.json()
print(request_for_member_latest_json["results"][0])
