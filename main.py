import tkinter as tk
from tkinter import colorchooser, messagebox
from PIL import Image, ImageTk
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Whiteboard with Matplotlib")

        self.color = "black"
        self.brush_size = 3
        self.shape = "freehand"
        self.old_x = None
        self.old_y = None

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Tool Frame
        tools = tk.Frame(self.root)
        tools.pack(fill=tk.X)

        tk.Button(tools, text="Color", command=self.choose_color).pack(side=tk.LEFT)
        tk.Label(tools, text="Size:").pack(side=tk.LEFT)
        self.size_scale = tk.Scale(tools, from_=1, to=10, orient=tk.HORIZONTAL, command=self.set_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT)

        tk.Label(tools, text="Shape:").pack(side=tk.LEFT)
        self.shape_var = tk.StringVar(value="freehand")
        shapes = ["freehand", "line", "rectangle", "oval"]
        for s in shapes:
            tk.Radiobutton(tools, text=s.capitalize(), variable=self.shape_var, value=s).pack(side=tk.LEFT)

        # Eraser button
        self.eraser_button = tk.Button(tools, text="Eraser", command=self.activate_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        tk.Button(tools, text="Clear", command=self.clear_canvas).pack(side=tk.RIGHT)
        tk.Button(tools, text="Code Box", command=self.open_code_box).pack(side=tk.RIGHT)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # To keep reference of images added to canvas
        self.canvas_images = []

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def set_size(self, val):
        self.brush_size = int(val)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.canvas_images.clear()

    def activate_eraser(self):
        self.color = "white"  # Change color to white for eraser functionality

    def start_draw(self, event):
        self.old_x, self.old_y = event.x, event.y
        if self.shape_var.get() != "freehand":
            self.start_x, self.start_y = event.x, event.y

    def draw(self, event):
        shape = self.shape_var.get()
        if shape == "freehand":
            if self.old_x and self.old_y:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                        width=self.brush_size, fill=self.color,
                                        capstyle=tk.ROUND, smooth=True)
            self.old_x, self.old_y = event.x, event.y

    def reset(self, event):
        shape = self.shape_var.get()
        if shape != "freehand":
            end_x, end_y = event.x, event.y
            if shape == "line":
                self.canvas.create_line(self.start_x, self.start_y, end_x, end_y,
                                        width=self.brush_size, fill=self.color)
            elif shape == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y,
                                             outline=self.color, width=self.brush_size)
            elif shape == "oval":
                self.canvas.create_oval(self.start_x, self.start_y, end_x, end_y,
                                        outline=self.color, width=self.brush_size)
        self.old_x, self.old_y = None, None

    def open_code_box(self):
        code_window = tk.Toplevel(self.root)
        code_window.title("Matplotlib Code Box")
        code_window.geometry("600x400")

        code_editor = tk.Text(code_window, font=("Courier", 10))
        code_editor.pack(fill=tk.BOTH, expand=True)

        def run_code():
            user_code = code_editor.get("1.0", tk.END)
            try:
                local_ns = {}
                exec(user_code, {"plt": plt}, local_ns)

                # Render the current figure to an image
                fig = plt.gcf()
                canvas = FigureCanvasAgg(fig)
                buf = io.BytesIO()
                canvas.draw()
                fig.savefig(buf, format='png', dpi=100)
                buf.seek(0)

                image = Image.open(buf)
                tk_image = ImageTk.PhotoImage(image)

                # Keep a reference so it's not garbage collected
                self.canvas_images.append(tk_image)

                # Add to canvas
                self.canvas.create_image(100, 100, anchor=tk.NW, image=tk_image)
                plt.close(fig)

            except Exception as e:
                messagebox.showerror("Error", f"Code execution failed:\n{e}")

        tk.Button(code_window, text="Run Code", command=run_code).pack(side=tk.BOTTOM)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Whiteboard(root)
    root.mainloop()
