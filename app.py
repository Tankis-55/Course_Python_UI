import streamlit as st
import requests


API_URL = 'https://course-python-api-gjdt.onrender.com/items'

### Service fetch_items
def fetch_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    st.error(f'Error fetching items : {response.status_code}')
    return []

### Service fetch_item by id
def fetch_item():
    response = requests.get(f'{API_URL}/{item_id}')
    if response.status_code == 200:
        return response.json()
    st.error(f'Error fetching item by ID : {response.status_code}')
    return None

###Frontend
st.title('Custom application with backend')

###Fetch Items
st.subheader('Fetch Items')
if st.button('Fetch all Items'):
    items = fetch_items()
    st.write(items)

###Fetch Items by id
st.subheader('Fetch Items by ID')
item_id = st.number_input('Item ID', min_value=1)
if st.button('Fetch  Item'):
    item = fetch_item()
    st.write(item)
