import tkinter as tk

class TrackCreator:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Track Creator")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
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

        color_options = ["orange", "yellow", "blue"]
        for i, color in enumerate(color_options):
            tk.Radiobutton(color_frame, text=color, variable=self.color_var, value=color, command=self.update_color).grid(row=0, column=i+1, padx=5, pady=5)

        mode_frame = tk.Frame(self.root)
        mode_frame.pack(side=tk.TOP, padx=10, pady=10)

        mode_label = tk.Label(mode_frame, text="Mode:")
        mode_label.grid(row=0, column=0, padx=5, pady=5)

        mode_options = [("Add", "add"), ("Erase", "erase")]
        for i, (text, mode) in enumerate(mode_options):
            tk.Radiobutton(mode_frame, text=text, variable=self.mode_var, value=mode, command=self.update_mode).grid(row=0, column=i+1, padx=5, pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.canvas.bind("<Button-1>", self.place_cone) #Bind the mouse click event to the canvas

    def update_color(self):
        self.color = self.color_var.get()

    def update_mode(self):
        self.mode = self.mode_var.get()

    
    def place_cone(self, event):
        x, y = event.x, event.y
        if self.mode == "add":
            cone = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=self.color, outline="", tags=self.color)
            self.cones.append((cone, x, y, self.color))  # Store cone ID, x, y, and color
        elif self.mode == "erase":
            items = self.canvas.find_overlapping(x-10, y-10, x+10, y+10)
            for item in items:
                if self.canvas.gettags(item)[0] in ["orange", "yellow", "blue"]:
                    self.canvas.delete(item)
                    self.cones = [cone for cone in self.cones if cone[0] != item]


    def submit(self):
        orange_cone = None
        for cone_id, x, y, color in self.cones:
            if color == "orange":
                orange_cone = (x, y)
                break

        if orange_cone:
            orange_x, orange_y = orange_cone
            print("Blue cones:")
            for cone_id, x, y, color in self.cones:
                x_meters = (x - orange_x) / 10  # Assuming 10 pixels = 1 meter
                y_meters = (y - orange_y) / 10
                if color == "blue":
                    print("- -", y_meters)
                    print("-", x_meters)

            print("\nOrange cones:")
            print("- - 0")  # Orange cone is at (0,0)
            print("-", 0)

            print("\nYellow cones:")
            for cone_id, x, y, color in self.cones:
                x_meters = (x - orange_x) / 10
                y_meters = (y - orange_y) / 10
                if color == "yellow":
                    print("- -", y_meters)
                    print("-", x_meters)
        else:
            print("No orange cone found.")



if __name__ == "__main__":
    root = tk.Tk()
    app = TrackCreator(root)
    root.mainloop()
