import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of a select or multi-select custom field in your organization
custom_field_id = '<CUSTOM_FIELD_ID>'

# =======================================
# Request a custom field's select options
# =======================================

# In API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/custom-field/{custom_field_id}/select-options', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# In API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/select-option/?custom_field={custom_field_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])

# ==========================================
# Add a new select option for a custom field
# ==========================================

# In API version `stable`
data_for_post_stable = {
    'value': 123
}
request_stable = requests.post(f'https://easyverein.com/api/stable/custom-field/{custom_field_id}/select-options', json=data_for_post_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["id"], request_stable_json["customField"], request_stable_json["value"])

# In API version `latest`
data_for_post_latest = {
    'value': 123,
    'custom_field': custom_field_id
}
request_latest = requests.post(f'https://easyverein.com/api/latest/select-option', json=data_for_post_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["id"], request_latest_json["custom_field"], request_latest_json["value"])

# Save the select option ID for later
select_option_id = request_latest_json["id"]

# ==============================
# bulk-create new select options
# ==============================

# In API version `stable`
data_for_bulk_create_stable = {
    'entries': [
        {
            'value': 321
        }
    ]
}
request_stable = requests.post(f'https://easyverein.com/api/stable/custom-field/{custom_field_id}/select-options/bulk-create', json=data_for_bulk_create_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_bulk_create_latest = {
    'entries': [
        {
            'value': 321,
            'custom_field': custom_field_id
        }
    ]
}
request_latest = requests.post(f'https://easyverein.com/api/latest/select-option/bulk-create', json=data_for_bulk_create_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))

# ==========================
# bulk-update select options
# ==========================

# In API version `stable`
data_for_bulk_update_stable = {
    'entries': [
        {
            'id': select_option_id,
            'value': 789
        }
    ]
}
request_stable = requests.patch(f'https://easyverein.com/api/stable/custom-field/{custom_field_id}/select-options/bulk-update', json=data_for_bulk_update_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_bulk_update_latest = {
    'entries': [
        {
            'id': select_option_id,
            'value': 789
        }
    ]
}
request_latest = requests.patch(f'https://easyverein.com/api/latest/select-option/bulk-update', json=data_for_bulk_update_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))
