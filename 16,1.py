import tkinter as tk
from tkinter import ttk, messagebox
import requests


def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
        response = requests.get(url)
        data = response.json()

        if to_curr in data['rates']:
            rate = data['rates'][to_curr]
            result = amount * rate
            label_result.config(text=f"Результат: {amount} {from_curr} = {result:.2f} {to_curr}")
        else:
            label_result.config(text="Ошибка: валюта не найдена")
    except ValueError:
        label_result.config(text="Ошибка: введите число")
    except:
        label_result.config(text="Ошибка: проверьте интернет")


# Создаём окно
window = tk.Tk()
window.title("Конвертор валют")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

# Элементы интерфейса
tk.Label(window, text="Из валюты:", bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)
combo_from = ttk.Combobox(window, values=["USD", "EUR", "RUB", "GBP", "CNY", "JPY"])
combo_from.pack(pady=5)
combo_from.set("USD")

tk.Label(window, text="В валюту:", bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)
combo_to = ttk.Combobox(window, values=["RUB", "USD", "EUR", "GBP", "CNY", "JPY"])
combo_to.pack(pady=5)
combo_to.set("RUB")

tk.Label(window, text="Сумма:", bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)
entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

btn_convert = tk.Button(window, text="Конвертировать", command=convert, bg="#4CAF50", fg="white")
btn_convert.pack(pady=10)

label_result = tk.Label(window, text="Результат: ---", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_result.pack(pady=20)

window.mainloop()