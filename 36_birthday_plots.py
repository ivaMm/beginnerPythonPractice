import json
from collections import Counter
# basic format of bokeh (ie. histogram)
from bokeh.plotting import figure, show, output_file


MONTHS = {'01': 'Jan',
          '02': 'Feb',
          '03': 'Mar',
          '04': 'Apr',
          '05': 'May',
          '06': 'Jun',
          '07': 'Jul',
          '08': 'Aug',
          '09': 'Sep',
          '10': 'Oct',
          '11': 'Nov',
          '12': 'Dec'
          }

with open('birthdays.json', 'rt') as f:
    birthday = json.load(f)
    months = [MONTHS[date.split('/')[0]] for date in birthday.values()]
    result = Counter(months)

x_categories = [x for x in MONTHS.values()]
x = [x for x in result.keys()]
y = [y for y in result.values()]

# specify an HTML file where the output will go
output_file("birthdays_plot.html")

# create a histogram
p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)






