from django import template
from bs4 import BeautifulSoup  # Убедись, что библиотека установлена (pip install beautifulsoup4)

register = template.Library()

@register.filter
def limit_html_tags(value):
    """
    Ограничивает HTML-контент одним <h3> и одним <p>.
    """
    if not value:
        return ""
    
    soup = BeautifulSoup(value, "html.parser")

    # Извлекаем только первый <h3> и <p>
    h3_tag = soup.find("h3")
    p_tag = soup.find("p")

    # Создаём новый HTML-контент с нужными тегами
    result_html = ""
    if h3_tag:
        result_html += str(h3_tag)
    if p_tag:
        result_html += str(p_tag)

    return result_html
