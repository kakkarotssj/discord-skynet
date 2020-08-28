from .base import EventProcessorBase
from repository.managers.search_history_manager import SearchHistoryManager


class SearchHistoryProcessor(EventProcessorBase):
    """
    Handles messages to search through database for recent searches

    eg: !recent game - results searches from history of user with keyword game
    """

    @classmethod
    def process(cls, keyword, user_id):
        """
        Handles messages to return searches from history for a user\

        :param keyword: keyword to search in history table
        :param user_id: user id of the user interacting with server
        :return: list of keyword related searches
        """

        searches = SearchHistoryManager.search_history(keyword, user_id)

        # [{'keyword': 'apple games'}, {'keyword': 'game of thrones'} data retrieved example
        return [list(search.values())[0] for search in searches] # convert dict_values to list and fetch value at 0 index
