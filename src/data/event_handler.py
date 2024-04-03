import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
class EventHandler:
    def __init__(self) -> None:
      self.__events_repository = EventsRepository()
      
    def register(self, http_request) -> HttpResponse:
      body = http_request.body
      body["uuid"] = str(uuid.uuid4())
      self.__events_repository.insert_event(eventsInfo=body)
      
      return HttpResponse(
        body={"eventId": body["uuid"]},
        status_code=200
      )
      pass