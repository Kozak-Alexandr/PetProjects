

import datetime
import tkinter as tk

# создаем окно
window = tk.Tk()

# выбранная дата
target_date = datetime.datetime(2023, 8, 31, 10, 00, 00)

# текущая дата и время
now = datetime.datetime.now()

# вычисляем разницу во времени
time_left = target_date - now

# создаем метку для вывода оставшегося количества часов
label = tk.Label(window, text="Осталось " + str(time_left.days) + " Д " + "и " + str(time_left.days * 24 + time_left.seconds // 3600) + " Ч")
#label = tk.Label(window, text="Осталось " + str(time_left.days * 24 + time_left.seconds // 3600) + " часов")
label.pack()

# запускаем главный цикл окна
window.mainloop()