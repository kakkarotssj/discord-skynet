from src.event_handler import EventHandler
from utils import generate_uuid


message = '!recent nodejs'
x = EventHandler.execute(message, 'sid', generate_uuid())
print(x)
