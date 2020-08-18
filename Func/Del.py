from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Удалить")

        self.setWindowTitle("Удалить все")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.setWindowIcon(QIcon("Images\Удалить.png"))
        self.QBtn.clicked.connect(self.deleteAllWorks)
        layout = QVBoxLayout()
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deleteAllWorks(self):
        try:
            self.conn = sqlite3.connect("Result.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from Result")
            self.c.execute("DELETE from Skills")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            self.close()
        except Exception:
<<<<<<< HEAD
            QMessageBox.warning(QMessageBox(), 'Error', 'Не удалось удалить вакансии')
=======
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete from the database.')
>>>>>>> parent of 86358a0... Update Del.py
