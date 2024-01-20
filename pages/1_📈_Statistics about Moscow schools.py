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
st.title('Статистика московских школ')
st.sidebar.success("Выберете интересующий раздел")
df = pd.read_csv('C:\\Users\\aleks\\EGE.csv')
summ = df['students_220_and_above'].sum() + df['students_above_160'].sum()
ch = df['budget_institution'].sum()
private = df['private_institution'].sum()
sr = round(df['students_220_and_above'].mean(), 3)
st.metric("Число сдававших ЕГЭ в Москве за последние 7 лет", summ)
st.metric("Медианное значение выпусников в одной школе, сдавших ЕГЭ >= 220 баллов", sr, "+3%")
st.metric("Число бюджетных заведений", ch, "+1.9%")
st.metric("Число частных заведений", private)

# График распределения по административным округам
fig3 = px.histogram(df, x='admin_district', title='Распределение школ по административным округам')
fig3.update_layout(
    xaxis_title="Административный округ",
    yaxis_title="Число школ",
)
st.plotly_chart(fig3, use_container_width=True)
st.markdown(
    """
    Из графика видно, что число школ в каждом АО не сильно разнится, не считая
    недавно образовавшихся - Троицкого, Номосковского, Зеленоградского 
    """
)
fig_ege_district = px.bar(df, x='admin_district', y='students_220_and_above', title='Средний балл ЕГЭ по административным округам', color='private_institution')
st.plotly_chart(fig_ege_district, use_container_width=True)
def filter_schools_by_district(df, district):
    return df[df['district'] == district]


# Заголовок страницы


# Селектор района
districts = df['district'].unique()
selected_district = st.selectbox('Выберите район:', districts)

# Кнопка для отображения школ в выбранном районе
if st.button('Показать школы в районе'):
    filtered_df = filter_schools_by_district(df, selected_district)
    st.write(filtered_df)

