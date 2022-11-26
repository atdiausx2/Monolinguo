from monolinguo import Monolinguo
import dash
# import dash_core_components as dcc
import pandas as pd
from dash import dcc
# import dash_html_components as html
from dash import html


def loadData():
    allCorrectedData = pd.read_csv("./essays_20211214.csv", sep=",")



def getLevel():

def selectSubmission(allCorrectedData, n_sentences):
    if n_sentences == 1:

        asignment_suggestion = np.random.choice(a=np.random.choice(
            allCorrectedData[allCorrectedData['mother_tongues'] == mother_tongue_code][
                'original_text'].to_list()).split("."),
                                                size=n_sentences,
                                                replace=False

                                                )
    else:
        suggestionData = allCorrectedData[allCorrectedData['mother_tongues'] == mother_tongue_code].reset_index().iloc[
            sentence_idx]
        suggested_answer = "".join(suggestionData['original_text'].split(".")[:n_sentences])
        correct_answer = "".join(suggestionData['corrected_text'].split(".")[:n_sentences])


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
# server = app.server
# self.server = app.server
# app = Monolinguo(username="kadara")
# app.run()
if __name__ == "__main__":
    # server = app.server
    app.run_server(debug=True)








