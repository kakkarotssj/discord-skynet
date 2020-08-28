import bs4

from .base import EventProcessorBase
from repository.managers.search_history_manager import SearchHistoryManager
from services.google import GoogleAPI


class SearchGoogleProcessor(EventProcessorBase):
    """
    Handles messages to search on google and return results

    eg: !google nodejs
    """

    top_n_links = 5
    link_tag = 'div#main > div > div > div > a'
    output_search_uri = 'https://google.com'

    @classmethod
    def process(cls, keyword, user_id):
        """
        Search google for the keyword and output top n links from the result page
        Insert the keyword in search history table

        :param keyword: keyword to search in google
        :param user_id: user id of the user interacting with server
        :return: list of top n links
        """

        search_response = GoogleAPI().request('SEARCH', params={'q': keyword})
        soup = bs4.BeautifulSoup(search_response.text, 'html.parser')
        all_links = soup.select(cls.link_tag)
        links = []
        for index in range(min(cls.top_n_links, len(all_links))):
            links.append(cls.output_search_uri+all_links[index].get('href'))

        SearchHistoryManager.insert_in_history(keyword, user_id)

        return links
