import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


ax = figure.gca()

def update_blit(artists):
    figure.canvas.restore_region(bg_cache)
    for a in artists:
        a.axes.draw_artist(a)

    ax.figureure.canvas.blit(ax.bbox)

artists = init_func()

for a in artists:
   a.set_animated(True)

figure.canvas.draw()
bg_cache = figure.canvas.copy_from_bbox(ax.bbox)

for f in frames:
    artists = func(f, *fargs)
    update_blit(artists)
    figure.canvas.start_event_loop(interval)
