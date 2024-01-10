from bs4 import BeautifulSoup
import requests
import json

def parse_currency():
    # do scrapping "$"(usd), "€"(eur), "£"(gbp), "¥"(jpy), "₽"(rub)
    with open('measurments.json', 'r') as f:
        config = json.load(f)
    codes = ['usd', 'eur', 'gbp', 'jpy']
    result = []
    url = "https://www.banki.ru/products/currency/cb/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    currencies = soup.find_all("tr", attrs={"data-test":"currency-table-row"})
    # all rows in table
    for code in codes:
        for cur in currencies:
            if cur['data-currency-code'] == code.upper():
                result.append(cur.select("td:nth-child(4)")[0].get_text())
    i = 0
    for num in result:
        config["currency"][codes[i].upper()][0] = round((1/float(num)), 4)
        config["currency"][codes[i].upper()][1] = float(num)
        i += 1
    with open('measurments.json', 'w') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pass