import logging

import bs4

from .base import EventProcessorBase
from repository.managers.search_history_manager import SearchHistoryManager
from services.google import GoogleAPI


logger = logging.getLogger()


class SearchGoogleProcessor(EventProcessorBase):
    """
    Handles messages to search on google and return results

    eg: !google nodejs
    """

    output_search_uri = 'https://google.com'

    @classmethod
    def process(cls, keyword, user_id, request_id):
        """
        Search google for the keyword and output top n links from the result page
        Insert the keyword in search history table

        :param keyword: keyword to search in google
        :param user_id: user id of the user interacting with server
        :param request_id: request id assigned to process
        :return: list of top n links
        """

        search_response = GoogleAPI(request_id, user_id).search(keyword)
        links = []
        for link in search_response:
            links.append(cls.output_search_uri+link.get('href'))

        SearchHistoryManager.insert_in_history(keyword, user_id)

        return '\n'.join(links)
