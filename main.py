from Modes.Calculator import calculator
from Modes.Graph import graphing
from Modes.Triangles import solveTri
from Modes.ElectronConfig import electronConfig
from Modes.Ellipsis import ellipseCalculator
from Modes.encryption import encryption
from Util.Math_Functions import *
from decimal import Decimal
from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont

allModes = {
  "Calculator": calculator,
  "Graph": graphing,
  "Solve Triangle": solveTri,
  "Electron Config" : electronConfig,
  "Solve Ellipse": ellipseCalculator,
  "Encrypt": encryption
}

'''class App(Tk):
  def __init__(self, *args, **kwargs):
    #self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold",slant="italic")
    #self.title('Super Solver')
    # the container is where we'll stack a bunch of frames
    # on top of each other, then the one we want visible
    # will be raised above the others
    container = Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}
    for F in (StartPage, Calculator, SolveTriangle):
        page_name = F.__name__
        frame = F(parent=container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

class StartPage(Frame):
  def __init__(self, parent, controller):
      Frame.__init__(self, parent)
      self.controller = controller
      label = Label(self, text="This is the start page", font=controller.title_font)
      label.pack(side="top", fill="x", pady=10)

      button1 = Button(self, text="Calculator",
                            command=lambda: controller.show_frame("Calculator"))
      button2 = Button(self, text="Triangle Solver",
                            command=lambda: controller.show_frame("SolveTriangle"))
      button1.pack()
      button2.pack()

class Calculator(Frame):
  def __init__(self, parent, controller):
      Frame.__init__(self, parent)
      self.controller = controller
      label = Label(self, text="Calculator", font=controller.title_font)
      label.pack(side="top", fill="x", pady=10)

      button1 = Button(self, text="Menu",
                            command=lambda: controller.show_frame("StartPage"))
      button1.pack()

class SolveTriangle(Frame):
  def __init__(self, parent, controller):
      Frame.__init__(self, parent)
      self.controller = controller
      label = Label(self, text="Triangle Solver", font=controller.title_font)
      label.pack(side="top", fill="x", pady=10)

      button1 = Button(self, text="Menu",
                            command=lambda: controller.show_frame("StartPage"))
      button1.pack()

app = App()
app.mainloop()


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()'''


running = True
while running:
  for choice in allModes:
    print(f"-{choice}")
  
  Input = input()
  if Input == 'exit':
    running = False
    continue

  calculating = True
  try:
    while calculating:
      allModes[Input]()
      if input() == 'exit':
        calculating = False
  except:
      print("Error")