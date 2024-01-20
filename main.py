from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()
show_pages(
    [
        Page("home.py", "О проекте", "🏠"),
        Page("pages/page_statistics_schools.py", "Статистика школ Москвы", "📈"),
        Page("pages/page_segmetation.py", "Сегментация школ Москвы", "📊"),
    ]
)