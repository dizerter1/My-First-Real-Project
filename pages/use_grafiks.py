import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler, QuantileTransformer

# Load the dataset
df = pd.read_csv("clean_dataset.csv")

# Sidebar for selecting scaling method
with st.sidebar:
    scaling_list = ['No Selected', 'Minmax Scaling', 'Standardization', 'Robust Scaling', 'MaxAbs Scaling', 'Quantile Transformation Scaling']
    selected_scaling = st.selectbox('Select scaling method', scaling_list)

# Apply scaling if selected
if selected_scaling != 'No Selected':
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    if selected_scaling == 'Minmax Scaling':
        scaler = MinMaxScaler()
    elif selected_scaling == 'Standardization':
        scaler = StandardScaler()
    elif selected_scaling == 'Robust Scaling':
        scaler = RobustScaler()
    elif selected_scaling == 'MaxAbs Scaling':
        scaler = MaxAbsScaler()
    elif selected_scaling == 'Quantile Transformation Scaling':
        scaler = QuantileTransformer()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Drop unnecessary columns
df = df.drop(columns=["Unnamed: 0","Unnamed: 0.1"])
st.write(df)


with st.expander("Box Plot of workclass and age"):

    # Create a heatmap
    st.write("### Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Heatmap of Features')
    st.pyplot(fig)

with st.expander("Box Plot of workclass and age"):

    # Create a bar plot
    st.write("### Bar Plot")
    fig, ax = plt.subplots()
    sns.barplot(x='workclass', y='education.num', data=df, ax=ax)
    ax.set_title('Bar Plot of Age by Class')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
    st.pyplot(fig)
    st.write("Biz bar plot orqali workclass hamda education.num ustunlarini chizib oldik. Biz bundan oladigan hulosamiz insonlarni ishlayotgan ishlariga qabul qilinishi uchun qancha vaqt oqiganini tahmin qilish hamda kelajak yoshlari uchun ular hohlagan ishlari uchun tahminiy oquv rejasi tuzish mumkin")

# Create a box plot
with st.expander("Box Plot of workclass and age"):

    st.write("### Box Plot")
    fig, ax = plt.subplots()
    sns.boxplot(y='workclass', x='age', data=df, ax=ax)
    ax.set_title('Box Plot of Age by Class')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
    st.pyplot(fig)
    st.write("### biz bolxplot orqali workclass hamda age ustunlarini grafik korinishiga keltirib oldik va biz bundan data setdagi ish turlarini odatda necha yosh orasida bolishini hamda insonlar u ishda tahmina necha yil ishlashini aniqlashimiz mumkin")

# Create a violin plot
with st.expander("Violin Plot of workclass and educatio.num"):
    st.write("### Violin Plot")
    fig, ax = plt.subplots()
    sns.violinplot(x='workclass', y='education.num', data=df, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
    ax.set_title('Violin Plot of Age by Class')
    st.pyplot(fig)
    st.write("### Biz workclass hamda education.num ustunlarini violin plot orqali tasvirlab odamlarning oqigan yillariga nisbatan qanday ishlarda ishlayotganini aniqlashimiz va shu orqali oquv yillarining miqdori orqali qanday darajadagi ishlarga qabul qilinishini tahminan aytishimiz mumkin ")

with st.expander("Violin Plot of age and native.country"):
    st.write("### Violin Plot")
    fig, ax = plt.subplots()
    sns.violinplot(y='age', x='native.country', data=df, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
    ax.set_title('Violin Plot of Age by Class')
    st.pyplot(fig)
    st.write("### Biz age hamda native.country ustunlarini violin plot orqali tasvirladik. agar bu dataset biron-bir saytga yo ilovaga tegishli bolganda osha sayt yoki ilova qaysi davlatlarda va qaysi yoshlar orasida keng tarqalganini aytish mumkin. ")


with st.expander("countplot of workclass"):
    st.write("### Count Plot")
    fig, ax = plt.subplots()
    sns.countplot(x='race' , data=df, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
    ax.set_title('Count Plot of Passenger Class')
    st.write("Biz bu race ustunini countplot orqali tasvirlab data setdagi insonlarning qanday irqlarda ekanini bilish, hamda agar bu dataset qanqadir saytning foydalanuvchilari bo'lsa , unda bu grafik osha sayt qaysi toifadagi insonlarga koproq manzur kelayotganini tahmin qilish mumkin")

    st.pyplot(fig)
