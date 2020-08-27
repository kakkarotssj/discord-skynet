from src.event_handler import EventHandler


message = '!google nodejs'
x = EventHandler.execute(message, 'sid')
print(x)
