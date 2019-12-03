# https://catalogue.data.govt.nz/dataset/bus-stops1

import os
import sqlite3

import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import get_provider, Vendors


output_file("bus_stops.html")

db_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "bus_stops.db"
)
db_conn = sqlite3.connect(r"{}".format(db_path))

query = "SELECT * FROM stop WHERE stop.owner='Metro Christchurch'"

stops_df = pd.read_sql(query, db_conn, index_col="stop_id")
stops = ColumnDataSource(stops_df)


tile_provider = get_provider(Vendors.CARTODBPOSITRON)

TOOLTIPS = [
    ("Platform No", "@platform_no"),
    ("Platform Name", "@platform_name"),
    ("Routes", "@routes"),
    ("x", "$x"),
    ("y", "$y"),
]

geo = figure(
    title="Christchurch Bus Stops",
    plot_height=600,
    plot_width=1000,
    x_axis_type="mercator",
    y_axis_type="mercator",
    tooltips=TOOLTIPS,
    tools="pan,wheel_zoom,box_zoom,reset,zoom_in,zoom_out",
)
geo.add_tile(tile_provider)
geo.circle(
    x="lat_mercator", y="long_mercator", alpha=0.5, source=stops, fill_color="red"
)

geo.sizing_mode = "stretch_both"
geo.margin = (50, 50, 50, 50)
geo.title.text_font_size = "20pt"

show(geo)
