# Web Scraping Project using Python v0.1
from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the Hacker News website
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Initialize lists to store article information
article_titles = []
article_links = []
article_upvotes = []

# Extract article titles and links
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

# Extract article upvotes
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# Find the index of the article with the maximum upvotes
max_upvotes_index = article_upvotes.index(max(article_upvotes))

# Display the information of the most upvoted article
print(
    f"{article_titles[max_upvotes_index]}, "
    f"{article_upvotes[max_upvotes_index]} points, "
    f"available at: {article_links[max_upvotes_index]}."
)
# END OF CODE
