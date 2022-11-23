from PyQt5 import QtCore, QtGui, QtWidgets
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkFiltersSources
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class ModelUi(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.resize(960, 720)
        self.frame = QtWidgets.QFrame()

        self.vl = QtWidgets.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)

        self.ren = vtkmodules.vtkRenderingCore.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtkmodules.vtkFiltersSources.vtkConeSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(0.1)

        source1 = vtkmodules.vtkFiltersSources.vtkConeSource()
        source1.SetCenter(0, 0, 0)
        source1.SetRadius(0.5)

        # Create a mapper
        mapper = vtkmodules.vtkRenderingCore.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        mapper1 = vtkmodules.vtkRenderingCore.vtkPolyDataMapper()
        mapper1.SetInputConnection(source1.GetOutputPort())

        # Create an actor
        actor = vtkmodules.vtkRenderingCore.vtkActor()
        actor.SetMapper(mapper)

        actor1 = vtkmodules.vtkRenderingCore.vtkActor()
        actor1.SetMapper(mapper1)

        self.ren.AddActor(actor)
        self.ren.AddActor(actor1)

        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()
