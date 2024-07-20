import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px


df = pd.read_csv("14.csv")
data = pd.read_csv("clean_dataset.csv")
with st.expander("untidy data"):
  st.write(df)
with st.expander(" Kodi "):
    st.write('''df["age"] = df["age"].fillna(value=df.groupby("native.country")["age"].transform("mean")
             df["age"] = df["age"].fillna(value=df["age"].mean())''')
col = st.columns((2,2),gap='medium')
df1 = df['age'].isna().mean() * 100
df2 = 100 - df1
data1 = data['age'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title='Percentage of NaN Values in Age Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title='Percentage of NaN Values in Age Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["workclass"] = df["workclass"].fillna(value=df["workclass"].mode()[0])''')
col = st.columns((2,2),gap='medium')
colm = 'workclass'
df1 = df['workclass'].isna().mean() * 100
df2 = 100 - df1
data1 = data['workclass'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["education"] = df["education"].fillna(value=df["education"].mode()[0])''')
col = st.columns((2,2),gap='medium')
colm = 'education'
df1 = df['education'].isna().mean() * 100
df2 = 100 - df1
data1 = data['education'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)


with st.expander(" Kodi "):
    st.write('''df["income"] = df["income"].fillna(value=df["income"].mode()[0])''')
col = st.columns((2,2),gap='medium')
colm = 'income'
df1 = df['income'].isna().mean() * 100
df2 = 100 - df1
data1 = data['income'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)


with st.expander(" Kodi "):
    st.write('''df["occupation"] = df["occupation"].fillna(value=df.groupby("income")["occupation"].transform((lambda x: x.mode()[0] if not x.mode().empty else None)))
''')
col = st.columns((2,2),gap='medium')
colm = 'occupation'
df1 = df['occupation'].isna().mean() * 100
df2 = 100 - df1
data1 = data['occupation'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)


with st.expander(" Kodi "):
    st.write('''df["hours.per.week"] = df["hours.per.week"].fillna(value=df.groupby("occupation")["hours.per.week"].transform("median"))

''')
col = st.columns((2,2),gap='medium')
colm = 'hours.per.week'
df1 = df['hours.per.week'].isna().mean() * 100
df2 = 100 - df1
data1 = data['hours.per.week'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["race"] = df["race"].fillna(value=df.groupby("native.country")["race"].transform(lambda x: x.mode()[0] if not x.mode().empty else None))
''')
col = st.columns((2,2),gap='medium')
colm = 'race'
df1 = df['race'].isna().mean() * 100
df2 = 100 - df1
data1 = data['race'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["education.num"] = df["education.num"].fillna(value=df.groupby("education")["education.num"].transform("mean"))''')
col = st.columns((2,2),gap='medium')
colm = 'education.num'
df1 = df['education.num'].isna().mean() * 100
df2 = 100 - df1
data1 = data['education.num'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["native.country"] = df["native.country"].fillna(value=df["native.country"].mode()[0])
''')
col = st.columns((2,2),gap='medium')
colm = 'native.country'
df1 = df['native.country'].isna().mean() * 100
df2 = 100 - df1
data1 = data['native.country'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["capital.gain"] = df["capital.gain"].fillna(value=df["capital.gain"].mode()[0])

''')
col = st.columns((2,2),gap='medium')
colm = 'capital.gain'
df1 = df['capital.gain'].isna().mean() * 100
df2 = 100 - df1
data1 = data['capital.gain'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["capital.loss"] = df["capital.loss"].fillna(value=df["capital.loss"].mode()[0])''')
col = st.columns((2,2),gap='medium')
colm = 'capital.loss'
df1 = df['capital.loss'].isna().mean() * 100
df2 = 100 - df1
data1 = data['capital.loss'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)




with st.expander(" Kodi "):
    st.write('''df["relationship"] = df["relationship"].fillna(value=df["relationship"].mode()[0])
''')
col = st.columns((2,2),gap='medium')
colm = 'relationship'
df1 = df['relationship'].isna().mean() * 100
df2 = 100 - df1
data1 = data['relationship'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)





with st.expander(" Kodi "):
    st.write('''df["fnlwgt"] = df["fnlwgt"].fillna(value=df["fnlwgt"].mode()[0])
''')
col = st.columns((2,2),gap='medium')
colm = 'fnlwgt'
df1 = df['fnlwgt'].isna().mean() * 100
df2 = 100 - df1
data1 = data['fnlwgt'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)




with st.expander(" Kodi "):
    st.write('''df["fnlwgt"] = df["fnlwgt"].fillna(value=df["fnlwgt"].mode()[0])
''')
col = st.columns((2,2),gap='medium')
colm = 'fnlwgt'
df1 = df['fnlwgt'].isna().mean() * 100
df2 = 100 - df1
data1 = data['fnlwgt'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)


with st.expander(" Kodi "):
    st.write('''df['native.country'] = df['native.country'].replace("United-States",'United-Kingdom')''')
col = st.columns((2,2),gap='medium')
colm = 'native.country'
df1 = df['native.country'].isna().mean() * 100
df2 = 100 - df1
data1 = data['native.country'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''df["marital.status"] = df["marital.status"].fillna(value=df.groupby("relationship")["marital.status"].transform(lambda x: x.mode()[0] if not x.mode().empty else None))''')
col = st.columns((2,2),gap='medium')
colm = 'marital.status'
df1 = df['marital.status'].isna().mean() * 100
df2 = 100 - df1
data1 = data['marital.status'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)



with st.expander(" Kodi "):
    st.write('''def get_mode(series):
    return series.mode().iloc[0] if not series.mode().empty else None
df['sex'] = df.groupby('relationship')['sex'].transform(lambda x: x.fillna(get_mode(x)))
''')
col = st.columns((2,2),gap='medium')
colm = 'relationship'
df1 = df['relationship'].isna().mean() * 100
df2 = 100 - df1
data1 = data['relationship'].isna().mean() * 100
data2 = 100 - data1
data_for_pie = pd.DataFrame({
      'Category': ['NaN Values', 'Non-NaN Values'],
      'Percentage': [df1, df2]
  })
data_for_pie1 = pd.DataFrame({
    'Category': ['NaN Values', 'Non-NaN Values'],
    'Percentage': [data1, data2]
})

with col[0]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=  ["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)
with col[1]:
  st.title("NaN Values in Age Column")
  fig = px.pie(data_for_pie1, values='Percentage', names='Category', title=f'Percentage of NaN Values in {colm} Column', color_discrete_sequence=["blue", "red"])
  st.plotly_chart(fig, width=290, height=290)

with st.expander("cleaned data"):
  st.write(df)