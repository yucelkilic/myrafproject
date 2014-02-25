#!/usr/bin/env python
import os
import pyfits

class FitsPlot:
    
    def __init__(self, filepath, chartDev):
        
        self.filepath = filepath
        self.chartDev = chartDev
    
    def dataFits(self):
        
        f = pyfits.open(self.filepath)
        fitsData = f[0].data
        return fitsData
    
    def drawFits(self, dataArray, dvmin = 0, dvmax = 255, dcmap = "Greys_r"):

        self.chartDev.ax.clear()
        self.chartDev.ax.imshow(dataArray, vmin = dvmin, vmax = dvmax, cmap = dcmap)
        return ""
    
    def axisLabel(self):
        
        font = {'family' : 'serif',
                'color'  : 'darkred',
                'weight' : 'normal',
                'size'   : 12,
                }
        
        self.chartDev.set_title('Phase - Diff. Mag.', fontdict=font)
        self.chartDev.set_xlabel("Phase", fontdict=font)
        self.chartDev.set_ylabel("Diff. Mag.", fontdict=font)
        self.chartDev.grid()