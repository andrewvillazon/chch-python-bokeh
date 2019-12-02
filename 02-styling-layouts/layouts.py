import numpy as np
from bokeh.layouts import column, gridplot, row
from bokeh.palettes import Blues9, Cividis11, RdYlGn11, Viridis11
from bokeh.plotting import figure, output_file, show
from bokeh.transform import linear_cmap


output_file("layouts.html")

# Define charts
p1 = figure(title="One", plot_width=w, plot_height=h)
p2 = figure(title="Two", plot_width=w, plot_height=h)
p3 = figure(title="Three", plot_width=w, plot_height=h)
p4 = figure(title="Four", plot_width=w, plot_height=h)

plots = [p1, p2, p3, p4]

# Chart settings
N, w, h = 100, 300, 300
palettes = [Viridis11, Cividis11, Blues9, RdYlGn11]

# Build up glyphs iteratively
for plot, palette in zip(plots, palettes):
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sizes = (5 * np.random.rand(N)) ** 2

    mapper = linear_cmap(field_name="y", palette=palette, low=min(y), high=max(y))

    plot.circle(x=x, y=y, color=mapper, size=sizes, alpha=0.7)


# Construct the layout with one of these methods
# l = row(*plots)
# l = column(*plots)
# l = gridplot(plots, ncols=2, sizing_mode="stretch_both")
l = gridplot(plots, ncols=2, sizing_mode="stretch_height")

show(l)
