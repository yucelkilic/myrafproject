from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):

    def __init__(self):
        font = {'family' : 'serif',
            'color'  : 'darkred',
            'weight' : 'normal',
            'size'   : 12,
            }
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Phase - Diff. Mag.', fontdict=font)
        self.ax.set_xlabel("Phase", fontdict=font)
        self.ax.set_ylabel("Diff. Mag.", fontdict=font)
        self.ax.grid()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class matplotlibWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.show()
