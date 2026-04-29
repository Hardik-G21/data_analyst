import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 1. Load Data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day20/meetmux_transactions.csv")

df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
df['Month'] = df['PurchaseDate'].dt.strftime('%Y-%m')

# 2. Initialize App
app = dash.Dash(__name__)

# 3. Layout
app.layout = html.Div([

    html.H1(
        "Business Growth & Analytics Dashboard",
        style={'textAlign': 'center'}
    ),

    # Summary Card
    html.Div(
        id='total-revenue-card',
        style={
            'padding': '20px',
            'fontSize': '24px',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'backgroundColor': '#f2f2f2',
            'marginBottom': '20px'
        }
    ),

    # Dropdown
    html.Div([
        html.Label("Select Activity Category:"),
        dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': i, 'value': i} for i in df['Category'].unique()],
            value=df['Category'].unique()[0]
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    # Graphs
    html.Div([
        dcc.Graph(id='trend-graph'),
        dcc.Graph(id='revenue-pie')
    ])
])

# 4. Callback
@app.callback(
    [Output('trend-graph', 'figure'),
     Output('revenue-pie', 'figure'),
     Output('total-revenue-card', 'children')],
    [Input('category-dropdown', 'value')]
)
def update_graphs(selected_category):

    filtered_df = df[df['Category'] == selected_category]

    # 📈 Line Chart with Hover Data
    line_fig = px.line(
        filtered_df,
        x='PurchaseDate',
        y='TransactionAmount',
        title=f'Revenue Trend: {selected_category}',
        hover_data=['CustomerID', 'Quantity']
    )

    # Pie Chart
    pie_fig = px.pie(
        filtered_df,
        names='Region',
        values='TransactionAmount',
        title=f'Revenue Distribution by Region: {selected_category}'
    )

    # Total Revenue
    total_revenue = filtered_df['TransactionAmount'].sum()

    return line_fig, pie_fig, f"Total Revenue: ₹{total_revenue:,.0f}"


# 5. Run App
if __name__ == '__main__':
    app.run(debug=True)