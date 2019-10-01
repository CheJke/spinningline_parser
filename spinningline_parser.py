from bs4 import BeautifulSoup
import urllib.request

#функция для получения ссылок всех категорий в меню конкретной страницы
def get_categ_urls(url, html):
    categ_urls = ['https://spinningline.ru/primanki-blsny-c-38208_1.html?page=1&notstockcheck=true', 'https://spinningline.ru/primanki-voblery-c-38208_2.html']
    # !!!!!!!
    return categ_urls

#функция получения html из ссылки
def get_html(url):
    html = urllib.request.urlopen(url).read()
    return html

def main():
    url = 'https://spinningline.ru/'
    html = get_html(url)
    categ_urls = get_categ_urls(url, html)
    categ = []
    prod = []
    i = 0
    # формируем словарь с характеристиками товака каждой категории
    for categ_url in categ_urls:
        categ_html = get_html(categ_url)
        soup = BeautifulSoup(categ_html, features="html.parser")
        categ_name = soup.find('h1', class_='b__hdr-big-text').text
        categ_properties = soup.find_all('span', class_='b-sort__props-item__prop-name')
        categ_property_dict = {
            'Main_category': categ_name
        }
        for categ_property in categ_properties:
            categ_property_dict.update({
                BeautifulSoup(str(categ_property), features="html.parser").find('span').text: ''
            })
        prods = soup.find_all('div', class_='b-prod')
        for prod in prods:
            prod_name = prod.find('div', class_='b-prod__name').text.lstrip().rstrip()
            prod_img = prod.find('img').get('src')
            prod_manuf = prod.find('span', class_='b-prod__manufacturer-text').text
            prod_categ = eval(str(prod.find('a').get('onclick')).replace("dataLayer.push({'event': 'ecommerce','EnchE': 'productClick','ecommerce' : {'click': {'products': [",'').replace(']}}});', '').replace(' / ', '///'))
            if prod.find('div', class_='b-prod__nostock') in prod.find('div', class_='b-prod__offer'):
                prod_price = 0
            else:
                prod_price = int(prod.find('span', class_='b-prod__price_red').text.replace(' ', ''))
            prod_props = prod.find_all('div', class_='b-prod-prop')
            prod_property = categ_property_dict.copy()
            prod_property.update({
                'Name': prod_name,
                'Full_category': prod_categ.get('category'),
                'img': prod_img,
                'Производитель': prod_manuf,
                'price': prod_price
            })
            for prod_prop in prod_props:
                prop = prod_prop.find('span', class_='b-prod-prop__name').text
                val = prod_prop.find('span', class_='b-prod-prop__val').text
                prod_property.update({
                    prop: val
                })

            print (prod_property)


        # #начинаем заполнять товар и его характеристики.
        # prod_page_list = soup.find_all('div', class_='b-prod__info-col')
        # prod_img_list = soup.find_all('div', class_='b-prod__img-col')
        # for prod_page in prod_page_list:
        #     name = prod_page.find('div', class_='b-prod__name').text.lstrip().rstrip()
        #     manufacturer = prod_page.find('div', class_='b-prod__manufacturer').text.lstrip().rstrip()
        #     prod_props = prod_page.find_all('div', class_='b-prod-prop')
        #     prod.append({
        #         'Наименование': name,
        #         'Производитель': manufacturer,
        #     })
        #     for prod_prop in prod_props:
        #         prop = prod_prop.find('span', class_='b-prod-prop__name').text
        #         val = prod_prop.find('span', class_='b-prod-prop__val').text
        #         prod[-1].update({
        #             prop: val
        #         })
        # # начинаем заполнять товар и его характеристики.
        # for prod_img in prod_img_list:
        #     img_small = prod_img.find('img').get('src')
        #     prod_categ = str(prod_img.find('a').get('onclick')).replace("dataLayer.push({'event': 'ecommerce','EnchE': 'productClick','ecommerce' : {'click': {'products': [",'').replace(']}}});', '').replace(' / ','///')
        #     prod_categ_dict = eval(prod_categ)
        #     prod[i].update({
        #         'img': img_small,
        #         'Категория': prod_categ_dict['category']
        #     })
        #     i += 1


    # print(prod)
    # print(categ)



if __name__ == '__main__':
    main()
