import fitz
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text()
    return text

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

pdf_path = 'path_to_your_pdf_file.pdf'
html_path = 'path_to_your_html_file.html'

# Extract text from PDF and generate word cloud
pdf_text = extract_text_from_pdf(pdf_path)
generate_word_cloud(pdf_text)

# Extract text from HTML and generate word cloud
html_text = extract_text_from_html(html_path)
generate_word_cloud(html_text)
