from .base import API


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
