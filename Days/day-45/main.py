from bs4 import BeautifulSoup
import requests

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string) #you can use .prettify()
print(soup.a)
print(soup.li)
print(soup.p)

all_anchor_tag = soup.find_all(name="a")
all_paragraph_tag = soup.find_all(name="p")

for tag in all_anchor_tag:
    print(tag.getText()) #nombres de los links
    print(tag.get("href")) #links

heading = soup.find(name= "h1", id="name") #solo buscara lo que cumple la especificacion
section_heading = soup.find(name="name", class_="heading") #class_ reserved keyword in python
print(section_heading.get("class"))

    
company_url = soup.select_one(selector= "p a")  #select_ine gives you the first match, and select gives you all the matches
names = soup.select_one(selector= "#name")
headings = soup.select_one(selector= ".heading")
print(company_url)

 

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_tags= soup.find_all(name="a", class_="storylink")

for article_tag in article_tags:
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_upvote = article_tag.find_next_sibling(name="span", class_="score")
    
    if article_upvote:
        print(f"Title: {article_text}")
        print(f"Link: {article_link}")
        print(f"Upvote: {article_upvote.getText()}\n")