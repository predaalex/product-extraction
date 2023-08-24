from bs4 import BeautifulSoup


def preprocess_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove unnecessary elements, scripts, styles, etc.
    for tag in soup(["script", "style", "head"]):
        tag.extract()

    # Get cleaned text content
    cleaned_text = soup.get_text()

    cleaned_text = cleaned_text.replace(r"\n", "\n")
    cleaned_text = cleaned_text.replace("  ", "")
    cleaned_text = cleaned_text.split("\n")
    cleaned_text = [sentence for sentence in cleaned_text if sentence != "" and sentence != " "]

    return cleaned_text
