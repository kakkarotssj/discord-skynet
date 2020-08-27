from abc import ABC, abstractmethod


class EventProcessorBase(ABC):
    """
    Base processor for all event processors
    """

    @classmethod
    @abstractmethod
    def process(cls, keyword, user_id):
        pass
