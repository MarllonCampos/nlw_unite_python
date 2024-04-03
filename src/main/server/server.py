from flask import Flask
from flask_cors import CORS
from src.main.routes.event_routes import event_route_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)