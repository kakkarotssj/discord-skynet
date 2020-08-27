from .base import EventProcessorBase


class SearchHistoryProcessor(EventProcessorBase):
    """
    Handles messages to search through database for recent searches

    eg: !recent game - results searches from history of user with keyword game
    """

    @classmethod
    def process(cls, keyword, user_id):
        """
        Handles messages to return searches from history for a user

        :param keyword: keyword to search in history table
        :param user_id: user id of the user interacting with server
        :return: list of keyword related searches
        """

        pass
