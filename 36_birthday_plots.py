import json
from collections import Counter
from calendar import month_name
# basic format of bokeh (ie. histogram)
from bokeh.plotting import figure, show, output_file

MONTHS = {'01': 'January',
          '02': 'February',
          '03': 'March',
          '04': 'April',
          '05': 'May',
          '06': 'June',
          '07': 'July',
          '08': 'August',
          '09': 'September',
          '10': 'October',
          '11': 'November',
          '12': 'December'
          }

month_lookup = list(month_name)

with open('birthdays.json', 'rt') as f:
    birthday = json.load(f)
    months = [MONTHS[date.split('/')[0]] for date in birthday.values()]
    r = Counter(months)
    result = {key: r[key] for key in sorted(r.keys(), key=month_lookup.index)}


x = [x[0:3] for x in result.keys()]
y = [y for y in result.values()]
colors = ['#fcba03', '#0f20d9', '#f0720c', '#f0240a', '#11cc0a', '#ab05a3', '#13d6bf', '#e81a88', '#9ab009',
          '#f571d4', '#71f5b3', '#fa602d']

# specify an HTML file where the output will go
output_file("birthdays_plot.html")

# create a histogram
p = figure(x_range=x, plot_height=350, plot_width=630, title='Birthday plots',
           toolbar_location=None, tools="")
p.vbar(x=x, top=y, width=0.9, legend_field="x", color=colors)

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 7
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

# render (show) the plot
show(p)
