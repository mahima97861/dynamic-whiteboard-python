# dynamic-whiteboard-python
An interactive whiteboard application built with Python, Tkinter, and Matplotlib that allows users to draw freely and generate dynamic plots by executing code in a built-in editor.

This project is an interactive whiteboard application built using Python. It allows users to draw freely and generate dynamic visualizations using Matplotlib by writing code inside a built-in code editor.

## 🚀 Features
- Freehand drawing on canvas
- Shape tools (Line, Rectangle, Oval)
- Color picker and brush size control
- Eraser functionality
- Clear canvas option
- Integrated code editor to run Matplotlib code
- Real-time graph rendering on whiteboard

## 🛠️ Technologies Used
- Python
- Tkinter (GUI)
- Matplotlib (Visualization)
- Pillow (Image Processing)

## ▶️ How to Run

1. Install dependencies: pip install -r requirements.txt
2. Run the project: python main.py


## 📊 Example Graph Codes

### Line Graph

plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("Line Plot on Whiteboard")


### Scatter Plot

plt.scatter([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("Scatter Plot on Whiteboard")


### Bar Plot

plt.bar([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("Bar Plot on Whiteboard")


### Histogram

plt.hist([1, 2, 2, 3, 4, 5, 6], bins=5)
plt.title("Histogram on Whiteboard")


### Pie Chart

plt.pie([10, 20, 30, 40], labels=["A", "B", "C", "D"], autopct='%1.1f%%')
plt.title("Pie Chart on Whiteboard")


## 🎯 Learning Outcomes
- GUI development using Tkinter
- Integration of Matplotlib in applications
- Event handling and drawing logic
- Executing dynamic Python code

⭐ Developed as a BCA project to explore GUI and data visualization.
