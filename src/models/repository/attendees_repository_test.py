from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dado")
def test_insert_attendee():
  event_id = "meu-uuid-e-nois2"
  attenddee_info = {
    "uuid": "meu-uuid-attendee",
    "name": "attendee name",
    "email": "attende@email.com",
    "event_id": event_id
  }
  
  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attenddeInfo=attenddee_info)
  print(response)
  
@pytest.mark.skip(reason="Busca desnecessária")
def test_get_attendee_badge_by_id():
  attendde_id = "meu-uuid-attendee"
  attendees_repository = AttendeesRepository()
  attendee = attendees_repository.get_attendee_badge_by_id(attendee_id=attendde_id)
  print(attendee)