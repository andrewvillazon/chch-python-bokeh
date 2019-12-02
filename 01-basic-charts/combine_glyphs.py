from bokeh.plotting import figure, output_file, show


output_file("combined_glyphs.html")

plot = figure(plot_width=400, plot_height=400)

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# We add two glpyhs on top of each other to create a combined effect
plot.line(x=x, y=y, line_width=2)
plot.circle(x=x, y=y, fill_color="white", size=8)

show(plot)
