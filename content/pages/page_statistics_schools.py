import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import sqlalchemy
st.set_page_config(
    page_title="GoodSchool",
    page_icon="📈",
)

st.title('Статистика московских школ')
st.sidebar.success("Выберете интересующий раздел")
conn = st.connection('mysql', type='sql')
df = conn.query('SELECT * from moscow_schools;', ttl=600)
ch = df['budget_institution'].sum()
private = df['private_institution'].sum()
round(df['students_220_and_above'].median(), 3)

st.metric("Число сдававших ЕГЭ в Москве за последние 7 лет", df['students_220_and_above'].sum() + df['students_above_160'].sum())
st.metric("Медианное значение выпусников в одной школе, сдавших ЕГЭ >= 220 баллов", round(df['students_220_and_above'].median(), 3), "+3%")
st.metric("Медианное значение выпусников в одной школе, сдавших ЕГЭ > 160 баллов", round(df['students_above_160'].median(), 3), "+5.3%")


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
financing_counts = df[['budget_institution', 'private_institution', 'autonomous_institution', 'military_institution']].sum().reset_index()
financing_counts.columns = ['type', 'count']

type_translation = {
    'budget_institution': 'Бюджетное учреждение',
    'private_institution': 'Частное учреждение',
    'autonomous_institution': 'Автономное учреждение',
    'military_institution': 'Военное учреждение'
    }


financing_counts['type'] = financing_counts['type'].map(type_translation)


fig_type_school = px.bar(
    financing_counts,
    x='type',
    y='count',
    title='Распределение школ по источнику финансирования',
    labels={'type': 'Тип финансирования', 'count': 'Число школ'}  # Задаем подписи на русском языке
)



st.plotly_chart(fig_type_school, use_container_width=True)





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

