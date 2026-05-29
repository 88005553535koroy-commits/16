import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notes = []  # список заметок
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Мои заметки")
        self.setFixedSize(550, 500)

        # Центральный виджет
        central = QWidget()
        central.setStyleSheet("background-color: #f5f5f5;")
        self.setCentralWidget(central)

        # Главный вертикальный layout
        main_layout = QVBoxLayout(central)

        # Заголовок
        title = QLabel("📝 Мои заметки")
        title.setStyleSheet("font: 24px 'Impact'; color: #333;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Поле для заголовка
        main_layout.addWidget(QLabel("Заголовок:"))
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Введите заголовок...")
        self.title_input.setStyleSheet("padding: 8px; font: 14px; border: 1px solid #ccc; border-radius: 5px; color: black;")
        main_layout.addWidget(self.title_input)

        # Поле для текста заметки
        main_layout.addWidget(QLabel("Заметка:"))
        self.note_input = QTextEdit()
        self.note_input.setPlaceholderText("Введите текст заметки...")
        self.note_input.setStyleSheet("padding: 8px; font: 14px; border: 1px solid #ccc; border-radius: 5px; color: black;")
        self.note_input.setMaximumHeight(150)
        main_layout.addWidget(self.note_input)

        # Кнопки (горизонтально)
        btn_layout = QHBoxLayout()

        self.btn_add = QPushButton("➕ Добавить заметку")
        self.btn_add.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px; border-radius: 5px; color: black;")
        self.btn_add.clicked.connect(self.add_note)
        btn_layout.addWidget(self.btn_add)

        self.btn_delete = QPushButton("🗑 Удалить выбранное")
        self.btn_delete.setStyleSheet("background-color: #f44336; color: white; padding: 8px; border-radius: 5px; color: black;")
        self.btn_delete.clicked.connect(self.delete_note)
        btn_layout.addWidget(self.btn_delete)

        main_layout.addLayout(btn_layout)

        # Список заметок
        main_layout.addWidget(QLabel("Список заметок:"))
        self.list_notes = QListWidget()
        self.list_notes.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; color: black;")
        self.list_notes.itemClicked.connect(self.show_note)
        main_layout.addWidget(self.list_notes)

        # Просмотр выбранной заметки
        main_layout.addWidget(QLabel("Просмотр:"))
        self.view_text = QTextEdit()
        self.view_text.setReadOnly(True)
        self.view_text.setStyleSheet(
            "background-color: #fff; border: 1px solid #ccc; border-radius: 5px; padding: 8px; color: black;")
        self.view_text.setMaximumHeight(120)
        main_layout.addWidget(self.view_text)

    def add_note(self):
        title = self.title_input.text().strip()
        content = self.note_input.toPlainText().strip()

        if title and content:
            note = {"title": title, "content": content}
            self.notes.append(note)
            self.list_notes.addItem(title)
            self.title_input.clear()
            self.note_input.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Заполните заголовок и заметку!")

    def delete_note(self):
        current_row = self.list_notes.currentRow()
        if current_row >= 0:
            self.notes.pop(current_row)
            self.list_notes.takeItem(current_row)
            self.view_text.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите заметку для удаления!")

    def show_note(self, item):
        for note in self.notes:
            if note["title"] == item.text():
                self.view_text.setText(f"*** {note['title']} ***\n\n{note['content']}")
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec_())