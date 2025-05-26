import requests
from bs4 import BeautifulSoup
import time
import os

def scrape_links(url, delay=1.0, output_folder="scraped_pages"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links on the page
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        # Remove URL fragment (hash) to avoid duplicates caused by section anchors
        href = href.split('#')[0]
        # Filter out javascript or empty links
        if href and not href.startswith("javascript:") and href != "":
            links.append(href)

    # Remove duplicates
    unique_links = list(dict.fromkeys(links))

    print(f"Found {len(unique_links)} unique links on {url}:")

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for idx, link in enumerate(unique_links):
        print(link)
        # Normalize link to full URL if relative
        if link.startswith("/"):
            full_url = url.rstrip("/") + link
        elif link.startswith("http"):
            full_url = link
        else:
            full_url = url.rstrip("/") + "/" + link

        try:
            page_resp = requests.get(full_url, headers=headers)
            page_resp.raise_for_status()
            filename = f"page_{idx+1}.html"
            filepath = os.path.join(output_folder, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(page_resp.text)
            print(f"Saved {full_url} to {filepath}")
        except requests.RequestException as e:
            print(f"Failed to fetch {full_url}: {e}")

        # Removed time.sleep to avoid long delays during testing
        # time.sleep(delay)

    return unique_links

if __name__ == "__main__":
    url = "https://api-reference.checkout.com/"
    scrape_links(url, delay=1.0)
