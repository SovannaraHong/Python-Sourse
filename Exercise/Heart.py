import tkinter as tk
import math
import itertools
import random

root = tk.Tk()
root.title("I LOVE YOU ❤️")
root.geometry("700x700")
root.configure(bg="#1a1a1a")  # Dark background
root.resizable(False, False)

canvas = tk.Canvas(root, width=700, height=700, bg="#1a1a1a", highlightthickness=0)
canvas.pack()


center_x, center_y = 350, 350
scale = 15
message = "💖 I LOVE YOU 💖 "
index = 0

# Color gradients for glow
gradient_colors = ["#FF1A1A", "#FF4C4C", "#FF6B6B", "#FF8080", "#FF9999"]
color_cycle = itertools.cycle(gradient_colors)



def draw_heart():
    global index
    canvas.delete("all")
    color = next(color_cycle)


    pulse = 1 + 0.08 * math.sin(index * 0.15)
    canvas.create_text(center_x, center_y, text="❤️", font=("Helvetica", int(120 * pulse)), fill="#FF1A1A")


    t = 0
    t_step = 0.06
    while t < 2 * math.pi:
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        char = message[index % len(message)]


        for i, glow_color in enumerate(reversed(gradient_colors)):
            canvas.create_text(center_x + x * scale, center_y - y * scale, text=char,
                               font=("Helvetica", 18 + i * 2, "bold"), fill=glow_color)

        canvas.create_text(center_x + x * scale, center_y - y * scale, text=char, font=("Helvetica", 18, "bold"),
                           fill=color)
        t += t_step
        index += 1


    for i in range(15):
        angle = i * 2 * math.pi / 15 + index * 0.05
        radius = 50 + 150 * math.sin(index * 0.02 + i)
        x = center_x + radius * math.cos(angle)
        y = center_y - radius * math.sin(angle)
        canvas.create_text(x, y, text="💖", font=("Helvetica", 20), fill=gradient_colors[i % len(gradient_colors)])

    root.after(80, draw_heart)


draw_heart()
root.mainloop()
