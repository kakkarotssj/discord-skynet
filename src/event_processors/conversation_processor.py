from .base import EventProcessorBase


class ConversationProcessor(EventProcessorBase):
    """
    Handles all non command based or non executable messages
    ~ maintains a map between input and output messages
    """

    input_output_conversation_map = {
        'hi': 'hey'
    }

    @classmethod
    def process(cls, keyword, user_id):
        """
        Processor method to find out the output from the conversation map for the received input

        :param keyword: input keyword
        :param user_id: user id of the user interacting with server
        :return: return expected conversation of the input keyword or return empty string
        """

        return cls.input_output_conversation_map.get(keyword, '')
