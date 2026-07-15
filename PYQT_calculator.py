import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)
        self.create_widgets()

    def create_widgets(self):
        self.display = QLineEdit()
        self.display.setReadOnly(False)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ]

        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 10px;")

            if text == "C":
                button.clicked.connect(self.clear_display)
            else:
                button.clicked.connect(lambda checked, t=text: self.button_click(t))

            grid.addWidget(button, row, col)

        equals_button = QPushButton("=")
        equals_button.setStyleSheet(
            "font-size: 18px; padding: 10px; background-color: lightblue;"
        )
        equals_button.clicked.connect(self.calculate_result)
        grid.addWidget(equals_button, 5, 0, 1, 4)

        main_layout = QVBoxLayout()
        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def button_click(self, value):
        current_text = self.display.text()
        self.display.setText(current_text + str(value))

    def clear_display(self):
        self.display.clear()

    def calculate_result(self):
        expression = self.display.text()

        try:
            result = eval(expression)
            self.display.setText(str(result))

        except ZeroDivisionError:
            self.display.setText("Error: Div by 0")

        except Exception:
            self.display.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())