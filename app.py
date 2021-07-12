import streamlit as st
from streamlit_folium import folium_static

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium


@st.cache
def load_data():
    df = pd.read_csv('data/covid_19_india.csv',parse_dates=['Date'])
    df.replace('Bihar****','Bihar',inplace=True)
    return df

df = load_data()


# menu
options = [
            'Introduction',
            'About'
            'Geo Visualization',
            'Analysis - Univariate',
            'Analysis-Bivarite',
            'Conclusion'
        ]
menu = st.sidebar.radio("Select a variable", options)

if menu == options[0]:
    st.title("Geo Visualization")
    st.image("images/testing.jpeg",use_column_width=True)
    fiop = st.sidebar.slider("fill color opacity", 0.0, 1.0, value=0.7)
    states_df = df.groupby("State/UnionTerritory")['Deaths'].sum().reset_index()
    st.write(states_df)

    map = folium.Map(location=[25,80], zoom_start=4)
    map.choropleth(
        geo_data='data/india_states.json',
        name='choropleth',
        data=states_df,
        columns=['State/UnionTerritory', 'Deaths'],
        key_on='feature.properties.NAME_1',
        fill_color='YlOrRd',
        fill_opacity=fiop,
        line_opacity=0.2,
        legend_name='Deaths'
    )
    folium_static(map)

if menu == options[1]:
    st.title("Univariate Analysis")

if menu == options[2]:
    st.title("Bivariate Analysis")