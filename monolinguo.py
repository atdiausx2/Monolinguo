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
