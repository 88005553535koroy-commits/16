import sys
import requests
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Конвертер валют")
        self.setFixedSize(500, 500)

        central = QWidget()
        central.setStyleSheet("background-color: #22222e;")
        self.setCentralWidget(central)

        frame = QFrame(central)
        frame.setStyleSheet("background-color: #fb5b5d; border-radius: 20px;")
        frame.setGeometry(20, 20, 460, 270)

        title = QLabel("Конвертер валют", frame)
        title.setStyleSheet("color: white; font: 24px 'Impact';")
        title.setAlignment(Qt.AlignCenter)
        title.setGeometry(0, 20, 460, 50)

        self.input_cur = QLineEdit(frame)
        self.input_cur.setPlaceholderText("Из валюты (USD, EUR, RUB...)")
        self.input_cur.setStyleSheet("background-color: white; font: 16px; border-radius: 10px; padding: 10px; color: black;")
        self.input_cur.setGeometry(40, 90, 380, 45)

        self.input_sum = QLineEdit(frame)
        self.input_sum.setPlaceholderText("Сумма")
        self.input_sum.setStyleSheet("background-color: white; font: 16px; border-radius: 10px; padding: 10px; color: black;")
        self.input_sum.setGeometry(40, 145, 380, 45)

        self.output_cur = QLineEdit(frame)
        self.output_cur.setPlaceholderText("В валюту (USD, EUR, RUB...)")
        self.output_cur.setStyleSheet("background-color: white; font: 16px; border-radius: 10px; padding: 10px; color: black;")
        self.output_cur.setGeometry(40, 200, 380, 45)

        self.btn_convert = QPushButton("Конвертировать", central)
        self.btn_convert.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d; 
                border-radius: 30px; 
                color: white; 
                font: 18px 'Impact';
            }
            QPushButton:pressed {
                background-color: #fa4244;
            }
        """)
        self.btn_convert.setGeometry(60, 310, 380, 55)
        self.btn_convert.clicked.connect(self.convert)

        self.output_sum = QLineEdit(central)
        self.output_sum.setPlaceholderText("Результат")
        self.output_sum.setReadOnly(True)
        self.output_sum.setStyleSheet("background-color: #e0e0e0; font: 18px; border-radius: 15px; padding: 10px; color: #333; color: black;")
        self.output_sum.setGeometry(60, 390, 380, 55)

        self.status_label = QLabel("", central)
        self.status_label.setStyleSheet("color: #ff9999; font: 12px;")
        self.status_label.setGeometry(60, 455, 380, 30)

    def convert(self):
        from_cur = self.input_cur.text().strip().upper()
        to_cur = self.output_cur.text().strip().upper()
        amount_text = self.input_sum.text().strip()

        if not from_cur or not to_cur or not amount_text:
            self.status_label.setText("Ошибка: заполните все поля!")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.status_label.setText("Ошибка: сумма должна быть числом!")
            return

        url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"

        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            if to_cur in data['rates']:
                rate = data['rates'][to_cur]
                result = amount * rate
                self.output_sum.setText(f"{result:.2f} {to_cur}")
                self.status_label.setText(f"Курс: 1 {from_cur} = {rate:.4f} {to_cur}")
            else:
                self.status_label.setText(f"Ошибка: валюта '{to_cur}' не найдена!")
        except:
            self.status_label.setText("Ошибка: проверьте интернет!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec_())