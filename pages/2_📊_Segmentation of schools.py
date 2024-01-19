import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Segmentation of schools",
    page_icon="📊",
)
st.sidebar.success("Выберете интересующий раздел")
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from product;', ttl=600)

st.dataframe(df)
