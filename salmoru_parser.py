from bs4 import BeautifulSoup
import requests

#
def get_html(url):
    login = 'CheJke@gmail.com'
    password = '123456'
    s = requests.Session()
    r = s.get(url, auth=(login, password))
    return (r)

def get_prettydisc(disc):
    disc = str(disc)
    prettydisc = disc.replace('\n\n\n\n\n\n', '').replace('\n\n\n\n\n', '').replace('\n\n\n', ';').replace('• ', '. ').replace('\xa0','').replace('\n?','.').replace('\nК','. К').replace('\nВ','. В').replace('\n', '').replace('..', '.').replace('  ', ' ').replace(' . ', '. ').split(';')
    prettydisc[1] = prettydisc[1].split(':')[1:]
    prettydisc[2] = prettydisc[2].split(':')[1:]
    prettydisc[3] = prettydisc[3].split(':')[1:]
    prettydisc[4] = prettydisc[4].split(':')[1:]
    prettydisc[5] = prettydisc[5].replace('-', ';').replace(' ', '').split(';')[1:]
    return (prettydisc)

def main():
    url = 'http://www.salmoru.com/market/catalog/index.php?pic=2&el_count=1&PAGEN_1=1'
    r = get_html(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    page_count = int(soup.find('div', class_='goodsOf').text.rstrip().split(' ').pop())-1
    prod_property = {}
    for i in range(3):#page_count:
        soup = BeautifulSoup(get_html(f'http://www.salmoru.com/market/catalog/index.php?pic=2&el_count=1&PAGEN_1={i+1}').text, features="html.parser")
        main_prop = soup.find_all('tr', class_='bgr-blue2')
        season = main_prop[0].text.lstrip().rstrip()
        categoty = main_prop[1].text.lstrip().rstrip()[6:]+'///'+main_prop[2].text.lstrip().rstrip()[9:]
        if str(soup.find('td', class_='status-sklad').text.replace('	', '').replace('\n', '')) == 'нет на складе':
            prod_sklad = 'N'
        else:
            prod_sklad = 'Y'
        print(prod_sklad)
        prod_url = 'http://www.salmoru.com/'+soup.find('td', class_='b-top b-right bgr-white').find('a').get('href')
        prod_soup = BeautifulSoup(get_html(prod_url).text, features="html.parser")
        prod_name = prod_soup.find('div', class_='name').text
        prod_artic = prod_soup.find('div', class_='artikul').text.split(': ')[1]
        prod_price =prod_soup.find_all('div', class_='pr red')
        prod_price_opt = prod_price[0].text[:-4].replace(' ', '')
        prod_price_roz = prod_price[1].text[:-4].replace(' ', '')
        prod_img = 'http://www.salmoru.com/'+prod_soup.find('div', class_='photo-switcher').find('img').get('src')
        try:
            prod_sert = 'http://www.salmoru.com/'+prod_soup.find('a', class_='cretificate-file-link').get('href')
        except:
            prod_sert = ''
        prod_props = prod_soup.find('div', class_='cont act').text
        prod_props = get_prettydisc(prod_props)
        prod_property.update({
            'Full_category': categoty,
            'prod_src': prod_url,
            'Name': prod_name,
            'Artikul': prod_artic,
            'price_opt': prod_price_opt,
            'price_roz': prod_price_roz,
            'prod_img': prod_img,
            'prod_sert': prod_sert,
            'prod_props': prod_props[0],
            'prod_props_short:': prod_props[1],
            'prod_manuf': prod_props[2],
            'prod_brand': prod_props[3],
            'prod_country': prod_props[4],
            'prod_season': season,
            'prod_status': prod_props[5],
            'prod_sklad': prod_sklad
        })
        print(prod_property)
        i+=1



if __name__ == '__main__':
    main()