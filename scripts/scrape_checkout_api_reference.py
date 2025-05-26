import requests
from bs4 import BeautifulSoup

def fetch_checkout_api_reference():
    url = "https://api-reference.checkout.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Attempt to remove cookie consent popup if present
    cookie_popup = soup.find("div", {"class": "cookie-consent"})
    if cookie_popup:
        cookie_popup.decompose()

    # Extract main content - this depends on the page structure
    main_content = soup.find("main") or soup.find("div", {"id": "main-content"}) or soup.body

    if not main_content:
        print("Could not find main content on the page.")
        return None

    # Extract headings and code blocks as a simple example
    content = []
    for element in main_content.descendants:
        if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            content.append(f"\n{element.name.upper()}: {element.get_text(strip=True)}\n")
        elif element.name == "pre":
            code = element.get_text()
            content.append(f"CODE BLOCK:\n{code}\n")

    return "\n".join(content)

if __name__ == "__main__":
    page_content = fetch_checkout_api_reference()
    if page_content:
        print(page_content)
    else:
        print("Failed to extract content.")
