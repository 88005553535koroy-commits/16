import tkinter as tk
from tkinter import messagebox


class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мои заметки")
        self.root.geometry("500x450")
        self.root.configure(bg="#f9f9f9")

        self.notes = []  # список заметок

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.root, text="Заголовок:", bg="#f9f9f9", font=("Arial", 10)).pack(pady=(10, 0))

        self.title_input = tk.Entry(self.root, width=50)
        self.title_input.pack(pady=5)

        # Текст заметки
        tk.Label(self.root, text="Заметка:", bg="#f9f9f9", font=("Arial", 10)).pack(pady=(10, 0))

        self.note_input = tk.Text(self.root, width=50, height=5)
        self.note_input.pack(pady=5)

        # Кнопки
        btn_frame = tk.Frame(self.root, bg="#f9f9f9")
        btn_frame.pack(pady=10)

        btn_add = tk.Button(btn_frame, text="Добавить заметку", command=self.add_note, bg="#4CAF50", fg="white")
        btn_add.pack(side=tk.LEFT, padx=5)

        btn_delete = tk.Button(btn_frame, text="Удалить выбранное", command=self.delete_note, bg="#f44336", fg="white")
        btn_delete.pack(side=tk.LEFT, padx=5)

        # Список заметок
        tk.Label(self.root, text="Список заметок:", bg="#f9f9f9", font=("Arial", 10)).pack()

        self.listbox = tk.Listbox(self.root, width=60, height=6)
        self.listbox.pack(pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.show_note)  # при клике показываем заметку

        # Просмотр выбранной заметки
        tk.Label(self.root, text="Просмотр:", bg="#f9f9f9", font=("Arial", 10)).pack()

        self.view_text = tk.Text(self.root, width=50, height=4, state="disabled")
        self.view_text.pack(pady=5)

    def add_note(self):
        title = self.title_input.get().strip()
        content = self.note_input.get("1.0", tk.END).strip()

        if title and content:
            note = {"title": title, "content": content}
            self.notes.append(note)
            self.listbox.insert(tk.END, title)
            self.title_input.delete(0, tk.END)
            self.note_input.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Ошибка", "Заполните заголовок и заметку!")

    def delete_note(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.notes.pop(index)
            self.listbox.delete(index)
            self.view_text.config(state="normal")
            self.view_text.delete("1.0", tk.END)
            self.view_text.config(state="disabled")
        else:
            messagebox.showwarning("Ошибка", "Выберите заметку для удаления!")

    def show_note(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            note = self.notes[index]

            self.view_text.config(state="normal")
            self.view_text.delete("1.0", tk.END)
            self.view_text.insert("1.0", f"*** {note['title']} ***\n\n{note['content']}")
            self.view_text.config(state="disabled")


# Запуск
if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()