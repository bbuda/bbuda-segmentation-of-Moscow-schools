import streamlit as st
st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)
st.title('Добро пожаловать на GoodSchool. Подобрать подходящую школу в Москве теперь проще!')

st.sidebar.success("Выберете интересующий раздел")
st.markdown(
    """
    На данный момент в Москве работает больше **1000** различных школ, гимназий, лицеев
    и это число будет дальше расти. Выбор учебного заведения для ребенка с каждым годом все усложняется,
    родителям необходимо опираться на множество параметров при своем выборе,
    при этом, именно среднее общее образование закладывает фундамент будущего успеха ребенка.
    Этот сервис создан с целью облегчить подбор школы ребенку
    ### Параметры на которых основывается сервис при подборе учебного заведения:
    - Результативность заведения, измеряемая в баллах ЕГЭ
    - Территориальное расположение школы (Округ, Район)
    - Источник финансирования
    - Форма образования (Основная, альтернативная)
"""
)
import streamlit as st
import base64

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    # Используйте стили CSS для уменьшения и позиционирования изображения
    html = r'''
    <div style="position: fixed; right: 90px; top: 600px; transform: scale(2.3);">
        <img src="data:image/svg+xml;base64,%s" style="max-width: 100px; max-height: 100px;"/>
    </div>
    ''' % b64
    c = st.container()
    c.write(html, unsafe_allow_html=True)

# Чтение содержимого SVG файла
with open("D:\\book-education-food-svgrepo-com.svg", "r") as file:
    svg = file.read()
    render_svg(svg)
st.caption("Основано на [открытых данных:](https://data.mos.ru/opendata/2072)")
