from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

def test_insert_event():
    event = {
        "uuid": "meu-uuid-e-nois",
        "title": "meu title",
        "maximum_attendees": "max attendies",
        "slug": "meu-slug"
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(eventsInfo=event)
    print(response)