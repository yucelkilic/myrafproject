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
    
    def drawim(self, slider):
        '''
        This fucntion actually handles the drawing of the imshow mpl canvas. It pulls the required elements from the ui on each redraw
        '''        
        self.chartDev.ax.cla()
        cur_xlim = self.chartDev.ax.get_xlim()
        cur_ylim = self.chartDev.ax.get_ylim()
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
        elif slider == "horizontalSlider_4":
            self.mx = ((self.imageedit.max()-self.imageedit.min())*self.objDev.horizontalSlider_4.value()/100. + self.imageedit.min())*1
            #updated the canvas and draw
        self.imdata = self.chartDev.ax.imshow(self.imageedit,vmax=float(self.mx),vmin=self.imageedit.min(),cmap="Greys_r", interpolation=None,alpha=1)
        if cur_xlim[1] != 1 and cur_ylim[1] != 1:
            self.chartDev.ax.set_xlim([int(cur_xlim[0]), int(cur_xlim[1])])
            self.chartDev.ax.set_ylim([int(cur_ylim[0]), int(cur_ylim[1])])
        self.chartDev.draw()
        return True
