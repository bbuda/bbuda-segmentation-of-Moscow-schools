from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
 [
 Page("streamlit_app.py", "Home", "🏠"),
 Page("other_pages/page2.py", "Page 2", ":books:"),
 ]
)