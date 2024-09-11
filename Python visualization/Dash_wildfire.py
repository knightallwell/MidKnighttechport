import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Create app
app = dash.Dash(__name__)

# Clear the layout and do not display exceptions till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the wildfire data into pandas dataframe
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')

# Extract year and month from the date column
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()  # Used for the names of the months
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Layout Section of Dash
app.layout = html.Div(children=[
    # Task 2.1: Add the Title to the Dashboard
    html.H1('Australia Wildfire Dashboard from Godwin Allwell', 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 26}),
    
    # Outer division starts
    html.Div([
        # Radio items to select the region
        html.Div([
            html.H2('Select Region:', style={'margin-right': '2em'}),
            dcc.RadioItems(
                options=[
                    {"label": "New South Wales", "value": "NSW"},
                    {"label": "Northern Territory", "value": "NT"},
                    {"label": "Queensland", "value": "QL"},
                    {"label": "South Australia", "value": "SA"},
                    {"label": "Tasmania", "value": "TA"},
                    {"label": "Victoria", "value": "VI"},
                    {"label": "Western Australia", "value": "WA"}
                ],
                value='NSW',  # Default value
                id='region',
                inline=True
            )
        ]),

        # Dropdown to select year
        html.Div([
            html.H2('Select Year:', style={'margin-right': '2em'}),
            dcc.Dropdown(
                options=[{'label': str(year), 'value': year} for year in df['Year'].unique()],
                value=df['Year'].max(),  # Default value
                id='year'
            )
        ]),

        # Second inner division for adding 2 inner divisions for 2 output graphs
        html.Div([
            html.Div([dcc.Graph(id='plot1')], id='plot1-container'),
            html.Div([dcc.Graph(id='plot2')], id='plot2-container')
        ], style={'display': 'flex', 'justify-content': 'space-between'})
    ])
])

# Task 2.4: Add the Output and input components inside the app.callback decorator
@app.callback(
    [Output(component_id='plot1', component_property='figure'),
     Output(component_id='plot2', component_property='figure')],
    [Input(component_id='region', component_property='value'),
     Input(component_id='year', component_property='value')]
)
# Task 2.5: Add the callback function
def reg_year_display(input_region, input_year):
    # Filter data
    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Plot one - Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()
    fig1 = px.pie(est_data, values='Estimated_fire_area', names='Month',
                  title=f"{input_region} : Monthly Average Estimated Fire Area in year {input_year}")

    # Plot two - Monthly Average Count of Pixels for Presumed Vegetation Fires
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()
    fig2 = px.bar(veg_data, x='Month', y='Count',
                  title=f'{input_region} : Average Count of Pixels for Presumed Vegetation Fires in year {input_year}')

    return [fig1, fig2]

if __name__ == '__main__':
    app.run_server(debug=True)
