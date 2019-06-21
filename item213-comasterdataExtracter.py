import requests
from bs4 import BeautifulSoup

#todo Program should go to http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do
#todo should insert the CIN of the company to begin with
#todo SHOULD HAVE THE CAPTCHA CLEARED AND THE SUBMIT BUTTON PRESSED - https://www.scrapehero.com/how-to-solve-simple-captchas-using-python-tesseract/
#TODO Program should be able to find out the various tags
#todo should insert the various tagged items alongwith ACTIVE COMPLIANCE IN PROPER 'EXCEL FILE'
#TODO should loop for the next item in list where director is in Board, search for such company



r = requests.get(
    "http://www.pyclass.com/example.html",
    headers={
        "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
    },
)

c = r.content

# print(c)
# print(type(c))

soup = BeautifulSoup(c, "html.parser")

# print(soup.prettify())

all = soup.find_all("div", {"class": "cities"})

# print(all)
# print(all[0].find_all("h2")[0].text)

for item in all:
    print(item.find_all("p")[0].text)

# all=soup.fin_all("div",)