from bokeh.plotting import figure, output_file, show, save


output_file("bar.html")

# https://www.statista.com/statistics/263264/top-companies-in-the-world-by-market-value/
big_4 = ["Apple", "Amazon", "Google", "Facebook"]
market_val = [961.3, 946.5, 863.2, 512]

p = figure(
    title="Market Value of the Big 4",
    x_range=big_4,
    y_range=[0, max(market_val) + 50],
    plot_height=500,
)
p.vbar(x=big_4, top=market_val, width=0.9)

# Modify visual properties
p.xgrid.grid_line_color = None
p.yaxis.axis_label = "Billion U.S. dollars"

show(p)
# save(p) # Saves instead of save and open in browser
