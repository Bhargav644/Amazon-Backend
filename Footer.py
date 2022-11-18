from db import getData
from script import getHTMLParser
from db import setData
from bs4 import BeautifulSoup
from uuid import uuid1
from headers import header


def Footer():
    '''
        working: fetches footer layout
        returns: None
    '''

    link = "https://www.amazon.in/"
    main = []
    soupHome = getHTMLParser(link, header)

    footerEle = soupHome.find_all(
        'div', class_="navFooterLinkCol navAccessibility")

    for i, v in enumerate(footerEle):
        footer = {}
        footer["heading"+str(i)] = v.find('div',
                                          class_="navFooterColHead").text
        ele = []
        list = v.find_all('li')
        for k in list:
            ele.append((k.text).replace('\n', ""))

        footer["footer"+str(i)] = ele

        main.append(footer)

    # if(main==None){
    #     getData
    # }
    setData("Footer", main)


# Footer()
