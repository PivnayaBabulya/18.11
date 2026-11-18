from tkinter import *

clicks = 0

def click_button():
    global clicks
    clicks += 1
    btn["text"] = f"Clicks {clicks}"

# Установка цвета кнопки
def change():
    b1['text'] ="Добавлено"
    b1['bg'] = '#ffffff'
    b1['fg'] = '#096B00'
    b1['activebackgroung'] = '#024100'
    b1['activeforegroung'] = '#ffffff' 

# Установка заголовка окна, его размеров и иконки
# Здесь не появляется установленная иконка
root = Tk()
root.title("Планировщик задач")
root.iconbitmap(default="images/image1.png")
root.geometry("460x520")
b1 = Button(text="Добавить задачу")
b1.pack()

# Создаём текст внутри кнопки
btn = Button(text="Добавить задачу")
btn.pack()

# Сщздаём лейбл для вывода текстового сообщения
label = Label(text="")
label.pack()

# Вызываем созданного окна
root.mainloop()
