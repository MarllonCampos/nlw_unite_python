from src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HttpClonfictError
from .error_types.http_not_found import HttpNotFoundError
def handle_error(error: Exception) -> HttpResponse:
  if isinstance(error, (HttpClonfictError,HttpNotFoundError)):
    return HttpResponse(
      body={
        "errors": [
          {
            "title": error.name,
            "details": error.message
            
          }
        ]
      },
      status_code=error.status_code
    )
  return HttpResponse(
    body={
      "errors": [{
        "title": "error",
        "details":str[error]
      }]
    }
  )