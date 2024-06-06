from ui.logic_ui import LogicUI
from PySide6 import QtWidgets
import sys


class Main:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QDialog()
        self.logic_ui = LogicUI(self.dialog)
        self.dialog.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    Main()
