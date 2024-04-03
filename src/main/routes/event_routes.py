from flask import Blueprint, jsonify

event_route_bp = Blueprint("event_rouite", __name__)


@event_route_bp.route("/events", methods=["POST"])
def create_events():
  return jsonify({"ola": "mundo"}), 200