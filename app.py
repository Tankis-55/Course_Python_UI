import streamlit as st
import requests

API_URL = 'https://course-python-api-gjdt.onrender.com/items'

st.title("Streamlit Frontend for FastAPI")

# Fetch all items from the backend
def fetch_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    st.error(f"Error fetching items: {response.status_code}")
    return []

# Fetch item by ID
def fetch_item_by_id(item_id):
    response = requests.get(f"{API_URL}/{item_id}")
    if response.status_code == 200:
        return response.json()
    st.error(f"Error fetching item {item_id}: {response.status_code}")
    return None

# Create new item
def create_item(item_data):
    try:
        response = requests.post(API_URL, json=item_data)
        response.raise_for_status()
        st.success("Item created successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating item: {str(e)}")
        return None

# Update item by ID
def update_item(item_id, item_data):
    try:
        response = requests.put(f"{API_URL}/{item_id}", json=item_data)
        response.raise_for_status()
        st.success(f"Item {item_id} updated successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating item: {str(e)}")
        return None

# Delete item by ID
def delete_item(item_id):
    try:
        response = requests.delete(f"{API_URL}/{item_id}")
        response.raise_for_status()
        st.success(f"Item {item_id} deleted successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting item: {str(e)}")

# Streamlit UI
st.subheader("Fetch Items")
if st.button("Fetch All Items"):
    items = fetch_items()
    if items:
        st.write(items)

st.subheader("Fetch Item by ID")
item_id = st.number_input("Item ID", min_value=1, step=1)
if st.button("Fetch Item"):
    item = fetch_item_by_id(item_id)
    if item:
        st.write(item)

st.subheader("Create New Item")
with st.form("create_item_form"):
    new_name = st.text_input("Name")
    new_description = st.text_input("Description")
    new_price = st.number_input("Price", min_value=0.0, step=0.1)
    new_available = st.checkbox("Available", value=True)
    create_submit = st.form_submit_button("Create Item")

    if create_submit:
        new_item = {
            "name": new_name,
            "description": new_description,
            "price": new_price,
            "available": new_available
        }
        create_item(new_item)

st.subheader("Update Item")
with st.form("update_item_form"):
    update_id = st.number_input("Update ID", min_value=1, step=1)
    update_name = st.text_input("Update Name")
    update_description = st.text_input("Update Description")
    update_price = st.number_input("Update Price", min_value=0.0, step=0.1)
    update_available = st.checkbox("Update Available", value=True)
    update_submit = st.form_submit_button("Update Item")

    if update_submit:
        updated_item = {
            "name": update_name,
            "description": update_description,
            "price": update_price,
            "available": update_available
        }
        update_item(update_id, updated_item)

st.subheader("Delete Item")
delete_id = st.number_input("Delete ID", min_value=1, step=1)
if st.button("Delete Item"):
    delete_item(delete_id)
