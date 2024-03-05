import tkinter as tk

class ConeCreator:
    def __init__(self, roogt):
        self.root = root
        self.root.title("Cone Creator")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.color = "orange"
        self.mode = "add"

        self.cones = []

        self.create_widgets()

    def create_widgets(self):
        self.color_var = tk.StringVar(value="orange")
        self.mode_var = tk.StringVar(value="add")

        color_frame = tk.Frame(self.root)
        color_frame.pack(side=tk.TOP, padx=10, pady=10)

        color_label = tk.Label(color_frame, text="Color:")
        color_label.grid(row=0, column=0, padx=5, pady=5)

        color_options = ["orange", "blue", "yellow"]
        for i, color in enumerate(color_options):
            tk.Radiobutton(color_frame, text=color, variable=self.color_var, value=color, command=self.update_color).grid(row=0, column=i+1, padx=5, pady=5)

        mode_frame = tk.Frame(self.root)
        mode_frame.pack(side=tk.TOP, padx=10, pady=10)

        mode_label = tk.Label(mode_frame, text="Mode:")
        mode_label.grid(row=0, column=0, padx=5, pady=5)

        mode_options = [("Add", "add"), ("Erase", "erase")]
        for i, (text, mode) in enumerate(mode_options):
            tk.Radiobutton(mode_frame, text=text, variable=self.mode_var, value=mode, command=self.update_mode).grid(row=0, column=i+1, padx=5, pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit)#function
        submit_button.pack(side=tk.BOTTOM, padx=10, pady=10) #display

        self.canvas.bind("<Button-1>", self.place_cone)

    def update_color(self):
        self.color = self.color_var.get()

    def update_mode(self):
        self.mode = self.mode_var.get()

    def place_cone(self, event):
        x, y = event.x, event.y
        if self.mode == "add":
            cone = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=self.color, outline="")
            self.cones.append(cone)
        elif self.mode == "erase":
            items = self.canvas.find_overlapping(x-10, y-10, x+10, y+10)
            for item in items:
                if item in self.cones:
                    self.canvas.delete(item)
                    self.cones.remove(item)

    def submit(self):
        print("Submitted cones:", self.cones)


if __name__ == "__main__":
    root = tk.Tk() 
    app = ConeCreator(root)
    root.mainloop()
