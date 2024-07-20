
import pandas as pd
import streamlit as st
import plotly.express as px
import folium
from folium.features import GeoJsonTooltip
from folium.plugins import MiniMap
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import json

# Load the data
data = pd.read_csv("clean_dataset.csv")

# App title
st.write("#### This map for statistic")

# Sidebar Elements
st.sidebar.header("Dashboard Controls")

data["native.country"] = data["native.country"].replace("United-States","United Kingdom")

def filter_data(data):
    """Apply filters based on sidebar selections and return filtered data."""
    if 'education.num' in data.columns:
        min_num, max_num = int(data['education.num'].min()), int(data['education.num'].max())
        num_range = st.sidebar.slider("Select education.num Range", min_num, max_num, (min_num, max_num))
        data = data[data['education.num'].between(num_range[0], num_range[1])]

    if 'hours.per.week' in data.columns:
        min_hour, max_hour = int(data['hours.per.week'].min()), int(data['hours.per.week'].max())
        hours_per_weekk = st.sidebar.slider("Select hours.per.week Range", min_hour, max_hour, (min_hour, max_hour))
        data = data[data['hours.per.week'].between(hours_per_weekk[0], hours_per_weekk[1])]

    if 'income' in data.columns:
        income = data['income'].unique().tolist()
        selected_income = 'United Kingdom'
        selected_income = st.sidebar.multiselect("Select income", income, default=income)
        data = data[data['income'].isin(selected_income)]

    if 'native.country' in data.columns:
        country = data['native.country'].unique().tolist()
        selected_nationalities = st.sidebar.multiselect("Select contries", country, default=country)
        data = data[data['native.country'].isin(selected_nationalities)]

    return data

# Apply Filters
filtered_data = filter_data(data)

# Pie chart for Gender Distribution
fig_income = px.pie(filtered_data, names='income',
                    title='income Distribution',
                    hole=0.4,
                    color_discrete_sequence=['Red', 'Black'])

# Pie chart for Scholarship holder status
fig_scholarship = px.bar(
    filtered_data,
    x='workclass',
    color='workclass',
    title='workclass',
)

fig_scholarship.update_layout(
    xaxis_title='marital.status',
    xaxis_tickangle=-45  # Rotate x-axis labels to -45 degrees
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_income)

with col2:
    st.plotly_chart(fig_scholarship)

# Create a new column 'Country' based on the 'native.country' column
filtered_data['Country'] = filtered_data['native.country']
# st.write(filtered_data['Country'])

# Load GeoJSON file for country boundaries
geojson_file = 'world_countries_geojson.geojson'
with open(geojson_file) as f:
    geojson_data = json.load(f)

# Prepare data for Choropleth
data_map = filtered_data['Country'].value_counts().reset_index()
data_map.columns = ['Country', 'Count']
data_map['Count'] = data_map['Count'].astype(int)  # Convert int64 to int for JSON serialization

# Create and customize the map
def create_map(data_map, geojson_data):
    m = folium.Map(
        location=[20, 0],
        zoom_start=2,
        max_zoom=20,
        min_zoom=1,
        scrollWheelZoom=True,
        maxBounds=[[-60, -180], [85, 180]],  # South-West and North-East corners
        tiles='cartodb positron',
        attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
    )

    choropleth = folium.Choropleth(
        geo_data=geojson_data,
        name='choropleth',
        data=data_map,
        columns=['Country', 'Count'],
        key_on='feature.properties.name',
        fill_color='RdBu',
        fill_opacity=0.7,
        line_opacity=0.5,  # Thicker boundary lines
        line_color='lime',  # Boundary color
        legend_name='Student Contribution by Country'
    ).add_to(m)

    # Ensure data is correctly being passed to the Choropleth layer
    for feature in choropleth.geojson.data['features']:
        country_name = feature['properties']['name']
        feature['properties']['Count'] = int(data_map.set_index('Country').loc[country_name]['Count']) if country_name in data_map['Country'].values else 'No data'

    # Add tooltips to the choropleth
    tooltip = GeoJsonTooltip(
        fields=['name', 'Count'],
        aliases=['Country', 'Count'],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """
    )
    choropleth.geojson.add_child(tooltip)
    folium.LayerControl().add_to(m)

    return m

# Create the map
m = create_map(data_map, geojson_data)

# Display the map
st.components.v1.html(m._repr_html_(), height=600)

# Select numeric columns for PCA
numeric_cols = filtered_data.select_dtypes(include=['float64', 'int64']).columns
numeric_data = filtered_data[numeric_cols]

# Handle missing values
imputer = SimpleImputer(strategy='mean')
numeric_data_imputed = imputer.fit_transform(numeric_data)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(numeric_data_imputed)
