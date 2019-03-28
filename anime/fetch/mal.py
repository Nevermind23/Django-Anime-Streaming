import requests
from .anime import Anime

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "Scrapy/0.24.2 (+http://scrapy.org)",
}

class mal(object):
    def _fetch(self, obj):
        data = requests.get(obj._get_url(), headers=HEADERS).text
        obj.parse(data)
        obj.fetched = True

    def _handle_related(self, obj):
        related = {'anime': Anime}
        for key, values in obj.related.items():
            obj.related[key] = [related[v['type']](v['id'], self) for v in values]

    def get_anime(self, mal_id):
        return Anime(mal_id, self)
