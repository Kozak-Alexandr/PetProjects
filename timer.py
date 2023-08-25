import datetime
import tkinter as tk


class CountdownTimer:
    def __init__(self, target_date):
        self.target_date = target_date
        self.running = False

        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.label_days = tk.Label(self.root, text="")
        self.label_days.pack()
        self.label_hours = tk.Label(self.root, text="")
        self.label_hours.pack()
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

    def update_label(self):
        now = datetime.datetime.now()
        time_left = self.target_date - now
        days_left = time_left.days
        hours_left = time_left.days * 24 + time_left.seconds // 3600
        days_string = "Осталось {} дней".format(days_left)
        hours_string = "Осталось {:02d} часов".format(hours_left)
        self.label_days.config(text=days_string)
        self.label_hours.config(text=hours_string)

    def start(self):
        self.running = True
        self.update_label()
        if datetime.datetime.now() < self.target_date and self.running:
            self.root.after(1000, self.start)
        else:
            self.running = False

    def stop(self):
        self.running = False

target_date = datetime.datetime(2023, 8, 31, 10, 00, 00)
timer = CountdownTimer(target_date)
timer.start()
timer.root.mainloop()