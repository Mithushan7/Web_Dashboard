import dash
from dash import html, dcc 
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv("Datasets/objective1&2-day.csv")
data=pd.read_csv("Datasets/line_data.csv")
dt=pd.read_csv("Datasets/line_data.csv")
data2=pd.read_csv("Datasets/objective4_new.csv")
data1=pd.read_csv("Datasets/objective4.csv")

app = dash.Dash(title="Energy generation App")
app.title = "Spain Energy Generation"

title = html.Div(
    children=[
        html.H1(
            "Spain Energy Generation Analysis",
            className="main_heading")],style={"background-color": "#0a0a92"}
)
footer = html.Div(className="footer",children=[html.Div([html.P('Created by: Mithushan & Sanjay',className="footer_text")])])

info_tab = [
    html.Div(
        id='info',
        className='image_style',
        children=[
            html.Div(children=[
                html.Br(),
                html.H1("This dashboard contains information on Spain's Energy generation and consumption for the year 2015 to 2018",
                        className="sub_heading"
                ),
                html.Br(),
                html.P("This dashboard's main energy-related indicators are attached below;", className='list_main'),
                html.Ul([
                    html.Li("Electricity genetation from Nuclear source - Megawatt (Mw)", className='list_sub'),
                    html.Li("Electricity generation from Natural sources- Megawatt (Mw)", className='list_sub'),
                    html.Li("Electricty generation from Fossil fuel - Megawatt (Mw)", className='list_sub'),
                    html.Li("Total Load (Electrcity demand and usage)- Megawatt (Mw)", className='list_sub'),
                    html.Li("Wastage (wastage of Electricity during Transmission)- Megawatt (Mw)", className='list_sub')
                ]),
                html.P("This dashboard's main weather-related indicators are attached below;", className='list_main'),
                html.Ul([
                    html.Li("Humidity", className='list_sub'),
                    html.Li("Temperature - Kelvin", className='list_sub')
                ]),
                html.P("This dashboard's main price-releated indicators are attached below;", className='list_main'),
                html.Ul([
                    html.Li("Price of total Actual demand - EUR/MWh", className='list_sub')
                ])
            ])]
            )
]

req_1_tab=[     html.P("please select an indicator from the dropdown (Multiselection option available)",
                       className='instruction_text'),
                       
                       dcc.Graph(id='req_1_line',className="line_plot"),
                       html.Div([dcc.Slider(data["Year"].min(),data["Year"].max(),step=1,value=2015,
                                            marks={2015: {'label': '2015','style': {'color': 'black','font-weight': 'bold'}},
                                                   2016: {'label': '2016','style': {'color': 'black','font-weight': 'bold'}},
                                                   2017: {'label': '2017','style': {'color': 'black','font-weight': 'bold'}},
                                                   2018: {'label': '2018','style': {'color': 'black','font-weight': 'bold'}}},
                                                   tooltip={"placement": "bottom", "always_visible": True},className="slider",
                                                   id='year-slider')
                                    ]
                                ),
                                                   
                                 dcc.Dropdown(id="dr_1",value=None,options=[{'label': html.Span("Fossil Fuel",className="dropdown_content"),'value': 'Fossil Fuel'},
                                                                            {'label': html.Span('Renewable Energy',className='dropdown_content'),'value': 'Renewable Energy'},
                                                                            {'label': html.Span('Nuclear',className="dropdown_content"),'value': 'Nuclear'}],
                                              className="dropdown",
                                              multi=True,clearable=True,searchable=True, maxHeight=300,
                                              placeholder="Please select")]
                  


req_2_tab = [   html.P("Please select an indicator for analysis",className="instruction_text"),
                dcc.RadioItems(
                id='spain_variable_selector',
                options=[
                        {'label': 'Daily rolling average price EUR/MWh', 'value': 'price actual'},
                        {'label': 'Daily Average humidity %', 'value': 'humidity'},
                        {'label': 'Daily Average temperature (kelvin)', 'value': 'temp'}],

                        value='price actual',
                        labelStyle={'display': 'block', 'textAlign': 'center'}),
            html.Div(id='correlation-card'),
            html.Br(),
            html.Div(dcc.Graph(id='req_2_scat', className="scatterplot"))
                    ]
                


req_3_tab =[
                 html.P("This section of the Dashboard gives a detailed breakdown of Total Electricity generation from different sources in Spain",
                        className='instruction_text'),
                 html.Br(),
                 html.P("Please select the required year from the checklist (Multiselect option available)",
                        className='instruction_text'),
                
                dcc.Checklist(
                    id='req_3_year_selector',
                    options=[{'label':str(year),'value':year} for year in dt['Year'].unique()],
                    value=[2015],
                    inline=True, #settign the checkbox horizontally
                    className='year_check'),
                
                html.Div([dcc.Graph(id="req_3_barchart", className='pb_graph_aligner'),
                          dcc.Graph(id="req_3_piechart",className='pb_graph_aligner')])
                        ]
                

req_4_tab=[ 
                 html.P("This section of the Dashboard gives the detailed movement of Total Electricity Wastage(Mwh) and explores the Electricity wastage movement along with Total Electrivity load generated",
                        className='instruction_text'),
                 html.P("Please select the required year from the checklist (Multiselect option available)",
                        className='instruction_text'),
                 
                 dcc.Checklist(id='req_4_year_selector',options=[{"label": "2015", "value": 2015},
                                                                 {"label": "2016", "value": 2016},
                                                                 {"label": "2017", "value": 2017},
                                                                 {"label": "2018", "value": 2018}],
                                                                 value=[],inline=True, #settign the checkbox horizontally
                                                                 className='year_check'),
                                                                 
                 html.Div([dcc.Graph(id="bar_req4_chart",className="pb_graph_aligner2"),
                 dcc.Graph(id="line_req4_graph", className='pb_graph_aligner2')]),
                 
                 html.Div([dcc.Graph(id="Scatter_req4_plot",className='scatterplot2')])
                        ]


tab_selected = {
    "background": "linear-gradient(320deg, rgba(23,12,210,1) 0%, rgba(56,56,175,1) 35%, rgba(133,218,236,1) 100%)",
    'color': 'black',
    'font-weight':'bold',
    "font-size": "17px"}

style={"background": "linear-gradient(170deg, rgba(1,5,102,1) 0%, rgba(2,2,154,1) 35%, rgba(145,215,248,1) 100%)",
       "font-size": "16px",
       'color': 'white',
       'font-weight':'bold'}

app.layout = html.Div(className="main",children=[title,
                                dcc.Tabs([

                                    dcc.Tab(label='Energy Information',value='tab1',children=info_tab,className="Tab_style",
                                            selected_style=tab_selected,style=style),

                                    dcc.Tab(label='Monthly Energy Trends',value='tab2',children=req_1_tab,className="Tab_style",
                                            selected_style=tab_selected,style=style),

                                    dcc.Tab(label='Actual Energy Demand Analysis',value='tab3',children=req_2_tab,className="Tab_style",
                                            selected_style=tab_selected,style=style),

                                    dcc.Tab(label='Electricity Source Breakdown',value='tab4',children=req_3_tab,className="Tab_style",
                                            selected_style=tab_selected,style=style),

                                    dcc.Tab(label="Wastage Trend Analysis",value="tab5",children=req_4_tab,className="Tab_style",
                                    selected_style=tab_selected,style=style)]

                                    ),footer])

#
@app.callback(
        Output('req_1_line', 'figure'),
        Input('year-slider', 'value'),
        Input('dr_1','value'))

def update_figure(selected_year,dr_1):  

    data1 = data[data["Year"] == selected_year]

    fig = px.line(data1, x="month", y=dr_1,title="Flow of Electricity Generation in Spain")

    fig.update_yaxes(title_text="Megawatt (MW)",range=[3000000,14000000],
                     title_font=dict(color='white'),tickfont=dict(color='white'))
    
    fig.update_xaxes(title_font=dict(color='white'),tickfont=dict(color='white'))
    fig.update_layout( transition_duration=200,
                       legend=dict(#bgcolor='rgba(0, 0, 255, 0.050)',
                                   font=dict(size=12,color="white"),
                                   x=1.05,
                                   y=1.2,
                                   yanchor="top",
                                   xanchor="right",
                                   borderwidth=0),
                       xaxis=dict(showgrid=True,
                                  gridwidth=0.125,
                                  gridcolor='white'),
                       yaxis=dict(showgrid=True,
                                  gridwidth=0.125,
                                  gridcolor='white'),
                       legend_font_family="Time New Roman",
                       height=550,
                       paper_bgcolor='#19234f',
                       plot_bgcolor='#19234f',
                       title=dict(font=dict(color='white'))) #legend={"x":100,"y":1}= aligning legend position
    fig.update_traces(line=dict(width=4))
    return fig

#requirement Two 
@app.callback(
    Output('req_2_scat', 'figure'),
    Output('correlation-card', 'children'),
    Output('correlation-card','style'),#for correlation card
    Input('spain_variable_selector', 'value')
)
def plot_scatter(selected_option):

    constant_title="Total Electricity demand(MW)"
    if selected_option == 'price actual':
        dynamic_title = 'Daily rolling average price EUR/MWh'
    elif selected_option == 'humidity':
        dynamic_title = 'Daily Average humidity %'
    elif selected_option == 'temp':
        dynamic_title = 'Daily Average temperature (kelvin)'

    fig = px.scatter(df, x='total load actual', y=selected_option, 
                     title=f'{constant_title} vs {dynamic_title}',
                     color=selected_option,color_continuous_scale='OrRd')
    
    fig.update_layout(
    plot_bgcolor='#19234f',  
    paper_bgcolor='#19234f', 
    title=dict( font=dict(color='white'), x=0.5  # z- 0.5 positions the title in the middle
    ),
    xaxis=dict(title=dict(text='Total Electricity demand(MW)', font=dict(color='white')  
                          
        ),
        tickfont=dict(color='white')   #changin title color to white
    ),
    yaxis=dict( title=dict( text=dynamic_title,font=dict(color='white') 
        ),
        tickfont=dict(color='white') 
    ),
    coloraxis_colorbar=dict( title=dict(font=dict(color='white')),
            tickfont=dict(color='white'))
    )
    fig.update_traces(marker=dict(size=6))
    fig.update_xaxes(range=[df["total load actual"].min()+100000,df["total load actual"].max()+100000])


    correlation = df['total load actual'].corr(df[selected_option])

    #if statement for assignign appropriate background colors for correlation
    if correlation > 0:
        cor_card_col = {'backgroundColor': '#61F879'}
    else:
        cor_card_col = {'backgroundColor': '#FB9A94'} 
    
    correlation_card_text=f'Correlation coefficient between Total Electricity demand(Mw) vs {dynamic_title}:  {correlation:.2f}'
    correlation_card_style = {
    'font-family': 'Arial',
    'font-size': '15px',
    'border': '1.5px solid #202643', 
    'padding': '10px',  
    'width': '30%',  
    'margin': 'auto',  
    'textAlign': 'center',  
    'box-sizing': 'border-box',
    'margin-top':'15px',
    'border-radius':'25px',
    **cor_card_col  # This adds the background color based on correlation
}

    

    
    return fig,correlation_card_text, correlation_card_style

#requirment three
@app.callback(
    Output('req_3_barchart','figure'),
    Input('req_3_year_selector','value'))

def bar_chart(clicked_years):
    filter_dt=dt[dt['Year'].isin(clicked_years)]
    group_year_dt=filter_dt.groupby('Year').agg({
        'Fossil Fuel':'sum',
        'Renewable Energy':'sum',
        'Nuclear':'sum'
    }).reset_index()
    
    fig = px.bar(group_year_dt, x='Year',y=['Fossil Fuel', 'Renewable Energy', 'Nuclear'],
                 labels={'value': 'Total Electricity load (MWh)','variable': 'Electricity Source'},
                 title='Total Electricty load generation by source',barmode='group')
  
    fig.update_layout(
    plot_bgcolor='#19234f',  
    paper_bgcolor='#19234f', 
    title=dict( font=dict(color='white'), x=0.5 ),
    legend=dict(font=dict(color='white')),  
    xaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white')),  
    yaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white'))  
    )
    return fig

@app.callback(
    Output('req_3_piechart','figure'),
    Input('req_3_barchart','clickData')
)
def piechart_breakdown (clickData):
    if clickData is not None:
        selected_year = clickData['points'][0]['x']
        clicked_source=clickData['points'][0]['curveNumber']

        if clicked_source == 0:
            sor_col_aggregates=['generation fossil brown coal/lignite', 'generation fossil gas', 'generation fossil hard coal', 'generation fossil oil']
            source_name='Fossil Fuel'
        elif clicked_source == 1:
            sor_col_aggregates=['generation biomass', 'generation hydro pumped storage consumption', 'generation hydro run-of-river and poundage', 'generation hydro water reservoir', 'generation other renewable', 'generation solar', 'generation wind onshore']
            source_name='Renewable Energy'
        elif clicked_source == 2:
            sor_col_aggregates = ['Nuclear']
            source_name = 'Nuclear' 
        
        pie_filtered_dt=dt[dt['Year']==selected_year]
        pie_label=[column.replace('generation','').title() for column in sor_col_aggregates]
        pie_values = [pie_filtered_dt[column].sum() for column in sor_col_aggregates]

        fig = px.pie(values=pie_values,names=pie_label)
        fig.update_layout(
             title=dict(text=f"Breakdown of Electricity Generation for {source_name} in {selected_year}", 
                        font=dict(color='white'),x=0.5),
              plot_bgcolor='#19234f',  
              paper_bgcolor='#19234f',
              legend=dict(font=dict(color='white'))
            )
        

        return fig 
    
    else:
       
        return {}

#Requirement four
@app.callback(
    Output("bar_req4_chart","figure"),
    Input("req_4_year_selector","value"))

def update_figure(value):

    data = data1[data1["year"].isin(value)]
    data["year"]=data["year"].astype(str)

    fig=px.histogram(data, x="year",y="wastage",title='Total Wastage of Electrcity by Year',barmode='group')

    fig.update_yaxes(title_text="Megawatt (MW)",title_font=dict(color='white'),tickfont=dict(color='white'))
    fig.update_xaxes(title_font=dict(color='white'),tickfont=dict(color='white'))

    fig.update_layout( transition_duration=400,
                      legend=dict(#bgcolor='rgba(0, 0, 255, 0.050)',
                                  font=dict(size=12,color="white")),
                      legend_font_family="Time New Roman",
                      paper_bgcolor='#19234f',
                      plot_bgcolor='#19234f',
                      #height=400,
                      #width=800,
                      title=dict(font=dict(color='white'),x=0.5))
    return fig


@app.callback(
    Output('line_req4_graph', 'figure'),
    Input('bar_req4_chart', 'hoverData'),
    Input("req_4_year_selector","value"))

def update_side(hoverdata, value):

    dff2 = data1[data1.year.isin(value)]
    fig = None

    if hoverdata is None:  
        fig = px.line()

        fig.update_layout( transition_duration=200,
                      legend=dict(#bgcolor='rgba(0, 0, 255, 0.050)',
                                  font=dict(size=12,color="white")),
                      legend_font_family="Time New Roman",
                      paper_bgcolor='#19234f',
                      plot_bgcolor="#19234f",
                      title=dict(font=dict(color='white')))

        fig.update_yaxes(title_text="Megawatt (MW)",title_font=dict(color='white'),tickfont=dict(color='white'),range=[5000000,19000000])
        fig.update_xaxes(title_font=dict(color='white'),tickfont=dict(color='white'))

        
    else:

        hov_year = hoverdata["points"][0]["x"]
        hov_year=int(hov_year)
        dff_hovered_year = dff2[dff2.year == hov_year]

        fig = px.line(dff_hovered_year, x="month", y="wastage",title=f"Monthly Electricity Wastage movement - {hov_year}")

        fig.update_layout(
                            legend=dict(font=dict(size=12, color="white")),
                            legend_font_family="Time New Roman",
                            paper_bgcolor='#19234f',
                            plot_bgcolor='#19234f',
                            title=dict(font=dict(color='white'),x=0.5))

        fig.update_yaxes(title_text="Megawatt (MW)",title_font=dict(color='white'),tickfont=dict(color='white'))
        fig.update_xaxes(title_font=dict(color='white'),tickfont=dict(color='white'))

        
    return fig


@app.callback(
    Output("Scatter_req4_plot", "figure"),
    Input("bar_req4_chart", "clickData"),
    Input("req_4_year_selector", "value"))

def update_side1(clickData, value2):

    df3 = data2[data2.year.isin(value2)]
    month_dt = df3.groupby(['day', 'year']).agg({
        'total load actual': 'sum',
        'wastage': 'sum'}).reset_index()
    
    selected_year = None 

    if clickData is not None:
        selected_year = int(clickData["points"][0]["x"])

    if selected_year is not None:
        df3_selected_year = month_dt[month_dt.year == selected_year]

        x_values = df3_selected_year['total load actual']
        y_values = df3_selected_year['wastage']

        correlation = x_values.corr(y_values)

        fig1 = px.scatter(df3_selected_year, x="total load actual", y='wastage',
                          title=f'Correlation analysis of Total Monthly Wastage (Mw) vs Monthly Total Electricity Load (Mw): {correlation:.2f}',
                          color="total load actual", color_continuous_scale='OrRd')

        fig1.update_layout(
                           legend=dict(font=dict(size=12, color="white")),
                           legend_font_family="Time New Roman",
                           paper_bgcolor='#19234f',
                           plot_bgcolor='#19234f',
                           title=dict(font=dict(color='white'),x=0.5),
                           coloraxis_colorbar=dict(title=dict(font=dict(color='white')),
                                                   tickfont=dict(color='white')))

        fig1.update_yaxes(title_text="Wastage in Megawatts(MW)", title_font=dict(color='white'), tickfont=dict(color='white'))
        fig1.update_xaxes(title_text="Total Electricity load in Megawatts(MW)", title_font=dict(color='white'),
                          tickfont=dict(color='white'))

        return fig1
    else:
        
        return {}

if __name__ == '__main__':
    app.run_server(debug=True)
