from flask import Blueprint
from flask_restful import Api

players_bp = Blueprint('players_bp', __name__,
                        url_prefix='/players')
players_api = Api(players_bp)