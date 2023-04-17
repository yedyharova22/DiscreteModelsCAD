import math
from tkinter import *
from tkinter import filedialog

import numpy as np
from PIL.ImageDraw import ImageDraw

from DM.РГР.graph import Graph


class App:
    def __init__(self, root):
        self.matrix_text = ""

        self.root = root
        self.root.title("Tarjan's Algorithm")
        self.root.geometry("435x700")

        self.lbl_i = Label(text="Введіть матрицю інцидентності:")
        self.lbl_i.grid(row=0, column=0)

        self.inp_i = Text(height=17, width=26)
        self.inp_i.grid(row=1, column=0)

        self.lbl_res = Label(text="Результат:")
        self.lbl_res.grid(row=0, column=1)
        self.text = Text(height=17, width=26)
        self.text.grid(row=1, column=1)

        self.btnCalc = Button(text="Знайти точки зʼєднання", width=20, command=self.calculate)
        self.btnClear = Button(text="Очистити", width=20, command=self.clear)
        self.btnCalc.grid(row = 3,column = 1)
        self.btnClear.grid(row = 4,column = 1)

        self.lbl_res = Label(text="АБО")
        self.lbl_res.grid(row=3, column=0)
        self.btnUpload = Button(text="Завантажити матрицю txt", width=20, command=self.browse_file)
        self.btnUpload.grid(row=4, column=0)

    def browse_file(self):
        # Open a file dialog to choose a file to open
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

        # Open the selected file and read its contents
        with open(file_path, 'r') as file:
            content = file.read()
            self.matrix_text = content
            self.inp_i.insert(1.0, file.name)

    def drawGraph(self, adj_matrix):
        # Create a canvas widget with a white background
        canvas_width = 370
        canvas_height = 370
        canvas = Canvas(self.root, width=canvas_width, height=canvas_height, bg='white')
        canvas.grid(row=6, column=0, columnspan=2)
        # Compute the coordinates of the nodes
        num_nodes = len(adj_matrix)
        node_coords = []
        for i in range(num_nodes):
            x = canvas_width / 2 + 100 * math.cos(i * 2 * math.pi / num_nodes)
            y = canvas_height / 2 + 100 * math.sin(i * 2 * math.pi / num_nodes)
            node_coords.append((x, y))

        # Draw the edges
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if adj_matrix[i][j] > 0:
                    x1, y1 = node_coords[i]
                    x2, y2 = node_coords[j]
                    canvas.create_line(x1, y1, x2, y2)

        # Draw the nodes
        for i, (x, y) in enumerate(node_coords):
            canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill='lightblue')
            canvas.create_text(x, y, text=str(i + 1))

    def calculate(self):
        try:
            # i = int(self.inp_i.get() or 0)
            # xi = float(self.inp_xi.get())
            # result = (math.sqrt(xi) + math.sin(xi)) / (xi + math.pow(math.e, xi))
            # self.text.insert(2.0, str(round(result, 4)))
            # with open("Yedyharova.txt", 'w') as f:
            #     f.write("Result F = " + str(result))
            # return result
            if len(self.matrix_text) == 0:
                self.matrix_text = self.inp_i.get("1.0", END)
            rows = self.matrix_text.strip().split("\n")
            matrix = np.array([list(map(int, row.strip().split(" "))) for row in rows])
            print(matrix, len(matrix))

            graph = Graph(len(matrix))
            graph.addEdgesFromMatrix(matrix)
            res = graph.AP()

            self.drawGraph(matrix)

            if len(res) == 0:
                self.text.insert(1.0, "Точки зʼєднання не знайдені")
                print("Точки зʼєднання не знайдені")
            else:
                self.text.insert(1.0, "Точки зʼєднання: ")
                print("Точки зʼєднання: ")
                for index, value in enumerate(res):
                    if value:
                        self.text.insert(2.0, str(index + 1) + ' ')
                        print(index, end=" ")

        except ValueError:
            self.text.delete(1.0, END)
            self.text.insert(1.0, "Виникла помилка! \nСпробуйте інше значення!")

    def clear(self):
        self.inp_i.delete(1.0,END)
        self.text.delete(1.0, END)


root = Tk()
app = App(root)
root.mainloop()
