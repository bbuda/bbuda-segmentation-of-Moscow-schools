import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
from pygments.lexers import go
import plotly.graph_objs as go
import pygments.lexers.go as go_lexer  # Используйте другой псевдоним


st.set_page_config(
    page_title="GoodSchool",
    page_icon="📊",
)
st.sidebar.success("Выберете интересующий раздел")
conn = st.connection('mysql', type='sql')

st.title('Кластеризация школ Москвы')
agree = st.checkbox('Вывести данные для кластеризации')
if agree:
    cl_df = conn.query('SELECT * FROM data_segmetation')
    st.dataframe(cl_df)
df = conn.query('SELECT * from moscow_schools;', ttl=600)

pca = conn.query('SELECT * FROM pca_ege')
pca['cluster_label'] = pca['cluster_label'].astype(str)
sorted_labels = sorted(pca['cluster_label'].unique(), key=lambda x: int(x))
st.header('Визуализация DBSCAN с использованием понижения размерности')
# Создайте график с упорядоченными метками легенды и установите цветовую палитру tab20
fig = px.scatter(
    pca,
    x="c1",
    y="c2",
    color="cluster_label",
    category_orders={"Метка кластера": sorted_labels},
    color_discrete_sequence=px.colors.qualitative.Light24
)
fig.update_layout(
    xaxis_title="Главная компонента №1",
    yaxis_title="Главная компонента №2",
)
# Отобразите график в Streamlit
st.plotly_chart(fig, use_container_width=True)
df['cluster_label'] = pca['cluster_label']
on = st.toggle('Статистика по кластерам')
if on:
    st.subheader('Всего 18 кластеров, 56 в среднем школ в одном кластере')
    a = []
    r = 0
    for i in range(-1, len(np.unique(pca['cluster_label']))-1):
        cluster_data = df[df['cluster_label'] == str(i)]
        mean_220 = cluster_data['students_220_and_above'].mean()
        mean_160 = cluster_data['students_above_160'].mean()
        dlina = len(cluster_data)
        most_common_district = cluster_data['district'].mode()[0]
        cluster_info = {
            'Кластер': i,
            'Число школ': dlina,
            'Средее число студентов сдавших ЕГЭ >= 220 баллов': mean_220,
            'Средее число студентов сдавших ЕГЭ > 160 баллов': mean_160,
            'Самый часто встречающийся район': most_common_district,
        }
        a.append(cluster_info)

# Создаем DataFrame из списка словарей
    clusters_df = pd.DataFrame(a)
    st.dataframe(clusters_df)
    clusters = list(np.unique(pca['cluster_label']))
    mean_220_values = [item['Средее число студентов сдавших ЕГЭ >= 220 баллов'] for item in a]

    # Создаем объект для группы графиков с одним рядом и одной колонкой
    fig = make_subplots(rows=1, cols=1)

    # Добавляем гистограмму в первый ряд и первую колонку группы графиков
    fig.add_trace(
        go.Bar(
            x=clusters,
            y=mean_220_values,
            marker=dict(color='blueviolet')
        ),
        row=1, col=1
    )

    # Обновляем макет для всей группы графиков
    fig.update_layout(
        title='Статистика по каждому кластеру',
        xaxis=dict(title='Метка кластера'),
        yaxis=dict(title='Среднее число людей сдавших ЕГЭ >= 220 баллов'),
        showlegend=False,

    )
    st.plotly_chart(fig, use_container_width=True)

cluster_labels = df['cluster_label'].unique()


sample_size = st.slider('Размер выборки', 1, 100, 10)


selected_cluster = st.selectbox('Выберите кластер', cluster_labels)


sample = df[df['cluster_label'] == selected_cluster].sample(n=sample_size)


st.dataframe(sample)

if 'label_changes' not in st.session_state:
    st.session_state['label_changes'] = {}


# Функция для обновления названий меток
def update_label_name():
    current_label = st.session_state.current_label
    new_label = st.session_state.new_label
    if current_label and new_label:
        st.session_state.label_changes[current_label] = new_label
        st.success(f"Метка '{current_label}' изменена на '{new_label}'")
        st.session_state.current_label = ""
        st.session_state.new_label = ""


# Получаем уникальные метки кластеров
cluster_labels = pca['cluster_label'].unique()

# Создаем текстовые поля и кнопку для изменения названия метки
with st.form("label_form"):
    st.text_input("Текущее название метки", key="current_label")
    st.text_input("Новое название метки", key="new_label")
    submitted = st.form_submit_button("Обновить название", on_click=update_label_name)

# Применяем изменения к DataFrame
for current_label, new_label in st.session_state.label_changes.items():
    pca.loc[pca['cluster_label'] == current_label, 'cluster_label'] = new_label

# Создаем график с обновленными названиями меток
fig = px.scatter(
    pca,
    x="c1",
    y="c2",
    color="cluster_label",
    title="PCA Кластеризация с обновленными метками",
    color_discrete_sequence=px.colors.qualitative.Light24
)

# Отображаем график в Streamlit
st.plotly_chart(fig, use_container_width=True)
