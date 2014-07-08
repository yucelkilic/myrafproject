#
# fPlot.py -- Plotting function for embedded matplotlib widget with Ginga.
#
# Thanks for Eric Jeschke (eric@naoj.org), https://github.com/ejeschke/ginga
# Copyleft, Yücel Kılıç (yucelkilic@myrafproject.org) and Mohammad Niaei Shameoni (mshemuni@myrafproject.org).
# This is open-source software licensed under a GPLv3 license.

import os
import matplotlib.pyplot as plt
from ginga.mplw.ImageViewCanvasMpl import ImageViewCanvas
from ginga.misc import log
from ginga.AstroImage import AstroImage
from ginga import cmap

class FitsPlot:
    
    def __init__(self, filepath, chartDev):

        self.filepath = filepath
        self.chartDev = chartDev
    
    def plot(self):

        self.chartDev.fig.clf()
        # add matplotlib colormaps to ginga's own set
        cmap.add_matplotlib_cmaps()

        # Set to True to get diagnostic logging output
        use_logger = False
        logger = log.get_logger(null=not use_logger, log_stderr=True)

        # create a ginga object, initialize some defaults and
        # tell it about the figure
        fi = ImageViewCanvas(logger)
        fi.enable_autocuts('on')
        fi.set_autocut_params('zscale')
        #fi.set_cmap(cmap.get_cmap('rainbow3'))
        fi.set_figure(self.chartDev.fig)

        # enable all interactive ginga features
        fi.get_bindings().enable_all(True)

        # load an image  
        image = AstroImage(logger)
        image.load_file(self.filepath)
        fi.set_image(image)
        #fi.rotate(45)

        # plot some example graphics via matplotlib
        # Note adding axis from ginga (mpl backend) object
        ax = fi.add_axes()
        self.chartDev.draw()
