import os
from bs4 import BeautifulSoup
from bs4.element import Comment
import warnings
from bs4 import XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def tag_visible(element):
    # Filter function to check if an element is visible text
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    # Also exclude elements with CSS that hides them (optional, but requires more complex checks)
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(text=True)
    visible_texts = filter(tag_visible, texts)
    return u"\\n".join(t.strip() for t in visible_texts if t.strip())

def main():
    input_folder = 'scraped_pages'
    output_folder = 'parsed_pages'
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.html'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_path = os.path.join(output_folder, output_filename)

            with open(input_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            visible_text = text_from_html(html_content)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(visible_text)

if __name__ == '__main__':
    main()
