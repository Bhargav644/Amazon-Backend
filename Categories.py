
from pickletools import uint2
from script import getHTMLParser
from db import setData, getData
from bs4 import BeautifulSoup
from uuid import uuid1


def Categories():
    '''
        working: fetches Categories of the header part from website
        returns: None
    '''

    dict = {'Categories': []}
    link = 'https://www.amazon.in/'
    soupHome = getHTMLParser(link)

    category_content = soupHome.find_all(
        'a', class_="nav-a")

    for i, li in enumerate(category_content):

        # ?indexing in db
        if(i >= 10 and i <= 20):
            dict['Categories'].append(
                {'id_': str(uuid1()),
                 'name': (li.text).strip(),
                 })

    setData('Categories', dict['Categories'])


# Categories()
