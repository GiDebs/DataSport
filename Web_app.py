
from dash import Dash,html
import pandas as pd




newData = open(r"C:\Users\Giulio\Documents\GitHub\DataSport\Origini\30_05_22-03_07_22.csv")

df = pd.read_csv("newData")

def generate_table(dataframe , max_rows=10):
    return html.Table([html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Workouts'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
