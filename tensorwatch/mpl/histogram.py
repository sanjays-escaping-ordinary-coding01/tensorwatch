# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from .base_mpl_plot import BaseMplPlot
import matplotlib
import matplotlib.pyplot as plt
from .. import utils
import numpy as np
import ipywidgets as widgets

class Histogram(BaseMplPlot):
    def init_stream_plot(self, stream_vis, 
            xtitle='', ytitle='', color=None, 
            bins=None, normed=None, histtype='bar', edge_color=None, linewidth=2,
            opacity=None, **stream_vis_args):
        stream_vis.xylabel_refs = [] # annotation references

        # add main subplot
        stream_vis.bins, stream_vis.normed, stream_vis.linewidth = bins, normed, linewidth
        stream_vis.ax = self.get_main_axis()
        stream_vis.data = []
        stream_vis.hist_bars = [] # stores previously drawn bars

        #TODO: improve color selection
        color = color or plt.cm.Dark2((len(self._stream_vises)%8)/8) # pylint: disable=no-member
        stream_vis.color = color
        stream_vis.edge_color = 'black'
        stream_vis.histtype = histtype
        stream_vis.opacity = opacity
        stream_vis.ax.set_xlabel(xtitle)
        stream_vis.ax.set_ylabel(ytitle)
        stream_vis.ax.yaxis.label.set_color(color)
        stream_vis.ax.yaxis.label.set_style('italic')
        stream_vis.ax.xaxis.label.set_style('italic')

    def is_show_grid(self): #override
        return False

    def clear_bars(self, stream_vis):
        for bar in stream_vis.hist_bars:
            bar.remove()
        stream_vis.hist_bars.clear()

    def clear_plot(self, stream_vis, clear_history):
        stream_vis.data.clear()
        self.clear_bars(stream_vis)

    def _show_stream_items(self, stream_vis, stream_items):
        """Paint the given stream_items in to visualizer. If visualizer is dirty then return False else True.
        """

        vals = self._extract_vals(stream_items)
        if not len(vals):
            return True

        stream_vis.data += vals
        self.clear_bars(stream_vis)
        n, bins, stream_vis.hist_bars = stream_vis.ax.hist(stream_vis.data, bins=stream_vis.bins,
                           normed=stream_vis.normed, color=stream_vis.color, edgecolor=stream_vis.edge_color, 
                           histtype=stream_vis.histtype, alpha=stream_vis.opacity, 
                           linewidth=stream_vis.linewidth)

        stream_vis.ax.set_xticks(bins)

        #stream_vis.ax.relim()
        #stream_vis.ax.autoscale_view()

        return False



   
