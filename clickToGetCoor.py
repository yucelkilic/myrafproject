  QMainWindow.__init__(self)
    self.setWindowTitle('Select Window')
    self.local_image = QImage("Burası yol")

    self.local_grview = QGraphicsView()
    self.setCentralWidget( self.local_grview )

    self.local_scene = QGraphicsScene()

    self.image_format = self.local_image.format()
    self.pixMapItem = self.local_scene.addPixmap( QPixmap(self.local_image) )
    self.local_grview.setScene( self.local_scene )




    self.pixMapItem.mousePressEvent = self.pixelSelect

    self.show()
    sys.exit(app.exec_())

def pixelSelect( self, event ):
    print 'hello'
    position = QPoint( event.pos().x(),  event.pos().y())
    color = QColor.fromRgb(self.local_image.pixel( position ) )
    if color.isValid():
        rgbColor = '('+str(color.red())+','+str(color.green())+','+str(color.blue())+','+str(color.alpha())+')'
        self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - Value (R,G,B,A)= ' + rgbColor)
    else:
        self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - color not valid')    
