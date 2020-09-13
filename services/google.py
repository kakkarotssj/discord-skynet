import re

import bs4

from .base import API


# put these in different files
class ResponseScrapper(object):

    link_tag = 'div#main > div > div > div > a'

    @classmethod
    def scrape(cls, response, parser):
        soup = bs4.BeautifulSoup(response.text, parser)
        all_links = soup.select(cls.link_tag)

        return all_links


class SizeFilter(object):
    # make base class for all post filters

    @staticmethod
    def apply_filter(response):
        return response[:min(5, len(response))]


class GoogleAPI(API):
    """
    API class to help in google searching
    ~ define uri of google
    ~ define actions map, for every action define endpoint and request method
    """

    uri = 'https://google.com'
    actions = {
        'SEARCH': {
            'endpoint': '/search',
            'method': 'GET'
        }
    }

    valid_pre_filters = ('sort', )
    valid_post_filters = ('size', )
    post_filter_to_action_map = {
        'size': SizeFilter
    } # merge this map and tuple

    @classmethod
    def parse_keyword(cls, keyword):
        is_valid = True
        search_keyword, filters = None, {}
        pattern = re.compile('(.*) --.*')
        match = pattern.match(keyword)
        try:
            search_keyword = match.group(1)
        except IndexError:
            is_valid = False
            # do proper error handling here

        for filter in cls.valid_pre_filters + cls.valid_post_filters:
            pattern = re.compile('.* --{filter}=(\\d+)'.format(filter=filter))
            match = pattern.match(keyword)
            try:
                filters[filter] = match.group(1)
            except IndexError:
                is_valid = False
            # do proper error handling here

        assert is_valid is True, "Search statement is invalid"

        return search_keyword, filters

    @classmethod
    def segregate_filters(cls, filters):
        pre_filters, post_filters = {}, {}
        for filter_key, filter_val in filters.items():
            if filter_key in cls.valid_pre_filters:
                pre_filters[filter_key] = filter_val
            elif filter_key in cls.valid_post_filters:
                post_filters[filter_key] = filter_val

        return pre_filters, post_filters

    @classmethod
    def apply_post_filters(cls, response, post_filters):
        for filter_key, filter_val in post_filters.items():
            response = cls.post_filter_to_action_map[filter_key].apply_filter(response)

        return response


    @staticmethod
    def build_query_params(search_keyword, pre_filters):
        query_params = {'q': search_keyword}
        query_params.update(pre_filters)

        return query_params

    def search(self, keyword):
        search_keyword, filters = self.parse_keyword(keyword)
        pre_filters, post_filters = self.segregate_filters(filters)
        params = self.build_query_params(search_keyword, pre_filters)

        search_response =  self.request('SEARCH', params=params)
        # response.raise_for_status()
        # avoiding raise for status for now

        response = ResponseScrapper.scrape(search_response, 'html.parser')
        if post_filters:
            response = self.apply_post_filters(response, post_filters)

        return response
