import numpy as np
from bokeh.layouts import Spacer, row
from bokeh.plotting import figure, output_file, show


# Define data
normal = np.random.normal(0, 0.5, size=1000)
hist, edges = np.histogram(normal, bins=20)

# Default plot
before = figure(title="Before")
before.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])


# New plot for styling
after = figure(title="After", tools="")
after.quad(
    top=hist,
    bottom=0,
    left=edges[:-1],
    right=edges[1:],
    fill_color="orange",
    line_color=None,
    alpha=0.9,
)

# Reduce the data inc by modifying visual properties
after.outline_line_color = None
after.title.text_font_size = "15pt"
after.title.text_alpha = 0.2

after.xgrid.grid_line_color = None

after.ygrid.grid_line_alpha = 0.9
after.ygrid.grid_line_dash = [6, 4]

after.yaxis.minor_tick_line_color = None
after.yaxis.major_tick_line_color = None
# after.yaxis.major_label_orientation = "vertical"
after.yaxis.axis_line_alpha = 0
after.yaxis.major_label_text_alpha = 0.2


show(row(before, Spacer(width=50), after))
