from flask import Flask
from flask_restful import Api, reqparse

from src.routes.Autorize import Autorize
from src.routes.SearchRoutes import SearchSomething

from src.routes.TokenRoutes import TokenGet, TokenRead, TokenRefresh
from src.routes.PlayerRoutes import PlaySomething, GetDevices, PlayerState, Pause

app = Flask(__name__)
api = Api(app)

api.add_resource(Autorize, '/autorize/')
api.add_resource(SearchSomething, '/search/')
api.add_resource(TokenGet, '/callback/')
api.add_resource(TokenRead, '/token/read/')
api.add_resource(TokenRefresh, '/token/refresh/')

api.add_resource(PlayerState, '/player/state/')
api.add_resource(PlaySomething, '/player/play/<uri>')
api.add_resource(Pause, '/player/pause')
api.add_resource(GetDevices, '/player/devices')

parser = reqparse.RequestParser()

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
    )
