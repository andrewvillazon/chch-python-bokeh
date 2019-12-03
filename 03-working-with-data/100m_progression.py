import os
from datetime import datetime

import numpy as np
import pandas as pd
from bokeh.models import BoxAnnotation, ColumnDataSource, LabelSet
from bokeh.models.tools import HoverTool
from bokeh.plotting import figure, output_file, show


output_file("100m_progress.html")

# Wrangle data with pandas
hm_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "100m.tsv")
hm_df = pd.read_csv(hm_file, sep="\t", dtype={"time": np.float}, parse_dates=[4])


# Custom tool tip
hover_template = """
    <div style="width: 350px">
        <div>
            <span style="font-size: 20px; font-weight: 600;">@time s.</span>
        </div>
        <div>
            <span style="font-size: 12px; font-weight: 200;">@athlete, @nationality</span>
        </div>
        <div>
            <span style="font-size: 12px; font-weight: 200;">@date{%F} @location</span>
        </div>
        <div>
            <p>@note</p>
        </div>
    </div>
"""
hover = HoverTool(tooltips=hover_template, formatters={"date": "datetime"})

# Build plot
p = figure(
    plot_width=1000,
    title="100m World Record Progression",
    x_axis_type="datetime",
    tools=[hover, "pan", "reset", "undo", "redo", "save", "box_zoom"],
)
p.sizing_mode = "stretch_both"
p.margin = (50, 50, 50, 50)
p.title.text_font_size = "20pt"

statuses = ["Ratified", "Not ratified", "Ratified but later rescinded"]
markers = ["circle", "asterisk", "circle_x"]
colors = ["#43A047", "#FF8F00", "#C62828"]

# Iteratively add glyphs
for status, marker, color in zip(statuses, markers, colors):
    p.scatter(
        x="date",
        y="time",
        source=ColumnDataSource(hm_df.loc[hm_df["status"] == status]),
        size=20,
        marker=marker,
        fill_color=color,
        line_color=color,
        alpha=0.8,
        legend_label=status,
        muted_color=color,
        muted_alpha=0.2,
    )

p.legend.click_policy = "mute"

# Add Labels Annotation
labels = LabelSet(
    x="date",
    y="time",
    text="time",
    level="glyph",
    x_offset=-20,
    y_offset=-20,
    source=ColumnDataSource(hm_df),
    render_mode="canvas",
    text_font_size="7pt",
    text_alpha=0.4,
)

# Period of time when times were taken manually
manual_time = BoxAnnotation(
    left=datetime(1900, 1, 1, 0, 0),
    right=datetime(1977, 1, 1, 0, 0),
    fill_alpha=0.1,
    fill_color="#2874A6",
)

# Add annotations to figure
p.add_layout(labels)
p.add_layout(manual_time)


# Output
show(p)
