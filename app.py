from monolinguo import Monolinguo
import dash
# import dash_core_components as dcc
import pandas as pd
from dash import dcc
# import dash_html_components as html
from dash import html

def constructLayout( app):
    app.layout = html.Div([])
    pass

external_stylesheets = [
    {"href": "",
     "rel": ""}
]
app = dash.Dash(__name__
                # external_stylesheets = external_stylesheets
                )
constructLayout(app)

app.title = Monolinguo

# fixme: turn this off if not intending to deploy
server = app.server
# self.server = app.server
# app = Monolinguo(username="kadara")
# app.run()
if __name__ == "__main__":
    # server = app.server
    app.run_server(debug=True)








