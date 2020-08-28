from repository.queries.search_history_queries import SearchHistoryQueries


class SearchHistoryManager:
    """
    Manager level to separate out business logic from db querying
    """

    search_history_queries = SearchHistoryQueries

    @classmethod
    def search_history(cls, keyword, user_id):
        """
        call for query level of search history on keyword

        :param keyword: keyword to look into search history db
        :return: list of search results
        """

        return cls.search_history_queries.search_history(keyword, user_id)

    @classmethod
    def insert_in_history(cls, keyword, user_id):
        """
        call for query level to insert keyword in database

        :param keyword: keyword to set into search history db
        :return None
        """

        return cls.search_history_queries.insert_in_history(keyword, user_id)
