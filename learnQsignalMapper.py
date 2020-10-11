from PyQt5 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self._mapper = QtCore.QSignalMapper()
        self._mapper.mapped[str].connect(self.onClicked)
        vlay = QtWidgets.QVBoxLayout(self)
        checkbox = QtWidgets.QCheckBox("Block Signals")
        checkbox.stateChanged.connect(self.onStateChanged)
        vlay.addWidget(checkbox)
        for i in range(5):
            button = QtWidgets.QPushButton("{}".format(i))
            button.clicked.connect(self._mapper.map)
            self._mapper.setMapping(button, "button-{}".format(i))
            vlay.addWidget(button)


    @QtCore.pyqtSlot(int)
    def onStateChanged(self, state):
        self._mapper.blockSignals(state == QtCore.Qt.Checked)

    @QtCore.pyqtSlot(str)
    def onClicked(self, text):
        print(text)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
