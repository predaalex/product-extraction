import requests


def fetch_html_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch content from {url}. Status code:{response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None
