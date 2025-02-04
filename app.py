from dash import Dash
import dash_bootstrap_components as dbc
from layouts import create_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = Dash(__name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css'
    ],
    suppress_callback_exceptions=True
)

# Set up the app layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

server = app.server  # For deployment
#http://127.0.0.1:8062/
if __name__ == '__main__':
    app.run_server(debug=True, port=8062)
