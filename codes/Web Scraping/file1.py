import requests
import bs4

code = requests.get("https://projecteuler.net/archives")
soup = bs4.BeautifulSoup(code.text, "lxml")
string = soup.select("title")[0]
print(string.getText())
