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
    url = 'http://www.salmoru.com/market/catalog/index.php?pic=2&el_count=1'
    r = get_html(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    page_count = soup.find('div', class_='goodsOf').text.rstrip().split(' ').pop()
    print(page_count)
    main_prop = soup.find_all('tr', class_='bgr-blue2')
    season = main_prop[0].text.lstrip().rstrip()
    categoty = main_prop[1].text.lstrip().rstrip()[6:]+'///'+main_prop[2].text.lstrip().rstrip()[9:]




if __name__ == '__main__':
    main()