from bokeh.plotting import figure, output_file, show


# Set the output file
output_file("line.html")

# Define the empty plot
plot = figure(plot_width=400, plot_height=400)

# Add a line glyph (also called a renderer) to the plot. Note that
# bokeh expects two equal length sequences
plot.line(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5], line_width=2)

# Generate the plot, the output file, and show in the browser
show(plot)
