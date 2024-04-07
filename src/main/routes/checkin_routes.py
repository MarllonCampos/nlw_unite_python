from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler
attendees_route_bp = Blueprint("attendees_route", __name__)
