from flask import Flask
from flask_restful import Resource
from . import players_api

players = {
    1: 'player1',
    2: 'player2',
    3: 'player3'
}

class Players(Resource):
    def get(self, id):
        return players[id], 200

players_api.add_resource(Players, '/players/<int: id>')   