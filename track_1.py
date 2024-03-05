import tkinter as tk

class Cone:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class ConeDrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cone Drawing App")

        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()

        self.color_var = tk.StringVar()
        self.color_var.set("orange")

        self.mode_var = tk.StringVar()
        self.mode_var.set("add")

        self.submit_btn = tk.Button(master, text="Submit Cones", command=self.submit_cones)
        self.submit_btn.pack()

        self.canvas.bind("<Button-1>", self.place_cone)

    def place_cone(self, event):
        if self.mode_var.get() == "erase":
            self.erase_cone(event)
        else:
            color = self.color_var.get()
            x, y = event.x, event.y
            cone = Cone(x, y, color)
            self.draw_cone(cone)

    def erase_cone(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if item:
            self.canvas.delete(item)

    def draw_cone(self, cone):
        color = cone.color
        x, y = cone.x, cone.y
        if color == "orange":
            self.canvas.create_polygon(x, y, x-10, y+20, x+10, y+20, fill=color)
        elif color == "blue":
            self.canvas.create_polygon(x, y, x-10, y+20, x+10, y+20, fill=color)
        elif color == "yellow":
            self.canvas.create_polygon(x, y, x-10, y+20, x+10, y+20, fill=color)

        # Display cone coordinates
        self.canvas.create_text(x, y+25, text=f"({x}, {y})")

    def submit_cones(self):
        cones = []
        for item in self.canvas.find_all():
            coords = self.canvas.coords(item)
            color = self.canvas.itemcget(item, "fill")
            x = int((coords[0] + coords[4]) / 2)
            y = int((coords[1] + coords[5]) / 2)
            cones.append(Cone(x, y, color))
        for cone in cones:
            relative_x = cone.x - cones[0].x
            relative_y = cone.y - cones[0].y
            print(f"Color: {cone.color}, Relative Coordinates: ({relative_x}, {relative_y})")

root = tk.Tk()
app = ConeDrawingApp(root)
root.mainloop()
