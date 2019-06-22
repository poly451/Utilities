import tkinter as tk
import time, sys
import schedule
import os

keep_running = False

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        print("dkdkd")
        self.root.after(15, self.update_clock)

# app=App()
def job():
    global keep_running
    print("I'm working! :-)")
    user_input = input("> ")
    if user_input == "stop":
        schedule.clear()
        keep_running = False
        print("Clearing scheduled task ...")
    # print("Here's what you typed: {}".format(user_input))


def main(arg01):
    global keep_running
    if arg01 == "start":
        schedule.every(5).seconds.do(job)
        keep_running = True
        while keep_running:
            schedule.run_pending()
            time.sleep(1)
    elif arg01 == "stop":
        schedule.cancel_job(job)

if __name__ == "__main__":
    arg01 = ""
    if len(sys.argv) == 1:
        program_name = os.path.basename(__file__)
        s = """
        ---------- {} ----------
        
        Hi! This is my first take at writing a program to 
        schedule a task. And it requires arguments. For example:
        
        > {} start
        > {} stop
        ---------------------------------------
        """.format(program_name, program_name, program_name)
        print(s)
        sys.exit()
    possible_arguments = ["start", "stop"]
    arg01 = sys.argv[1]
    if not arg01 in possible_arguments:
        s = "Sorry, I don't recognize that input. Here are the arguments\n"
        s += "I recognize:\n"
        s += " ".join(possible_arguments)
        sys.exit()
    main(arg01)
