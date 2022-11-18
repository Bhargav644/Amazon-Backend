from xml.dom.minidom import Element

from matplotlib.pyplot import title
from db import getData
from script import getHTMLParser
from db import setData
from bs4 import BeautifulSoup
from uuid import uuid1
from headers import header


def Searching(searchby="all"):
    '''
        working: fetches the required tag from website
        returns: response
    '''
    _data = []
    if searchby == "all":
        pass
    else:
        link = 'https://www.amazon.in/s?k='+searchby
        soupHome = getHTMLParser(link, header)
        element = soupHome.find_all('div', class_="s-card-container")
        for ele in element:
            try:
                title = ""
                ratings = 0
                total_ratings = 0
                price = 0
                hidden_price = 0
                discount = 0
                offer = ""
                show = True
                getIt = ""

                _dict = {}
                newele = ele.find('div', class_="s-product-image-container")
                inner_part = newele.find('div', class_="a-section")
                offscreen_price = ele.find(
                    'span', class_="a-price a-text-price")
                discount_div = ele.find(
                    'div', class_="a-row a-size-base a-color-base")
                item_offers = ele.find(
                    'div', class_="a-color-secondary")

                title = ele.find('h2').text

                if(ele.find(
                        'span', class_="a-size-base s-underline-text")):
                    total_ratings = ele.find(
                        'span', class_="a-size-base s-underline-text").text
                if(discount_div.find_all(
                        "span")[-1].text):
                    discount = discount_div.find_all("span")[-1].text

                elif(discount_div.find_all(
                        "span")[-2].text):
                    discount = discount_div.find_all("span")[-2].text
                if(item_offers and item_offers.find_all(
                        'span')[0]):
                    offer = item_offers.find_all(
                        'span')[0].text
                if(ele.find(
                        'span', class_="a-color-base a-text-bold")):
                    getIt = ele.find(
                        'span', class_="a-color-base a-text-bold").text
                try:
                    ratings = ele.find('span', class_="a-icon-alt").text[0:3]
                    price = ele.find('span', class_="a-price-whole").text
                    hidden_price = offscreen_price.find(
                        'span', class_="a-offscreen").text
                except:
                    pass
                _dict['image'] = inner_part.find('img')['src']
            except:
                pass

            #!just adding the important data
            _dict['id_'] = str(uuid1())
            _dict['title'] = title
            _dict['ratings'] = ratings
            _dict['total_ratings'] = total_ratings
            _dict['price'] = price
            _dict['hidden_price'] = hidden_price
            _dict['discount'] = discount
            _dict['getIt'] = getIt
            if(offer.find(getIt) != -1):
                offer = ""
            _dict['offer'] = offer

            try:
                if(_dict['image'] == "" or _dict['title'] == ""):
                    show = False
            except:
                show = False

            _dict['toShow'] = show
            _data.append(_dict)
    return _data
