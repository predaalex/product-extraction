from bs4 import BeautifulSoup


def preprocess_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove unnecessary elements, scripts, styles, etc.
    for tag in soup(["script", "style", "head"]):
        tag.extract()

    # Get cleaned text content
    cleaned_text = soup.get_text()

    return cleaned_text
