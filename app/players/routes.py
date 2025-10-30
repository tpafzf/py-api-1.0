from flask import Flask
from flask_restful import Resource
from .players_bp import players_api

import nfl_data_py as nfl_data
import pandas as pd
import numpy as np

class Players(Resource):
    def get(self, season):
        
        result = nfl_data.import_seasonal_data([2024], 'REG')
        json = result.to_json()
        return json, 200 


players_api.add_resource(Players, '/get/<int:season>')   