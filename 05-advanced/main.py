from bokeh.layouts import row
from bokeh.plotting import curdoc, figure


p1 = figure(title="Indie flower", plot_height=300, plot_width=300)
p1.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], radius=0.2, alpha=0.5)
p1.title.text_font = "Indie flower"
p1.title.text_font_size = "40px"

p2 = figure(title="Roboto", plot_height=300, plot_width=300)
p2.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], radius=0.2, alpha=0.5)
p2.title.text_font = "Roboto"
p2.title.text_font_size = "40px"

curdoc().add_root(row(p1, p2))
