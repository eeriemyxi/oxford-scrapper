import aiohttp as http
import requests as req
from bs4 import BeautifulSoup as bs4

digits = [str(i) for i in list(range(51))]


class NotFound(Exception):
    pass


class Async():
    @classmethod
    async def define(self, keyword: str):
        if len(keyword.split()) > 1:
            raise ValueError('Only one word could be searched.')
        async with http.ClientSession() as session:
            async with session.get(
                    f'https://www.lexico.com/definition/{keyword}'
            ) as response:
                content = await response.text()
                html = bs4(content, 'html.parser')

                entrywrapper = html.find('div',
                                         attrs={'class': 'entryWrapper'})

                if entrywrapper.find('h2', attrs={'class': 'searchHeading'}):
                    raise NotFound('No definition found.')

                grambs = entrywrapper.find_all(attrs={'class': 'gramb'})
                POS = []

                for gramb in grambs:

                    self.heading = gramb.find('span', attrs={'class': 'pos'})
                    if not self.heading: continue
                    self.heading = self.heading.text.title()

                    self.meaning = [ [ meaning_and_index[0], meaning_and_index[1:] ] for meaning_and_index in [ meaning for meaning in [ meaning_object.text for meaning_object in gramb.find_all('p') ] ] ]
                    self.meaning = [ i if i[0] in digits else ['1', "".join(i) ] for i in self.meaning ]

                    POS.append({
                        'heading': self.heading,
                        'meaning': self.meaning
                    })
                return POS


def define(keyword: str):
    if len(keyword.split()) > 1:
        raise ValueError('Only one word could be searched.')
    content = req.get(f'https://www.lexico.com/definition/{keyword}').text
    html = bs4(content, 'html.parser')

    entrywrapper = html.find('div', attrs={'class': 'entryWrapper'})

    if entrywrapper.find('h2', attrs={'class': 'searchHeading'}):
        raise NotFound('No definition found.')

    grambs = entrywrapper.find_all(attrs={'class': 'gramb'})
    POS = []

    for gramb in grambs:

        heading = gramb.find('span', attrs={'class': 'pos'})
        if not heading: continue
        heading = heading.text.title()

        meaning = [ [meaning_and_index[0], meaning_and_index[1:] ] for meaning_and_index in [ meaning for meaning in [ meaning_object.text for meaning_object in gramb.find_all('p') ] ]]
        meaning = [i if i[0] in digits else ['1', "".join(i)] for i in meaning]

        POS.append({'heading': heading, 'meaning': meaning})
    return POS