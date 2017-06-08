from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import django
import random
import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import matplotlib.patches as patches


def ping(request):
    return HttpResponse("I am alive.", content_type="text/plain")


def matplotlib(request):
    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def heat_map(request):
    group1 = ['France', 'Italy', 'Spain', 'Portugal', 'Germany']
    group2 = ['Japan', 'China', 'Brazil', 'Russia', 'Australia']

    data = np.random.rand(5, 5)

    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.gray)

    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_xticklabels(group2, minor=False)
    ax.set_yticklabels(group1, minor=False)

    # Assumption: Use TkAgg as backend:
    # plt.show()

    # Assume: Use Agg as backend:
    # plt.savefig("./img/my-heatmap.png")
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def radar_plot(request):
    response = ''
    '''
    fig, ax = plt.axes(polar=True)

    theta = np.linspace(0, 2 * np.pi, 8, endpoint=False)
    radius = .25 + .75 * np.random.random(size=len(theta))
    points = np.vstack((theta, radius)).transpose()

    plt.gca().add_patch(patches.Polygon(points, color='.75'))

    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    '''
    return response
