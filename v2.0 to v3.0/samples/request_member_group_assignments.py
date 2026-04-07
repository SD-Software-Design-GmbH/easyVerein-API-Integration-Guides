import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of a member and a member group in your organization
member_id = '<MEMBER_ID>'
member_group_id = '<MEMBER_GROUP_ID>'

# ====================================
# Request a member's group assignments
# ====================================

# In API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/member/{member_id}/groups', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# In API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/member-group-assignment/?user_object={member_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])

# =======================================
# Add a new group assignment for a member
# =======================================

# In API version `stable`
data_for_post_stable = {
    'memberGroup': member_group_id
}
request_stable = requests.post(f'https://easyverein.com/api/stable/member/{member_id}/groups', json=data_for_post_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["id"], request_stable_json["memberGroup"], request_stable_json["userObject"])

# In API version `latest`
data_for_post_latest = {
    'member_group': member_group_id,
    'user_object': member_id
}
request_latest = requests.post(f'https://easyverein.com/api/latest/member-group-assignment', json=data_for_post_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["id"], request_latest_json["member_group"], request_latest_json["user_object"])

# Save the group assignment ID for later
group_assignment_id = request_latest_json["id"]

# =================================
# bulk-create new group assignments
# =================================

# In API version `stable`
data_for_bulk_create_stable = {
    'entries': [
        {
            'memberGroup': member_group_id
        }
    ]
}
request_stable = requests.post(f'https://easyverein.com/api/stable/member/{member_id}/groups/bulk-create', json=data_for_bulk_create_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_bulk_create_latest = {
    'entries': [
        {
            'member_group': member_group_id,
            'user_object': member_id
        }
    ]
}
request_latest = requests.post(f'https://easyverein.com/api/latest/member-group-assignment/bulk-create', json=data_for_bulk_create_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))

# =============================
# bulk-update group assignments
# =============================

# In API version `stable`
data_for_bulk_update_stable = {
    'entries': [
        {
            'id': group_assignment_id,
            'paymentActive': True
        }
    ]
}
request_stable = requests.patch(f'https://easyverein.com/api/stable/member/{member_id}/groups/bulk-update', json=data_for_bulk_update_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_bulk_update_latest = {
    'entries': [
        {
            'id': group_assignment_id,
            'payment_active': True
        }
    ]
}
request_latest = requests.patch(f'https://easyverein.com/api/latest/member-group-assignment/bulk-update', json=data_for_bulk_update_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))

# ================================
# Mass action for group assignments
# ================================

# In API version `stable`
data_for_mass_action_stable = {
    "data": {
        "entries": [
            {
                "memberGroup": member_group_id
            }
        ]
    },
    "ids": [member_id]
}
request_stable = requests.patch(f'https://easyverein.com/api/stable/member/groups/mass-action', json=data_for_mass_action_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_mass_action_latest = {
    "data": {
        "entries": [
            {
                "member_group": member_group_id
            }
        ]
    },
    "ids": [member_id]
}
request_latest = requests.patch(f'https://easyverein.com/api/latest/member/mass-action-member-groups', json=data_for_mass_action_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))