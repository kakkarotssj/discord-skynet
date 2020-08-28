import psycopg2
import psycopg2.extras

from config import DB_CONFIGURATIONS
from utils import Singleton


class PsycopgDatabaseInterface(Singleton):
    """
    Create singleton class for pyscopg2 database interface which will be used throughout app
    """

    def __init__(self):
        self.db_connection = psycopg2.connect(**DB_CONFIGURATIONS)
        self.cursor = self.db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def query(self, query, params):
        self.cursor.execute(query.format(**params))

    def commit(self):
        self.db_connection.commit()

    def __del__(self):
        self.db_connection.close()


class SearchHistoryQueries:
    """
    Query level to directly talk to database
    """

    db = PsycopgDatabaseInterface()

    @classmethod
    def search_history(cls, keyword, user_id):
        """
        call for database for keyword query

        :param keyword: keyword to look into search history db
        :return: list of search results
        """
        query = """SELECT keyword FROM search_history WHERE user_id='{user_id}' AND keyword LIKE '{keyword}'"""
        cls.db.query(query, {'user_id': user_id, 'keyword': '{}{}{}'.format('%', keyword, '%')})
        search_results = cls.db.cursor.fetchall()

        return search_results

    @classmethod
    def insert_in_history(cls, keyword, user_id):
        """
        insert keyword in database

        :param keyword: keyword to insert
        :return: None
        """

        search_query = """SELECT keyword FROM search_history WHERE user_id='{user_id}' AND keyword='{keyword}'"""
        cls.db.query(search_query, {'user_id': user_id, 'keyword': keyword})
        search_results = cls.db.cursor.fetchall()
        if not search_results:
            query = """INSERT INTO search_history (keyword, user_id) VALUES('{keyword}', '{user_id}')"""
            cls.db.query(query, {'user_id': user_id, 'keyword': keyword})
            cls.db.commit() # do this in processor on exception handling and rollback
