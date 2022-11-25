import dash
# import dash_core_components as dcc
import pandas as pd
from dash import dcc
# import dash_html_components as html
from dash import html

# // todo: @games_played and @XP should be loaded at least from config (TOML?) file
class Monolinguo(object):
    def __init__(self, username):
        self.user_name = username
        self.XP = 0
        self.games_played = 0

    def constructLayout(self, app):
        app.layout = html.Div([])
        pass

    def run(self):
        external_stylesheets = [
            { "href": "",
              "rel": ""}
        ]
        app = dash.Dash(__name__
                        # external_stylesheets = external_stylesheets
                        )
        self.constructLayout(app)

        app.title = Monolinguo
        app.run_server(debug=True)
        # fixme: turn this off if not intending to deploy
        server = app.server

    pass
