## RENAME TO DIR_ALUM_ENG_HOME
## Alumni Engagment Dashboard for Director of Alumni Engagement 


import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

try:
    import streamlit_antd_components as sac
except ModuleNotFoundError:
    import os
    os.system('pip install streamlit-antd-components')
    import streamlit_antd_components as sac

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


m = st.markdown("""
<style>
    /* Link to Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
    
    /* Set font for the whole page */
    body {
        font-family: 'Open Sans', sans-serif;
        margin-bottom: -10px;  /* Reduce the space below "Welcome to" */
    }   

    .light-text {
        font-family: 'Open Sans', sans-serif;
        font-weight: 300;  /* light */
        margin-top: 10px;
    }

    /* Optional: Adjust the font size for titles */
    h1 {
        font-family: 'Open Sans', sans-serif;
        margin-bottom: -30px;  /* Reduce the space below "Welcome to" */
    }

    div.stSelectbox > div > div > div > select {
        font-size: 18px;  /* Increase the font size */
        padding: 20px;    /* Increase the padding for larger select boxes */
        border-radius: 8px;  /* Optional: Make the select box rounded */
        border: 2px solid #ddd;  /* Optional: Change the border color */
    }

    div.stButton > button:first-child {
        font-family: 'Open Sans', sans-serif;
        font-weight: 300; /* light weight */
        font-size: 16px;  
        background-color: rgba(151, 166, 195, 0.15);
        color: rgb(0,0,0);
        border: 1px solid rgb(235,235,235);
        border-radius: 8px 8px 8px 8px;
        text-align: left; 
    }

</style>""", unsafe_allow_html=True)


# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Header and personalized greeting
#st.title(f"Welcome, System Administrator {st.session_state['first_name']}!")
st.markdown('<h1 style="font-size: 50px;font-weight: 300;">Engagment Dashboard</h1>', unsafe_allow_html=True)  # Large font for 'Welcome to'

st.markdown('<p class="light-text" style="font-size: 24px;">Welcome, Director of Alumni Relations.</p>', unsafe_allow_html=True)
sac.divider(align='center', color='gray')

## Place here:
##    active user count
# Generate random data for the chart (6 values between 0 and 200)
random_data = np.random.randint(0, 200, size=6).tolist()

# Create DataFrame with the generated data
data_df = pd.DataFrame({
    "Active User Count": [random_data]
})

# Display the editable data with an area chart
st.data_editor(
    data_df,
    column_config={
        "Active User Count": st.column_config.AreaChartColumn(
            "Active User Count",
            width="large",
            help="The connection requests over the last 6 months",
        ),
    },
    hide_index=True,
)

##    connection request

# Generate random data for the chart (6 values between 0 and 200)
random_data = np.random.randint(0, 200, size=6).tolist()

# Create DataFrame with the generated data
data_df = pd.DataFrame({
    "Connection Requests Over Time": [random_data]
})

# Display the editable data with an area chart
st.data_editor(
    data_df,
    column_config={
        "Connection Requests Over Time": st.column_config.AreaChartColumn(
            "Connection Requests Over Time",
            width="large",
            help="The connection requests over the last 6 months",
        ),
    },
    hide_index=True,
)

##    user demographics:
        ##  major
        ##  location


# Create two columns for layout
col1, col2 = st.columns([1, 1])  # First column for active users and connection requests, second column for demographics

# ----------------- Left Column (Active User Count and Connection Requests) -----------------



## Example Containers (not very pretty; change graph sources):
# Line graph for Active User Count
with col1:
    with st.container(border=True):
        st.subheader("Active User Count Over Time")
        days = np.arange(1, 31)
        active_user_count = np.random.randint(50, 500, size=30)  # Simulated user counts

        fig, ax = plt.subplots()
        ax.plot(days, active_user_count, color='red', marker='o')
        ax.set_title('Active User Count Over Time')
        ax.set_xlabel('Days')
        ax.set_ylabel('Active Users')
        ax.grid(True)
        st.pyplot(fig)

# Line graph for Connection Requests
with col1:
    with st.container(border=True):
        st.subheader("Connection Requests Over Time")
        connection_requests = np.random.randint(10, 100, size=30)  # Simulated requests

        fig, ax = plt.subplots()
        ax.plot(days, connection_requests, color='red', marker='x')
        ax.set_title('Connection Requests Over Time')
        ax.set_xlabel('Days')
        ax.set_ylabel('Connection Requests')
        ax.grid(True)
        st.pyplot(fig)

# ----------------- Right Column (Demographics) -----------------

# Custom colors
custom_colors = ['#C63D2F', '#E25E3E', '#FF9B50', '#FFBB5C']
custom_colors_blue = ['#C63D2F', '#E25E3E', '#FF9B50', '#FFBB5C']

# Pie chart for User Demographics - Major
with col2:
     with st.container(border=True):
        st.subheader("User Demographics - Major")
        majors = ['Computer Science', 'Business', 'Psychology', 'Biology', 'Engineering']
        major_counts = np.random.randint(50, 150, size=5)  # Simulated counts of students in each major

        major_data = pd.DataFrame({
        'Major': majors,
        'Count': major_counts
    })

        fig = px.pie(major_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=custom_colors)
        st.plotly_chart(fig)

# Pie chart for User Demographics - Location
with col2:
    with st.container(border=True):
     st.subheader("User Demographics - Location")
     locations = ['New York', 'California', 'Texas', 'Florida', 'Washington']
     location_counts = np.random.randint(50, 200, size=5)  # Simulated counts of users in each location
     location_data = pd.DataFrame({
        'Location': locations,
        'Count': location_counts})
     fig = px.pie(location_data, values='Count', names='Location', title='Location Distribution', color_discrete_sequence=custom_colors_blue)
     st.plotly_chart(fig)   

    