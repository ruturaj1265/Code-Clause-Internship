import tkinter as tk
import time
import winsound

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alarm Clock")
        self.geometry("300x200")
        self.alarm_time = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Label to display current time
        self.time_label = tk.Label(self, text="", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        # Entry widget for setting the alarm time
        self.alarm_entry = tk.Entry(self, textvariable=self.alarm_time, font=("Helvetica", 16))
        self.alarm_entry.pack(pady=10)

        # Button to set the alarm
        self.set_alarm_btn = tk.Button(self, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_btn.pack(pady=10)

        # Button to stop the alarm
        self.stop_alarm_btn = tk.Button(self, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_alarm_btn.pack(pady=10)

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.after(1000, self.update_time)

        # Check if the alarm time has been reached
        if current_time == self.alarm_time.get():
            self.alarm()

    def set_alarm(self):
        alarm_time = self.alarm_time.get()
        if alarm_time:
            self.stop_alarm_btn.config(state=tk.NORMAL)
            self.set_alarm_btn.config(state=tk.DISABLED)
            self.alarm_entry.config(state=tk.DISABLED)

    def stop_alarm(self):
        self.stop_alarm_btn.config(state=tk.DISABLED)
        self.set_alarm_btn.config(state=tk.NORMAL)
        self.alarm_entry.config(state=tk.NORMAL)

    def alarm(self):
        # Play the alarm sound
        for _ in range(3):
            winsound.Beep(2000, 2000)  # Beep at 2000Hz for 1 second
            time.sleep(1)
        self.stop_alarm()

if __name__ == "__main__":
    app = AlarmClock()
    app.update_time()
    app.mainloop()


