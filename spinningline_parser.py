import sys
from bs4 import BeautifulSoup
import csv
import os
import urllib.request

#функция для получения ссылок всех категорий в меню конкретной страницы
# def get_categ_urls(url, html):
#     soup = BeautifulSoup(html, features="html.parser")
#     urls = []
#     main_urls_list = []
#     main_urls = soup.find('div', class_='lb__content lb__cat left-catalog__content').find_all('a')
#     for main_url in main_urls:
#         main_urls_list.append('https://spinningline.ru'+str(main_url.get('href')))
#     for main_url in main_urls_list:
#         html = get_html(main_url)
#         soup = BeautifulSoup(html, features="html.parser")
#         categ_urls_list = []
#         categ_urls = soup.find('div', class_='lb__content lb__cat left-catalog__content').find_all('a')
#         for categ_url in categ_urls:
#             categ_urls_list.append(str(categ_url.get('href'))+'?notstockcheck=true')
#         urls.append(categ_urls_list)
#     urls = urls[:-1]
#     print(urls)



    # for i in range(0):
    #     categ_urls.append(f'https://spinningline.ru/primanki-blsny-c-38208_1.html?page={i+1}&notstockcheck=true')
    # # !!!!!!!
    # print(categ_urls)
    return main_urls_list

#функция получения html из ссылки
def get_html(url):
    html = urllib.request.urlopen(url).read()
    return html

def main():
    urls = [['https://spinningline.ru/aksessuary-rybolovnye-aksessuary-karpovoj-lovli-c-2590_18383.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-aksessuary-zimnie-c-2590_27968.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-aksessuary-materialy-nahlystovye-c-2590_21068.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-vesy-c-2590_27967.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-glubinomery-c-2590_34618.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-instrumenty-nozhi-c-2590_173376.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-kvoki-c-2590_75527.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-kruzhki-zherlicy-emkosti-zhivca-ae-ratory-c-2590_119135.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-otcepy-c-2590_27955.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-podsacheki-lipgripy-bagry-kukany-sadki-c-2590_30497.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-poleznye-melochi-c-2590_27969.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-signalizatory-poklevki-c-2590_21229.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-stojki-derzhateli-udilishch-sadkov-rodpody-c-2590_27974.html?notstockcheck=true', 'https://spinningline.ru/aksessuary-rybolovnye-firmennaya-suvenirnaya-produkciya-tematicheskaya-literatura-video-c-2590_100475.html?notstockcheck=true'], ['https://spinningline.ru/katushki-bezynercionnye-katushki-c-7_16511.html?notstockcheck=true', 'https://spinningline.ru/katushki-zapasnye-shpuli-c-7_8398.html?notstockcheck=true', 'https://spinningline.ru/katushki-inercionnye-katushki-c-7_16507.html?notstockcheck=true', 'https://spinningline.ru/katushki-komplektujushchie-katushek-c-7_37272.html?notstockcheck=true', 'https://spinningline.ru/katushki-multiplikatornye-katushki-c-7_16508.html?notstockcheck=true', 'https://spinningline.ru/katushki-nahlystovye-katushki-c-7_96125.html?notstockcheck=true', 'https://spinningline.ru/katushki-smazki-katushek-c-7_27956.html?notstockcheck=true'], ['/aksessuary-rybolovnye-c-2590.html?notstockcheck=true', '/katushki-c-7.html?notstockcheck=true', '/komplekty-c-20945.html?notstockcheck=true', '/leska-pletenye-shnury-c-11.html?notstockcheck=true', '/lodki-motory-c-17557.html?notstockcheck=true', '/osnastka-furnitura-c-2672.html?notstockcheck=true', '/podarochnye-sertifikaty-c-6430.html?notstockcheck=true', '/prikormki-nasadki-attraktanty-c-15834.html?notstockcheck=true', '/primanki-c-38208.html?notstockcheck=true', '/udilishcha-c-8095.html?notstockcheck=true', '/hranenie-transportirovka-c-2847.html?notstockcheck=true', '/e-kipirovka-snaryazhenie-c-846.html?notstockcheck=true', '/e-lektronika-c-4436.html?notstockcheck=true', '/ucenennye-tovary-c-145845.html?notstockcheck=true'], ['https://spinningline.ru/leska-pletenye-shnury-nanofil-c-11_28301.html?notstockcheck=true', 'https://spinningline.ru/leska-pletenye-shnury-aksessuary-lesok-shnurov-c-11_173378.html?notstockcheck=true', 'https://spinningline.ru/leska-pletenye-shnury-monofilnaya-leska-c-11_3372.html?notstockcheck=true', 'https://spinningline.ru/leska-pletenye-shnury-pletenyj-shnur-c-11_28712.html?notstockcheck=true', 'https://spinningline.ru/leska-pletenye-shnury-povodkovyj-material-lidery-karpovoj-lovli-c-11_18436.html?notstockcheck=true', 'https://spinningline.ru/leska-pletenye-shnury-fljuorokarbon-c-11_28714.html?notstockcheck=true', 'https://spinningline.ru/leska-pletenye-shnury-shnury-podleski-nahlystovye-c-11_33086.html?notstockcheck=true'], ['https://spinningline.ru/lodki-motory-komplektujushchie-aksessuary-lodok-motorov-c-17557_37305.html?notstockcheck=true', 'https://spinningline.ru/lodki-motory-lodki-boats-c-17557_79024.html?notstockcheck=true', 'https://spinningline.ru/lodki-motory-lodki-c-17557_32304.html?notstockcheck=true', 'https://spinningline.ru/lodki-motory-podvesnye-motory-c-17557_36260.html?notstockcheck=true', 'https://spinningline.ru/lodki-motory-e-lektricheskie-motory-c-17557_31000.html?notstockcheck=true', 'https://spinningline.ru/lodki-motory-yakornye-lebedki-c-17557_34384.html?notstockcheck=true', 'https://spinningline.ru/lodki-motory-yakorya-c-17557_33761.html?notstockcheck=true'], ['https://spinningline.ru/osnastka-furnitura-bombardy-c-2672_35775.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-vertljugi-zastezhki-karabiny-kolca-zavodnye-c-2672_9561.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-gotovye-osnastki-c-2672_37684.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-gruza-cheburashki-c-2672_4.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-derzhatel-silikonovyh-primanok-c-2672_155400.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-dzhiggolovki-c-2672_5.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-zimnie-osnastki-c-2672_24615.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-kormushki-fidernye-c-2672_35768.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-krjuchki-c-2672_16505.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-obzhimnye-trubochki-c-2672_9603.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-ogruzki-c-2672_20813.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-osnastka-zhivca-c-2672_232586.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-osnastka-karpovaya-c-2672_83148.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-osnastka-morskaya-c-2672_225004.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-osnastka-poplavochnaya-donnaya-c-2672_173362.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-povodki-c-2672_12.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-poplavki-c-2672_37304.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-termousadochnye-trubki-c-2672_222107.html?notstockcheck=true', 'https://spinningline.ru/osnastka-furnitura-flippingovye-dzhiggolovki-c-2672_22147.html?notstockcheck=true'], ['/aksessuary-rybolovnye-c-2590.html?notstockcheck=true', '/katushki-c-7.html?notstockcheck=true', '/komplekty-c-20945.html?notstockcheck=true', '/leska-pletenye-shnury-c-11.html?notstockcheck=true', '/lodki-motory-c-17557.html?notstockcheck=true', '/osnastka-furnitura-c-2672.html?notstockcheck=true', '/podarochnye-sertifikaty-c-6430.html?notstockcheck=true', '/prikormki-nasadki-attraktanty-c-15834.html?notstockcheck=true', '/primanki-c-38208.html?notstockcheck=true', '/udilishcha-c-8095.html?notstockcheck=true', '/hranenie-transportirovka-c-2847.html?notstockcheck=true', '/e-kipirovka-snaryazhenie-c-846.html?notstockcheck=true', '/e-lektronika-c-4436.html?notstockcheck=true', '/ucenennye-tovary-c-145845.html?notstockcheck=true'], ['https://spinningline.ru/prikormki-nasadki-attraktanty-system-c-15834_18431.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-attraktanty-hishchnika-c-15834_148444.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-bazovye-smesi-bojlov-c-15834_148475.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-bojly-c-15834_148452.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-gliny-grunty-c-15834_148462.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-dobavki-suhie-c-15834_148451.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-zhidkie-aromatizatory-dobavki-c-15834_148463.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-zernovye-c-15834_126365.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-kraska-prikormki-c-15834_148456.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-nasadki-testo-pasta-c-15834_148464.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-pellets-c-15834_148457.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-prikormki-c-15834_148445.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-prinadlezhnosti-prigotovleniya-prikormki-c-15834_37012.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-rakety-kobry-katapulty-c-15834_18396.html?notstockcheck=true', 'https://spinningline.ru/prikormki-nasadki-attraktanty-rogatki-c-15834_27961.html?notstockcheck=true'], ['https://spinningline.ru/primanki-balansiry-c-38208_3278.html?notstockcheck=true', 'https://spinningline.ru/primanki-blsny-c-38208_1.html?notstockcheck=true', 'https://spinningline.ru/primanki-viby-rattliny-c-38208_10570.html?notstockcheck=true', 'https://spinningline.ru/primanki-voblery-c-38208_2.html?notstockcheck=true', 'https://spinningline.ru/primanki-zimnie-letnie-mormyshki-c-38208_21299.html?notstockcheck=true', 'https://spinningline.ru/primanki-iskusstvennye-nasadki-c-38208_23861.html?notstockcheck=true', 'https://spinningline.ru/primanki-komplektujushchie-blesen-c-38208_138452.html?notstockcheck=true', 'https://spinningline.ru/primanki-komplektujushchie-silikonovyh-primanok-c-38208_192890.html?notstockcheck=true', 'https://spinningline.ru/primanki-komplektujushchie-spinnerbejtov-c-38208_190878.html?notstockcheck=true', 'https://spinningline.ru/primanki-mormyshki-polimernye-c-38208_169030.html?notstockcheck=true', 'https://spinningline.ru/primanki-mormyshki-sudakovye-c-38208_11998.html?notstockcheck=true', 'https://spinningline.ru/primanki-myagkie-primanki-c-38208_8.html?notstockcheck=true', 'https://spinningline.ru/primanki-porolonovye-rybki-c-38208_16566.html?notstockcheck=true', 'https://spinningline.ru/primanki-spinnerbejty-bazzbejty-c-38208_19787.html?notstockcheck=true', 'https://spinningline.ru/primanki-strimery-mushki-c-38208_70350.html?notstockcheck=true', 'https://spinningline.ru/primanki-tejlspinnery-c-38208_141190.html?notstockcheck=true', 'https://spinningline.ru/primanki-furnitura-komplektujushchie-voblerov-dzherkbejtov-c-38208_50523.html?notstockcheck=true', 'https://spinningline.ru/primanki-hvosty-balansirov-c-38208_110259.html?notstockcheck=true', 'https://spinningline.ru/primanki-jubki-vabiki-c-38208_4624.html?notstockcheck=true'], ['https://spinningline.ru/udilishcha-bolonskie-udilishcha-c-8095_38088.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-bortovye-udilishcha-c-8095_104258.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-zapchasti-aksessuary-sborki-udilishch-konnektory-c-8095_165465.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-zimnie-udochki-c-8095_3502.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-karpovye-udilishcha-c-8095_18544.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-kastingovye-dzherkovye-udilishcha-c-8095_16568.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-matchevye-udilishcha-c-8095_2618.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-mahovye-udilishcha-c-8095_38089.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-nahlystovye-udilishcha-c-8095_33759.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-spinningovye-udilishcha-c-8095_14.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-trollingovye-morskie-udilishcha-c-8095_65288.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-udilishcha-lovli-sbirulino-c-8095_130736.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-fidernye-udilishcha-c-8095_15.html?notstockcheck=true', 'https://spinningline.ru/udilishcha-shtekernye-udilishcha-c-8095_216774.html?notstockcheck=true'], ['https://spinningline.ru/hranenie-transportirovka-motovila-povodochnicy-c-2847_27971.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-razgruzochnye-sistemy-c-2847_73675.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-rjukzaki-c-2847_23309.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-sumki-c-2847_52569.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-tubusy-chehly-styazhki-udilishch-c-2847_2626.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-hranenie-zimnih-nasadok-c-2847_136856.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-chehly-c-2847_52570.html?notstockcheck=true', 'https://spinningline.ru/hranenie-transportirovka-yashchiki-korobki-c-2847_3054.html?notstockcheck=true'], ['https://spinningline.ru/e-kipirovka-snaryazhenie-aptechki-c-846_210233.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-barometry-c-846_145624.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-binokli-c-846_70246.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-kemping-c-846_20523.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-kresla-platformy-c-846_35764.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-ledobury-c-846_3401.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-obuv-c-846_3235.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-odezhda-rybalki-c-846_173364.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-ochki-c-846_13615.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-polotenca-c-846_23306.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-sanki-c-846_12150.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-sredstva-uhodu-odezhdoj-obuvju-c-846_33572.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-sushilki-ryby-c-846_138781.html?notstockcheck=true', 'https://spinningline.ru/e-kipirovka-snaryazhenie-e-kipirovka-sitka-c-846_89121.html?notstockcheck=true'], ['https://spinningline.ru/e-lektronika-avtomobilnye-navigatory-c-4436_34891.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-aksessuary-navigatorov-c-4436_4439.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-aksessuary-e-holotov-c-4436_6018.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-videoregistratory-c-4436_34550.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-karty-e-holotov-c-4436_68950.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-podvodnye-videokamery-c-4436_104262.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-portativnye-kolonki-c-4436_186450.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-portativnye-navigatory-c-4436_9.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-portativnye-radiostancii-c-4436_104277.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-fonari-c-4436_27965.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-e-lementy-pitaniya-c-4436_174657.html?notstockcheck=true', 'https://spinningline.ru/e-lektronika-e-holoty-c-4436_4440.html?notstockcheck=true']]
    url = 'https://spinningline.ru/'
    html = get_html(url)
    categ_urls = get_categ_urls(url, html)
    prods_category = []
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
            prods_category.append(prod_property)
        print(categ_url)
        #создаем .csv файл
    try:
        csv_columns = prods_category[0].keys()
        with open(f'{categ_name}.csv', 'w', encoding='utf-8-sig') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns, delimiter=";")
            writer.writeheader()
            for prod in prods_category:
                writer.writerow(prod)

    except Exception as e:
        print(sys.exc_info())



if __name__ == '__main__':
    main()