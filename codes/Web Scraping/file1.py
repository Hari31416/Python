import requests
import bs4

code = requests.get("https://coppermind.net/wiki/Cytonic_(book)")
soup = bs4.BeautifulSoup(code.text, "lxml")
images = soup.select(".image")
image = images[0]
print(image[src])
