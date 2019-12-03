import numpy as np
from bokeh.layouts import row
from bokeh.plotting import figure, output_file, show


# Define data
mu, sigma = 0, 0.5

measured = np.random.normal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=20)

x = np.linspace(-2, 2, 1000)
pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


# Default plot
before = figure(title="Before")
before.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="black")

before.margin = (20, 20, 20, 20)

# New plot for styling
after = figure(title="After", tools="")
after.quad(
    top=hist,
    bottom=0,
    left=edges[:-1],
    right=edges[1:],
    line_color="#2471A3",
    fill_color="#2471A3",
)

# Add a normal curve
after.line(x, pdf, line_color="#A9CCE3", line_width=4, alpha=0.8)

# Reduce the data inc by modifying visual properties
after.outline_line_color = None
after.title.text_font_size = "15pt"
after.title.text_alpha = 0.4
after.margin = margin = (20, 20, 20, 20)

after.xgrid.grid_line_color = None
after.xaxis.axis_line_alpha = 0.4
after.xaxis.major_label_text_alpha = 0.4
after.xaxis.minor_tick_line_color = None
after.xaxis.major_tick_line_color = None

after.ygrid.grid_line_alpha = 0.9
after.ygrid.grid_line_dash = [6, 4]

after.yaxis.minor_tick_line_color = None
after.yaxis.major_tick_line_color = None
after.yaxis.axis_line_alpha = 0
after.yaxis.major_label_text_alpha = 0.4


show(row(before, after, sizing_mode="stretch_width"))
