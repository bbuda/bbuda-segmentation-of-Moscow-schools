from st_pages import Page, show_pages, add_page_title
import  streamlit as st

show_pages(
    [
        Page("content/home.py", "О проекте", "🏠"),
        Page("content/pages/page_statistics_schools.py", "Статистика образовательных заведений Москвы", ":chart_with_upwards_trend:"),
        Page("content/pages/page_segmetation.py", "Сегментация школ Москвы", "📊")
    ]
)


