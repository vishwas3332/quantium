import pandas as pd
from dash import Dash,html,dcc, Input,Output

from plotly.express import line

PATH = 'formatted_data.csv'
COLORS = {
    "primary":"#FFDBDB",
    "secondary": "#EB9898",
    "font": "#522A61"
}

data = pd.read_csv(PATH)
data = data.sort_values(by='date')

app = Dash()

def generate_figure(chart_data):
    line_chart = line(chart_data,x='date',y='Sales',title='Sales of Pink Morsel')
    line_chart.update_layout(
        plot_bgcolor = COLORS['secondary'],
        paper_bgcolor = COLORS['primary'],
        font_color = COLORS['font']
    )
    return line_chart

visualization = dcc.Graph(
    id='visualization',
    figure=generate_figure(data)
)

header = html.H1(
    "Sales of Pink Morsel Visualizer",
    id='header',
    style={
        "background-color":COLORS["secondary"],
        'color':'black',
        'boder-radius':'20px'
    }
)

region_picker = dcc.RadioItems(
    ['north','east','south','west','all'],
    'north',
    id='region_picker',
    inline=True
)

region_picker_wrapper = html.Div(
    [region_picker],style={
        'font-size':'150%'
    }
)

@app.callback(
    Output(visualization,"figure"),
    Input(region_picker,"value")
)
def update_graph(region):
    if region == 'all':
        filtered_data =  data
    else:
        filtered_data = data[data['region'] == region]

    figure=generate_figure(filtered_data)

    return figure


app.layout = html.Div(
    [header,visualization,region_picker_wrapper],
    style={
        'textAlign':'center',
        'background-color':COLORS['primary'],
        'boder-radius':'20px'
    }
)

if __name__ =='__main__':
    app.run()
