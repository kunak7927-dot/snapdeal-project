import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/tv-and-appliances-republic-day-sale-jan26-store"

r = requests.get(url)

with open("file.html", "w", encoding="utf-8") as f:
    f.write(r.text)


web = requests.get("https://www.tutorialsfreak.com")

print(web)
print(web.content)
print(web.url)
print(web.status_code)

x = BeautifulSoup(web.content, "html.parser")

print(x.prettify())
print(x.title)
print(x.p)
print(x.a)
print(x.find_all("a"))
print(x.select(".title"))

classdata = x.find("div", class_="section subheading")
print(classdata)


res = requests.get("https://example.com")
soup = BeautifulSoup(res.content, "html.parser")

print(soup.title)
print(soup.title.text)

print(soup.select("div.title"))

button = soup.find(
    "button",
    class_="btn btn-primary setup btn-sm mt-2 mx-auto btn"
)
print(button)

items = soup.find_all("li")
for item in items:
    print(item.text)

data = soup.find("span", id="price")

if data:
    print(data)
    print(data.find_next())
    print(data.find_parent())
else:
    print("Price span not found")