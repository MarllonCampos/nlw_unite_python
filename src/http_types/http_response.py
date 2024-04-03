from typing import Dict

class HttpReponse:
  def __init__(self,body: Dict,status_code: int) -> None:
    self.body = body
    self.status_code = status_code