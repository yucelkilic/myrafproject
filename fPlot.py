#!/usr/bin/env python
import os
import pyfits
import numpy as np

class FitsPlot:
    
    def __init__(self, filepath, chartDev, objDev):
        
        self.objDev = objDev
        self.filepath = filepath
        self.chartDev = chartDev
        self.image,self.head = pyfits.getdata(self.filepath,header=True)
    
    def dataFits(self):
        
        f = pyfits.open(self.filepath)
        fitsData = f[0].data
        return fitsData
    
    def drawFits(self, dataArray, dvmin = 0, dvmax = 255, dcmap = "Greys_r"):

        self.chartDev.ax.cla()
        self.chartDev.ax.imshow(dataArray, vmin = dvmin, vmax = dvmax, cmap = dcmap)
        return ""

    def drawim(self, slider):
        '''
        This fucntion actually handles the drawing of the imshow mpl canvas. It pulls the required elements from the ui on each redraw
        '''        
        self.chartDev.ax.cla()
        #This next line sets the maximum value in the image according to what vale the slider bar is at, basicaly its the maximum value times
        #the ratio of of the silder position over 100 added to the minimum value
        self.imageedit = self.image.copy()
        self.imageedit[np.where(self.imageedit <=0)]=0.001
        self.imageedit = np.log(self.imageedit)
        if slider == "horizontalSlider":
            self.mx = ((self.imageedit.max()-self.imageedit.min())*self.objDev.horizontalSlider.value()/100. + self.imageedit.min())*1
        elif slider == "horizontalSlider_2":
            self.mx = ((self.imageedit.max()-self.imageedit.min())*self.objDev.horizontalSlider_2.value()/100. + self.imageedit.min())*1
        elif slider == "horizontalSlider_3":
            self.mx = ((self.imageedit.max()-self.imageedit.min())*self.objDev.horizontalSlider_3.value()/100. + self.imageedit.min())*1
        #updated the canvas and draw
        self.imdata = self.chartDev.ax.imshow(self.imageedit,vmax=float(self.mx),vmin=self.imageedit.min(),cmap="Greys_r", interpolation=None,alpha=1)
        self.chartDev.draw()