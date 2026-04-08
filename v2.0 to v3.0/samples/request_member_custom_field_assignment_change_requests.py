import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of a member, a member custom field and a member custom field assignment for this custom field in your organization
member_id = '<MEMBER_ID>'
custom_field_id = '<CUSTOM_FIELD_ID>'
custom_field_assignment_id = '<CUSTOM_FIELD_ASSIGNMENT_ID>'


# ==========================================================
# Request a member's custom field assignment change requests
# ==========================================================

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

# =============================================================
# Add a new custom field assignment change request for a member
# =============================================================

# In API version `stable`
data_for_post_stable = {
    'fieldValue': 'Hallo!'
}
request_stable = requests.post(f'https://easyverein.com/api/stable/member/{member_id}/custom-fields/{custom_field_assignment_id}/change-requests', json=data_for_post_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["id"], request_stable_json["userCustomField"], request_stable_json["fieldName"], request_stable_json["fieldValue"])

# In API version `latest`
data_for_post_latest = {
    'field_value': 'Hallo!',
    # Instead of the member's custom field assignment, the custom field itself must be given now
    'custom_field': custom_field_id
}
request_latest = requests.post(f'https://easyverein.com/api/latest/member-custom-field-assignment-change-request', json=data_for_post_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["id"], request_latest_json["user_custom_field"], request_latest_json["field_name"], request_latest_json["field_value"])
