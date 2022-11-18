
from db import getData
from script import getHTMLParser
from db import setData
from bs4 import BeautifulSoup
from uuid import uuid1
from headers import header


def Cards():
    '''
        working: fetches Cards layout from the website
        returns: None
    '''

    link = "https://www.amazon.in/"
    cards = []
    soupHome = getHTMLParser(link, header)

    common_id = "desktop-grid-"

    for i in range(1, 8):
        obj = {}
        obj['id_'] = str(uuid1())
        # ?phase1
        try:
            card_id = common_id+str(i)
            element = soupHome.find('div', id=card_id)
            heading = element.find(
                'h2', class_="a-color-base headline truncate-2line").text

            body = element.find('div', class_="a-cardui-body")
            footer = element.find(
                'div', class_="a-cardui-footer").find('a').text

            obj['heading'] = heading
            obj['footer'] = footer
            # ?phase2
            total_a = body.find_all('a')

            if(len(total_a) == 1):
                image1 = total_a[0].find('img')['src']
                obj['image1'] = image1

            else:
                for i, ele in enumerate(total_a):
                    image = total_a[i].find('img')['src']
                    label = total_a[i].find(
                        'span', class_="a-size-small a-color-base truncate-2line").text
                    obj['image'+str(i+1)] = image
                    obj['label'+str(i+1)] = label
            cards.append(obj)
        except:
            pass

    newCards = []
    i = 1
    j = 0
    flag = True
    while(i < 9 and j < len(cards)):
        if(i == 4 and flag):
            flag = False
            newCards.append({"id_": str(uuid1())})
        else:
            newCards.append(cards[j])
            j += 1
        i += 1

    if(len(getData("Cards")) <= len(newCards)):
        setData("Cards", newCards)

    # for i in newCards:
    #     print(i)
    #     print("------------------")


# Cards()
