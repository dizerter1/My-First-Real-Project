import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title="Population Dashboar",
    page_icon="🐱‍🏍",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Load the data
df = pd.read_csv("clean_dataset.csv")

# Sidebar settings
with st.sidebar:
    st.title('Population dashboard menu')
    df_selected_columns1 = ["workclass", "education", "education.num", "marital.status", "occupation", "relationship", "race", "sex", "native.country", "hours.pek.week", "age", "fnlwgt", "capital.loss", "capital.gain", "income"]
    selected_column1 = st.selectbox('Select column', df_selected_columns1)

    color_theme_list = ['Viridis', 'Cividis', 'Inferno', 'Magma', 'Plasma', 'Turbo', 'Blackbody', 'Bluered', 'Electric', 'Hot', 'Jet', 'Rainbow', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys']
    selected_color_theme = st.selectbox('Select a color theme of histogram', color_theme_list, key='selectbox2')


# Main content
st.title(f"Income Distribution by {selected_column1}")

# Split data based on income
df_below_50k = df[df['income'] == '<=50K']
df_above_50k = df[df['income'] == '>50K']

# Calculate value counts and percentages
workclass_below_50k = df_below_50k[selected_column1].value_counts(normalize=True) * 100
workclass_above_50k = df_above_50k[selected_column1].value_counts(normalize=True) * 100

below_50k_counts = pd.DataFrame(workclass_below_50k).reset_index()
below_50k_counts.columns = [selected_column1, 'Percentage']

above_50k_counts = pd.DataFrame(workclass_above_50k).reset_index()
above_50k_counts.columns = [selected_column1, 'Percentage']

# Pie charts and bin slider
col= st.columns((3,3),gap='medium')

st.subheader("Settings")
bin = st.select_slider(
        "Select number of hole",
        options=list([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]),
        key='bin_slider'
    )
st.write("Selected number of hole:", bin)

with col[0]:
    st.subheader("Income <=50K")
    fig_below_50k = px.pie(below_50k_counts, values='Percentage', hole=bin, names=selected_column1, title=f'Income <=50K Distribution by {selected_column1}', color_discrete_sequence=["blue", "red"], width=450, height=450)
    # fig_below_50k.update_traces(textinfo='none')  # Remove text info
    st.plotly_chart(fig_below_50k)

with col[1]:
    st.subheader("Income >50K")
    fig_above_50k = px.pie(above_50k_counts, values='Percentage', hole=bin, names=selected_column1, title=f'Income >50K Distribution by {selected_column1}', color_discrete_sequence=["blue", "red"], width=450, height=450)
    # fig_above_50k.update_layout(showlegend=False)
    st.plotly_chart(fig_above_50k)

# Histogram settings
st.sidebar.subheader('Histogram Settings')

if selected_color_theme in px.colors.sequential.__dict__.keys():
    color_sequence = px.colors.sequential.__getattribute__(selected_color_theme)
else:
    color_sequence = px.colors.sequential.Viridis
fig = px.histogram(df, x=selected_column1, title=f'Distribution of {selected_column1}', color_discrete_sequence=color_sequence)
st.plotly_chart(fig)


with st.expander('to see dataes', expanded=True):

    df = df.drop(columns=['Unnamed: 0'])
    genre = 'sex'
    genre = st.radio(
    label = "ustun",
    options = df.columns.unique().tolist(),
    index=None,
    )

    dataes = 'Male'
    dataes = st.selectbox("sizga qaysi malumotli qatorlar kerak :",df[genre].unique().tolist())
    if st.button("Jadvalni Ko'rsat"):
    # st.write("Why hello there")
        st.write("You selected:", dataes)

        st.dataframe(df[df[genre]==dataes])
