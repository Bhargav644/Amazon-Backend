import uuid
from script import getHTMLParser
from db import setData
from bs4 import BeautifulSoup
from headers import header
from uuid import uuid1


def HMenu():
    link = 'https://www.amazon.in/'
    soupHome = getHTMLParser(link, header)
    Hdata = [
        {'heading': True, 'title': 'Trending',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Best Sellers',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'New Releases',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Movers and Shakers',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': '', 'sep': True},
        {'heading': True, 'title': 'Digital Content And Devices',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Echo & Alexa',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Fire TV',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Kindle E-Readers & eBooks',
            'sep': False},
        {'heading': False, 'title': 'Audible Audiobooks',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Amazon Prime Vedio',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Amazon Prime Music',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': '', 'sep': True, 'id': str(uuid1())},
        {'heading': True, 'title': 'Shop By Department',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Mobiles & Computers',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'TV & Appliances',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Mens Fashion',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Womens Fashion',
            'sep': False, 'id': str(uuid1())},
        {'heading': False, 'title': 'Kids Fashion',
            'sep': False, 'id': str(uuid1())},
    ]

    setData('HMenu', Hdata)


HMenu()
