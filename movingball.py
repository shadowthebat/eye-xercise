from tkinter import * # imports all from tkinter
import random # imports random
import time

tk = Tk() # creates tkinter object ??
canvas = Canvas(tk, width=1400, height=800) # sizes window ??
tk.title('Drawing') # title the window
canvas.pack() #

class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(10,10,40,40,fill='black')
        self.xspeed = 20

    def move(self):
        canvas.move(self.shape, self.xspeed, 0)
        pos = canvas.coords(self.shape)
        if pos[2] >= 1400 or pos[0] <= 0:
            canvas.move(self.shape, -1350, 30)
            time.sleep(0.15)
        elif pos[3] >= 750:
            canvas.move(self.shape, 0, -650)
            time.sleep(0.15)

ball = Ball()

while True:
    ball.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
