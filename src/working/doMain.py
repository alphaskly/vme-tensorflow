import src.working.loginForm
import sys

from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = src.working.loginForm.Ui_Form()
    window.show()
    sys.exit(app.exec_())