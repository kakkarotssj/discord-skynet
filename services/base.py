import logging

import requests


logger = logging.getLogger()


class API(object):
    """
    Generic API class which can be inherited to create an api integration
    """

    uri = None
    actions = {}
    REQUEST_METHODS = {
        'GET': lambda url, params, headers: requests.get(url, params, headers=headers)
    }

    def __init__(self, request_id, user_id):
        self.request_id = request_id
        self.user_id = user_id

    def request(self, action, headers={}, url_slugs=[], params={}, payload={}):
        """
        Make call for api request

        :param action: action to perform on api ~ to be defined in base classes
        :param headers: key value of headers
        :param url_slugs: list of slug values in the URL
        :param params: key value pair of query params
        :param payload: payload data
        :return: response received from api
        """

        response = None
        action_data = self._get_action(action)
        request_method = action_data['method']
        endpoint = action_data['endpoint']
        if request_method in ('POST', 'PUT'):
            headers.update({'Content-Type': 'application/json'})
        url = self._get_url(endpoint, url_slugs)
        try:
            logger.info(f'Request id: [{self.request_id}], User id: [{self.user_id}], '
                        f'request sent: url: {url} params {params} headers {headers}')
            response = self.REQUEST_METHODS[request_method](url, params, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f'Request id: [{self.request_id}], User id: [{self.user_id}], '
                         f'HTTP error occurred: {err}')
        except requests.exceptions.Timeout as err:
            logger.error(f'Request id: [{self.request_id}], User id: [{self.user_id}], '
                         f'Request timed out: {err}')
        except requests.exceptions.TooManyRedirects as err:
            logger.error(f'Request id: [{self.request_id}], User id: [{self.user_id}], '
                         f'Too many redirects: {err}')
        except requests.exceptions.RequestException as err:
            logger.error(f'Request id: [{self.request_id}], User id: [{self.user_id}], '
                         f'Ambiguous exception occurred while handling request: {err}')

        return response

    def _get_action(self, action):
        """
        Helper method to get action's data defined in child classes containing endpoints and request method

        :param action: action key defined in child class
        :return: action data
        """

        return self.actions[action]

    def _get_url(self, endpoint, url_slugs):
        """
        Helper method to create url by appending endpoint to the uri and adds url slugs into it.
        In cases of appending slugs, endpoint will defined in child class as something like: /search/{}

        :param endpoint: endpoint string
        :param url_slugs: list of values to be appended to the url as the slug
        :return: return complete url of the request
        """

        return self.uri + endpoint.format(*url_slugs)
