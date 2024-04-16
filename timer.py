import customtkinter as ct
import time

class CountdownTimer:
    def __init__(self, window, store_time=30):
        self.window = window
        self.store_time = store_time  # Initial countdown duration
        self.start_time = None
        self.running = False

        self.timer_label = ct.CTkLabel(
            master=self.window, text=f"{self.store_time} seconds remaining"
        )
        self.timer_label.pack(pady=20)

        self.start_button = ct.CTkButton(
            master=self.window, text="Start Timer", command=self.start_timer
        )
        self.start_button.pack()

        self.stop_button = ct.CTkButton(
            master=self.window, text="Stop Timer", command=self.stop_timer, state="disabled"
        )
        self.stop_button.pack()

    def start_timer(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            self.update_timer()

    def update_timer(self):
        if self.running:
            present_time = time.time()
            elapsed_time = present_time - self.start_time
            remaining_time = self.store_time - int(elapsed_time)

            if remaining_time > 0:
                self.timer_label.configure(text=f"{remaining_time} seconds remaining")
                self.window.after(1000, self.update_timer)  # Update every 1 second
            else:
                self.stop_timer()
                self.timer_label.configure(text="Timer Finished!")

    def stop_timer(self):
        if self.running:
            self.running = False
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")


# Create the main window and start the timer application
window = ct.CTk()
window.geometry("300x150")
window.title("CustomTkinter Countdown Timer")

countdown_timer = CountdownTimer(window)

window.mainloop()
