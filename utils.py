import uuid


class Singleton(object):
    """
    Singleton class to maintain single instance of a class through out app
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def generate_uuid():
    """
    generate uuid
    :return: return uuid
    """

    return uuid.uuid4()
