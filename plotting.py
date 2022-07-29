from bokeh.plotting import figure, show, output_file
import pandas
from yaml import parse

df = pandas.read_csv("Sample_of_the_produced_time_values.csv", parse_dates=["Start", "End"])

p = figure(x_axis_type = 'datetime', height = 100, width = 500, title = "Motion Graph", sizing_mode = "scale_both")

q = p.quad(left = df["Start"], right = df["End"], bottom = 0, top = 1, color = "green")

output_file('Graph.html')

show(p)

