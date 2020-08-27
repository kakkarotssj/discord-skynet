from src.event_processors.conversation_processor import ConversationProcessor
from src.event_processors.search_history_processor import SearchHistoryProcessor
from src.event_processors.search_google_processor import SearchGoogleProcessor


class EventHandler(object):
    """
    Entry point for all events received on discord bot and direct them to proper executors
    ~ Maintains a map between event name to activity and call activity's process method

    eg:
        1). hi
        2). !google nodejs
        3). !recent game
    """

    event_processor_map = {
        'conversation': ConversationProcessor,
        '!google': SearchGoogleProcessor,
        '!recent': SearchHistoryProcessor
    }

    @classmethod
    def execute(cls, message, user_id):
        """
        Handler method to run for event received
        ~ if message length is of size 1, assume it's for conversation and modify event message
        ~ run validations on the message
        ~ call process method

        :param message: event message received
        :param user_id: user id of the user interacting with server
        :return: return expected output on basis of handler
        """

        assert isinstance(message, str), "message type is invalid, should be string!"
        if len(message.split()) == 1:
            message = 'conversation ' + message

        action, keyword = message.split(maxsplit=1)
        assert action in cls.event_processor_map, "invalid command"
        processor = cls.event_processor_map[action]
        result = processor.process(keyword, user_id)

        return result
