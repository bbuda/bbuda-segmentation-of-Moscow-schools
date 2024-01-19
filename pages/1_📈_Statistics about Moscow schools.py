import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Statistics of Moscow schools",
    page_icon="📈",
)
st.sidebar.success("Выберете интересующий раздел")
df = pd.read_csv('C:\\Users\\aleks\\EGE.csv')
st.dataframe(df)
pca = pd.read_csv('C:\\Users\\aleks\\Pca_ege.csv')
st.dataframe(pca)
pca['Метка кластера'] = pca['Метка кластера'].astype(str)
st.write(np.unique(pca['Метка кластера']))
fig = px.scatter(pca, x="c1", y="c2", color="Метка кластера",  category_orders={"Метка кластера": sorted(pca['Метка кластера'].unique())})
st.plotly_chart(fig, theme="streamlit", use_container_width=True)