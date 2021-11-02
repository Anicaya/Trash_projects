import requests
from bs4 import BeautifulSoup

html_text = requests.get('http://www.nytimes.com').text
soup = BeautifulSoup(html_text, "lxml")

story_heading = soup.find_all("h3")

for story in story_heading:
    try:
        if story.text != "Advertisement":
            print(story.text)
    except AttributeError:
        pass
