import os
import sqlite3
from functools import lru_cache

import pandas as pd
from bokeh.layouts import column, layout
from bokeh.models import ColumnDataSource
from bokeh.models.ranges import FactorRange
from bokeh.models.widgets import Div, Select
from bokeh.plotting import curdoc, figure


# Database specifics
db_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "search_interest.db"
)
db_conn = sqlite3.connect(r"{}".format(db_path))

# Queries are parameterised, pandas will populate these when required
interest_query = "SELECT * FROM search_interest WHERE search_interest.language = ?"
region_query = "SELECT * FROM region_search_interest WHERE region_search_interest.language = ? LIMIT 20"


# Setup Widget, options is a list of (value, label) tuples
options = [(li, li) for li in ["Python", "Java", "JavaScript", "Go"]]
lang_select = Select(title="Language:", options=options)


# Create empty figures, glyphs, and datasources. These will be updated later
trend_source = ColumnDataSource(data={"month": [], "interest": []})
trend = figure(
    title="Search Interest over time",
    plot_width=700,
    plot_height=500,
    x_axis_type="datetime",
    y_range=[0, 100],
)
trend.line(x="month", y="interest", line_width=3, source=trend_source)
trend.margin = (20,20,20,20)

bar_source = ColumnDataSource(data={"country": [], "interest": []})
bar = figure(
    title="Top 20 Regions by Search Interest",
    plot_width=350,
    plot_height=500,
    y_range=[],
)
bar.hbar(y="country", left=0, right="interest", height=0.5, source=bar_source)
bar.margin = (20,20,20,20)


# If fetching the data was expensive we could cache it with @lru_cache
@lru_cache()
def fetch_data(language):
    print(f"Fetching data for: {language}")

    si_df = pd.read_sql(
        sql=interest_query, con=db_conn, params=[language], parse_dates=["month"]
    )
    ri_df = pd.read_sql(sql=region_query, con=db_conn, params=[language])

    ri_df.sort_values(by="interest", ascending=True, inplace=True)

    return (si_df, ri_df)


# Callback function, note the method signature
def update(attr, old, new):
    si_df, ri_df = fetch_data(new)

    # Modify the data attribute of the source linked to a glyph.
    # This triggers data to be sent to the front end and re-rendered
    trend_source.data = {"month": si_df["month"], "interest": si_df["interest"]}

    # Also modify the factors, this is not done automatically on change of data
    bar.y_range.factors = ri_df["country"].tolist()
    bar_source.data = {"country": ri_df["country"], "interest": ri_df["interest"]}


# Register callback function by passing the property we expect to change
# and callback's function definition (function name)
lang_select.on_change("value", update)


# Initial render of the chart on start
update(None, None, "Python")


# Add some additional information to the vis as Divs
resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources")

with open(os.path.join(resources_path, "header.html")) as h_file, open(
    os.path.join(resources_path, "interest_note.txt")
) as i_file:
    header = h_file.read()
    note = i_file.read()

header_div = Div(text=header, sizing_mode="stretch_width")
note_div = Div(text=f"<p>{note}</p>", sizing_mode="stretch_width")


# Build layout
l = layout([[header_div], [lang_select], [trend, bar], [note_div]])


# Add to current document for rendering
curdoc().add_root(l)
