from bs4 import BeautifulSoup
import requests

#
def get_html(url):
    login = 'CheJke'
    password = '123456'
    s = requests.Session()
    r = s.get(url, auth=(login, password))
    return (r)


def main():
    url = 'http://www.salmoru.com/market/catalog/index.php'
    r = get_html(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    # table = soup.find('table', class_ = 'goodList')
    table = soup.find_all('tr', class_ = 'bgr-white')
    for prod_line in table:
        print(prod_line)
    print(len(table))


if __name__ == '__main__':
    main()