import tkinter as tk

# Создаём окно
root = tk.Tk()
root.title("Авторизация")      # заголовок окна — из ТЗ
root.geometry("300x150")       # размер окна — из ТЗ
root.resizable(False, False)   # фиксируем размер, чтобы макет не «поплыл»

# Метка «Вход в систему» — заголовок формы
title_label = tk.Label(root, text="Вход в систему",
                       font=("Arial", 7, "bold"))
title_label.pack(pady=(10, 5))

# Поле для логина
login_label = tk.Label(root, text="Логин:")
login_label.pack()
login_entry = tk.Entry(root, width=20)
login_entry.pack(pady=2)

# Поле для пароля — символы скрыты звёздочками
password_label = tk.Label(root, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(root, width=20, show="*")
password_entry.pack(pady=2)

# Кнопка «Войти»
login_button = tk.Button(root, text="Войти", width=10)
login_button.pack(pady=8)

# Запускаем главный цикл окна
root.mainloop()
