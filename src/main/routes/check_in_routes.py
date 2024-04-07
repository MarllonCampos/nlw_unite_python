from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.checkin_handler import CheckInHandler
check_in_route_bp = Blueprint("checkin_route", __name__)


@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
  check_in_handler = CheckInHandler()
  http_request = HttpRequest(param={"attendee_id": attendee_id})
  http_response = check_in_handler.registry(http_request)
  
  return jsonify(http_response.body), http_response.status_code