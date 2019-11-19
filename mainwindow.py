import sys
from PyQt5 import QtGui, QtWidgets, QtCore
import RiverManager
# import qdarkstyle
# import images_qr
from AdcpTerminal_pyqt5.terminal_vm import TerminalVM
from rti_python.Utilities.config import RtiConfig


class MainWindow(QtWidgets.QMainWindow):
    """
    Main window for the application
    """

    def __init__(self, config=None):
        QtWidgets.QMainWindow.__init__(self)

        self.rti_config = RtiConfig()
        self.rti_config.init_terminal_config()
        self.rti_config.init_plot_server_config()

        # Initialize the pages
        self.mgr = RiverManager.RiverManager(self, self.rti_config)

        # Initialize the window
        self.main_window_init()

    def main_window_init(self):
        # Set the title of the window
        self.setWindowTitle("Rowe Technologies, Inc. - RiveR")

        self.setWindowIcon(QtGui.QIcon(":rti.ico"))

        # Initialize Terminal
        self.Terminal = TerminalVM(self, self.rti_config)
        docked_terminal = QtWidgets.QDockWidget("Terminal", self)
        docked_terminal.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        docked_terminal.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        docked_terminal.setWidget(self.Terminal)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, docked_terminal)

        # Show the main window
        self.show()

    def closeEvent(self, event):
        """
        Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Close, Cancel buttons
        """
        reply = QtWidgets.QMessageBox.question(self, "Message",
            "Are you sure you want to quit?", QtWidgets.QMessageBox.Close | QtWidgets.QMessageBox.Cancel)

        if reply == QtWidgets.QMessageBox.Close:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Mac")

    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow()
    sys.exit(app.exec_())
