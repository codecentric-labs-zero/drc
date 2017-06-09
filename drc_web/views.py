import matplotlib

matplotlib.use('Agg')

from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import django
import random
import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from matplotlib.patches import Polygon


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
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def radar_plot(request):
    fig = plt.figure(figsize=(10, 10))
    theta = np.linspace(0, 2 * np.pi, 5, endpoint=False)
    angles = theta / (2 * np.pi) * 360
    ax = fig.add_subplot(111, polar=True)
    ax.grid(False)
    ax.set_frame_on(False)
    ax.set_ylim(0, 100)
    ax.set_rticks([])
    ax.set_thetagrids(angles, labels=('A', 'B', 'C', 'D', 'E'))
    ax.set_theta_zero_location('N')
    gridlines = [20, 40, 60, 80]
    for gridline in gridlines:
        radius = np.zeros(len(theta)) + gridline
        points = np.stack((theta, radius), axis=1)
        ax.add_patch(Polygon(points, color='.75', fill=False))
    radius = np.zeros(len(theta)) + 100
    points = np.stack((theta, radius), axis=1)
    ax.add_patch(Polygon(points, color='0', fill=False))
    radius = np.array([55, 75, 62, 80, 15])
    points = np.stack((theta, radius), axis=1)
    ax.add_patch(Polygon(points, color='r', fill=False))
    for t in theta:
        ax.plot((t, t), (0, 100), color='.5', lw=1)

    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
