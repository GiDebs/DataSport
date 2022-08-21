from dash import Dash, dcc, Output, Input 
import dash_bootstrap_components as dbc 
import pandas as pd

#Read the imported file
df = pd.read_csv(r"C:\Users\Giulio\Documents\GitHub\DataSport\Origini\2022-05-30-2022-07-03.csv") 

app = Dash(__name__)

mytext = dcc.Markdown(children='')
dropdown = dcc.Dropdown(df.columns.values[0:],
                        value='Title',
                        clearable=False)

app.layout = dbc.Container([mytext, dropdown])

@app.callback(
    Output(mytext, 'children'),
    Input(dropdown, 'value')
)

def select_column(column_name):
    return('# '+column_name)


if __name__ == '__main__':
    app.run_server(debug=True)
