import logging
from flask import Flask


app = Flask(__name__)


@app.route('/')
import tkinter as tk
root=tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)

canvas1.pack()
def hello ():
    label1 = tk.Label(root, text= 'Hello, Welcome To PyCalc! Now you can use the application. Click the cross Button to open the calculator.', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
button1 = tk.Button(text='CLICK TO START',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)


root.mainloop()
#Start of code and action
def ADD(A,B):
    return A+B
def SUBSTRACT(A,B):
    return A-B
def MULTIPLY(A,B):
    return A*B
def QUOTIENT_OF_DIVISION(A,B):
    return A//B
def REMAINDER_OF_DIVISION(A,B):
    return A%B
def AVERAGE(A,B):
    return (A+B)/2
def N_ROOT(A,B):
    return (A)**(1/B)
def POWER(A,B):
    return (A)**(B)
def COMPOSE(f,g):
    return lambda x : f(g(x))

print("WELCOME TO PyCalc")
print("HERE YOU CAN DO BASIC ARITHMETIC OPERATIONS AND MANY MORE!")
print("WE HAVE INSTALLED A WINDOW WHERE YOU CAN ALSO DO THE COMPLEX CALCULATIONS(EXCLUDING GRAPHS). YOU CAN USE EITHER OF THEM. BUT WE RECOMMEND YOU TO USE IT FOR DOUBLE CHECK! WE HAVE INCLUDED IT IN FUN ZONE SECTION.")
print("REMEMBER THE FOLLOWING KEYWORDS:")
print("ADD(A,B): FOR ADDING A AND B.")
print("SUBSTRACT(A,B): FOR SUBSTRACTING B FROM A.")
print("MULTIPLY(A,B): FOR MULTIPLYING A AND B.")
print("SQRT(A): FOR SQUARE ROOT.")
print("POWER(A,B): FOR A^B.")
print("AVERAGE(A,B): FOR AVERAGE OF A AND B.")
print("QUOTIENT_OF_DIVISION(A,B): QUOTIENT WHEN A IS DIVIDED BY B.")
print("REMAINDER_OF_DIVISION(A,B): REMAINDER WHEN A IS DIVIDED BY B.")
print("exp() : EULER'S NUMBER.")
print("TYPE x**a FOR x^a")
print("A KIND REQUEST:PLEASE DO NOT USE THE COMPOSITIO FOR GRAPHS. IT'S STILL UNDER PROCESSING STAGE! ")
print("PLEASE SELECT FROM FOLLOWING OPERATIONS:")
print("BASIC_OPERATIONS\nPARTITIONS\nFINDING_ROOTS\nLOGARITHMIC_OPERATIONS\nTRIGONOMETRIC_OPERATIONS\nINVERSE_TRIGONOMETRIC_OPERATIONS\nGRAPHS\nCALCULUS\nNUMBER_THEORY\nCOMBINATORIAL_CALCULATIONS\nAREA_CALCULATIONS\nVOLUME_CALCULATIONS\nSOLVE_SYSTEM_OF_LINEAR_EQUATIONS\nBASE_CONVERSION\nMiniCalc\nFUN_ZONE\nMATRIX_OPERATIONS\nNUMBER_THEORETIC_FUNCTIONS")
E = input("ENTER THE OPERATION YOU NEED:")

if E == "BASIC_OPERATIONS":
    import re
    calc = input("CALCULATION: ")
    num_list = re.split('[- + * / ^]', calc)
    orig_calc_list = [char for char in calc]
    calc_list = []
    ind = 0
    can_proceed = True

    for item in orig_calc_list:
      if item.isdigit() == False:
        if item == '+' or item == '-' or item == '*' or item == '/' or item == '.' or item == '^':
            if orig_calc_list[ind + 1].isdigit() == False or orig_calc_list[ind - 1].isdigit() == False:
                print("Invalid Input")
                can_proceed = False
                break
        else:
            print("INVALID INPUT")
            can_proceed = False
            break
      if item == '+' or item == '-' or item == '*' or item == '/' or item == '^':
        calc_list.append(item)
      ind += 1
    del orig_calc_list
    if can_proceed == True:
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        i = 0
        while i < len(calc_list):
            if calc_list[i] == '^':
                num_list[i] = num_list[i] ** num_list[i + 1]
                num_list.pop(i + 1)
                calc_list.pop(i)
                calc_list.append('')
                i -= 1
            i += 1
        i = 0
        while i < len(calc_list):
            if calc_list[i] == '*':
                num_list[i] = num_list[i] * num_list[i + 1]
                num_list.pop(i + 1)
                calc_list.pop(i)
                calc_list.append('')
                i -= 1
            elif calc_list[i] == '/':
                num_list[i] = num_list[i] / num_list[i + 1]
                num_list.pop(i + 1)
                calc_list.pop(i)
                calc_list.append('')
                i -= 1
            i += 1
        i = 0
        while i < len(calc_list):
            if calc_list[i] == '+':
                num_list[i] = num_list[i] + num_list[i + 1]
                num_list.pop(i + 1)
                calc_list.pop(i)
                calc_list.append('')
                i -= 1
            elif calc_list[i] == '-':
                num_list[i] = num_list[i] - num_list[i + 1]
                num_list.pop(i + 1)
                calc_list.pop(i)
                calc_list.append('')
                i -= 1
            i += 1
        print(num_list[0])


elif E == "PARTITIONS":
    import winsound
    winsound.Beep(1000,100)
    w = int(input("HOW MANY TIMES YOU WANT TO FIND THE NUMBER OF PARTITIONS OF A NUMBER:"))
    for i in range(w):
         s=int(input("ENTER THE NUMBER:"))
         X=1/((4*s*3**(1/2))*(2.718)**(3.414*((2*s)/3)**(1/2)))
         print("~" , str(X))
    i=i+1
elif E == "FINDING_ROOTS":
    a=int(input("HOW MANY TIMES DO YOU WANT TO WANT TO USE THIS OPERATION:"))
    for i in range(a):
        import winsound
        winsound.Beep(1000,100)
        V=int(input("ENTER THE DEGREE OF THE POLYNOMIAL:"))
        if V == 2:
            import winsound
            winsound.Beep(1000,100)
            Y=int(input("ENTER THE COEFFICIENT OF X^2:"))
            Z=int(input("ENTER THE COEFFICIENT OF X:"))
            W=int(input("ENTER THE CONSTANT:"))
            T=(-Z+((Z**2)-4*Y*W)**(1/2))/(2*Y)
            U=(-Z-((Z**2)-4*Y*W)**(1/2))/(2*Y)
            print("THE POLYNOMIAL IS ({}X^2) + ({}X) + ({})".format(Y,Z,W))
            print("THE FIRST ROOT IS",T)
            print("THE SECOND ROOT IS",U)
        else:
            import winsound
            winsound.Beep(1000,100)
            print("WE CURRENTLY DON'T SUPPORT POLYNOMIALS OF DEGREES MORE THAN 2")
    i+=1
elif E == "LOGARITHMIC_OPERATIONS":
    m=int(input("HOW MANY TIMES DO YOU WANT TO WANT TO USE THIS OPERATION:"))
    for i in range(m):
        import winsound
        winsound.Beep(1000,100)
        a=int(input("ENTER THE NUMBER:"))
        import math
        print(math.log(a))
    i+=1
elif E == "TRIGONOMETRIC_OPERATIONS":
    O = int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    for i in range(O):
        print("sin(x)\ncos(x)\ntan(x)\nsec(x)\ncosec(x)\ncot(x)")
        d=input("ENTER THE FUNCTION:")
        if d == "sin(x)":
            import math
            x=int(input("ENTER THE VALUE OF x:"))
            print(math.sin(x))
        elif d == "cos(x)":
            import math
            x=int(input("ENTER THE VALUE OF x:"))
            print(math.cos(x))
        elif d == "tan(x)":
            import math
            x=int(input("ENTER THE VALUE OF x:"))
            print(math.tan(x))
        elif d == "sec(x)":
            import math
            x=int(input("ENTER THE VALUE OF x:"))
            a = (math.cos(x))
            print(1/a)
        elif d == "cosec(x)":
            import math
            x=int(input("ENTER THE VALUE OF x:"))
            a = (math.sin(x))
            print(1/a)
        elif d == "cot(x)":
            import math
            x=int(input("ENTER THE VALUE OF x:"))
            a = (math.tan(x))
            print(1/a)
        else:
            print("INVALID INPUT!")
    O+=1
elif E == "INVERSE_TRIGONOMETRIC_OPERATIONS":
    import winsound
    winsound.Beep(1000,100)
    m=int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    import winsound
    winsound.Beep(1000,100)
    for i in range(m):
            print("arcsin(x)\narccos(x)\narctan(x)")
            d = input("ENTER THE FUNCTION:")
            import winsound
            winsound.Beep(1000,100)
            if d == "arcsin(x)":
                import winsound
                winsound.Beep(1000,100)
                import math
                e=float(input("ENTER THE VALUE OF X:"))
                print(str(math.asin(e)) , "(IN RADIANS)")
            elif d == "arccos(x)":
                import winsound
                winsound.Beep(1000,100)
                import math
                e=float(input("ENTER THE VALUE OF X:"))
                print(str(math.acos(e)) , "(IN RADIANS)")
            elif d == "arctan(x)":
                import winsound
                winsound.Beep(1000,100)
                import math
                e=float(input("ENTER THE VALUE OF X:"))
                print(str(math.atan(e)) , "(IN RADIANS)")
    i+=1
elif E == "POWER":
    m=int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    for i in range(m):
        import winsound
        winsound.Beep(1000,100)
        A=int(input("ENTER THE BASE:"))
        B=int(input("ENTER THE EXPONENT:"))
        print(POWER(A,B))
    i+=1
elif E == "N_ROOT":
    m=int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    for i in range(m):
        import winsound
        winsound.Beep(1000,100)
        A=int(input("ENTER THE NUMBER:"))
        B=int(input("ENTER THE NUMBER N:"))
        print(N_ROOT(A,B))
    i+=1


elif E == "GRAPHS":
    m=int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    for i in range(m):
        from tkinter import *
        import winsound
        winsound.Beep(1000,100)
        print("TRIGONOMETRIC\nEXPONENTIAL\nLOGARITHMIC\nPOLYNOMIAL\nCOMPOSITION")
        d=input("PLEASE ENTER WHICH TYPE OF GRAPH YOU HAVE TO MAKE:")
        if d == "TRIGONOMETRIC":
             import winsound
             winsound.Beep(1000,100)
             b=input("ENTER THE TRIGONONOMETRIC FUNCTION(sin/cos/tan):")
             c=float(input("ENTER THE NUMBER WHICH WILL BE COEFICIENT OF theta:"))
             if b == "sin":
              import winsound
              winsound.Beep(1000,100)
              from matplotlib.figure import Figure
              from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
              class Root(Tk):
                  def __init__(self):
                      super(Root, self).__init__()
                      self.title("Tkinter First Window")
                      self.minsize(640, 400)
                      self.wm_iconbitmap('py.ico')
                      self.matplotCanvas()
                  def matplotCanvas(self):
                      f = Figure(figsize=(5,5), dpi=100)
                      plt = f.add_subplot(111)
                      import numpy as np
                      c=float(input("ENTER THE NUMBER WHICH WILL BE COEFICIENT OF theta:"))
                      x=np.arange(0, c*(np.pi), 0.1)
                      y=np.sin(x)
                      plt.plot(x,y)
                      canvas = FigureCanvasTkAgg(f, self)
                      canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
              if __name__ == '__main__':
                  root = Root()
                  root.mainloop()
             elif b == "cos":
              import winsound
              winsound.Beep(1000,100)
              from matplotlib.figure import Figure
              from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
              class Root(Tk):
                  def __init__(self):
                      super(Root, self).__init__()
                      self.title("Tkinter First Window")
                      self.minsize(640, 400)
                      self.wm_iconbitmap('py.ico')
                      self.matplotCanvas()
                  def matplotCanvas(self):
                      f = Figure(figsize=(5,5), dpi=100)
                      plt = f.add_subplot(111)
                      import numpy as np
                      c=float(input("ENTER THE NUMBER WHICH WILL BE COEFICIENT OF theta:"))
                      x=np.arange(0, c*(np.pi), 0.1)
                      y=np.cos(x)
                      plt.plot(x,y)
                      canvas = FigureCanvasTkAgg(f, self)
                      canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
              if __name__ == '__main__':
                  root = Root()
                  root.mainloop()

             elif b == "tan":
              import winsound
              winsound.Beep(1000,100)
              from matplotlib.figure import Figure
              from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
              class Root(Tk):
                  def __init__(self):
                      super(Root, self).__init__()
                      self.title("Tkinter First Window")
                      self.minsize(640, 400)
                      self.wm_iconbitmap('py.ico')
                      self.matplotCanvas()
                  def matplotCanvas(self):
                      f = Figure(figsize=(5,5), dpi=100)
                      plt = f.add_subplot(111)
                      import numpy as np
                      c=float(input("ENTER THE NUMBER WHICH WILL BE COEFICIENT OF theta:"))
                      x=np.arange(0, c*(np.pi), 0.1)
                      y=np.tan(x)
                      plt.plot(x,y)
                      canvas = FigureCanvasTkAgg(f, self)
                      canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
              if __name__ == '__main__':
                  root = Root()
                  root.mainloop()
             elif b == "cosec":
              import winsound
              winsound.Beep(1000,100)
              import matplotlib.pyplot as plt
              import numpy as np
              x=np.arange(0, c*(np.pi), 0.1)
              y=np.csc(x)
              plt.plot(x,y)
              plt.show()
             elif b == "sec":
              import matplotlib.pyplot as plt
              import numpy as np
              x=np.arange(0, c*(np.pi), 0.1)
              y=np.sec(x)
              plt.plot(x,y)
              plt.show()
             elif b == "cot":
              import matplotlib.pyplot as plt
              import numpy as np
              x=np.arange(0, c*(np.pi), 0.1)
              y=np.cot(x)
              plt.plot(x,y)
              plt.show()
             else:
              import winsound
              winsound.Beep(1000,100)
              print("INVALID INPUT")
        elif d == "EXPONENTIAL":
            import winsound
            winsound.Beep(1000,100)
            from tkinter import *
            from matplotlib.figure import Figure
            from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
            class Root(Tk):
                def __init__(self):
                    super(Root, self).__init__()
                    self.title("Graphs")
                    self.minsize(640, 400)
                    self.wm_iconbitmap('py.ico')
                    self.matplotCanvas()

                def matplotCanvas(self):
                    f = Figure(figsize=(5,5), dpi=100)
                    plt = f.add_subplot(111)
                    import numpy as np
                    c=int(input("ENTER THE NUMBER WHICH WILL BE THE FIRST VALUE IN THE RANGE:"))
                    d=int(input("ENTER THE NUMBER WHICH WILL BE THE SECOND VALUE IN THE RANGE:"))
                    x=np.arange(c,d,0.1)
                    e=2.718281828
                    y=np.e**x
                    plt.plot(x,y)
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
            if __name__ == '__main__':
               root = Root()
               root.mainloop()
        elif d == "LOGARITHMIC":
            import winsound
            winsound.Beep(1000,100)
            import winsound
            winsound.Beep(1000,100)
            from tkinter import *
            from matplotlib.figure import Figure
            from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
            class Root(Tk):
                def __init__(self):
                    super(Root, self).__init__()
                    self.title("Graphs")
                    self.minsize(640, 400)
                    self.wm_iconbitmap('py.ico')
                    self.matplotCanvas()

                def matplotCanvas(self):
                    f = Figure(figsize=(5,5), dpi=100)
                    plt = f.add_subplot(111)
                    import numpy as np
                    c=int(input("ENTER THE NUMBER WHICH WILL BE THE FIRST VALUE IN THE RANGE:"))
                    d=int(input("ENTER THE NUMBER WHICH WILL BE THE SECOND VALUE IN THE RANGE:"))
                    x=np.arange(c,d,0.1)
                    y=np.log(x)
                    plt.plot(x,y)
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
            if __name__ == '__main__':
               root = Root()
               root.mainloop()

        elif d == "POLYNOMIAL":
            a_y = input("ENTER WHAT TYPE OF POLYNOMIAL GRAPH(LINEAR/QUADRATIC/CUBIC/BIQUADRATIC):")
            if a_y == "LINEAR":
                import winsound
                winsound.Beep(1000,100)
                from tkinter import *
                from matplotlib.figure import Figure
                from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
                class Root(Tk):
                     def __init__(self):
                         super(Root, self).__init__()
                         self.title("Graphs")
                         self.minsize(640, 400)
                         self.wm_iconbitmap('py.ico')
                         self.matplotCanvas()

                     def matplotCanvas(self):
                         f = Figure(figsize=(5,5), dpi=100)
                         plt = f.add_subplot(111)
                         import numpy as np
                         a_e = int(input("ENTER THE COEFFICIENT OF X:"))
                         a_f = int(input("ENTER THE CONSTANT:"))
                         a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
                         a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
                         x=np.linspace(a_g,a_h,256, endpoint=True)
                         y=a_e*(x)+a_f
                         plt.plot(x,y)
                         #plt.show()
                         canvas = FigureCanvasTkAgg(f, self)
                         canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
                if __name__ == '__main__':
                   root = Root()
                   root.mainloop()
            if a_y == "QUADRATIC":
                from tkinter import *
                from matplotlib.figure import Figure
                from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
                class Root(Tk):
                     def __init__(self):
                         super(Root, self).__init__()
                         self.title("Graphs")
                         self.minsize(640, 400)
                         self.wm_iconbitmap('py.ico')
                         self.matplotCanvas()

                     def matplotCanvas(self):
                         f = Figure(figsize=(5,5), dpi=100)
                         plt = f.add_subplot(111)
                         import numpy as np
                         a_s=int(input("ENTER THE COEFFICIENT OF X^2:"))
                         a_d=int(input("ENTER THE COEFFICIENT OF X:"))
                         a_f=int(input("ENTER THE CONSTANT:"))
                         a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
                         a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
                         x=np.linspace(a_g,a_h,256, endpoint = True)
                         y=(a_s*(x*x))+(a_d*x)+a_f
                         plt.plot(x,y)
                         canvas = FigureCanvasTkAgg(f, self)
                         canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
                if __name__ == '__main__':
                   root = Root()
                   root.mainloop()

            elif a_y == "CUBIC":
                from tkinter import *
                from matplotlib.figure import Figure
                from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
                class Root(Tk):
                     def __init__(self):
                         super(Root, self).__init__()
                         self.title("Graphs")
                         self.minsize(640, 400)
                         self.wm_iconbitmap('py.ico')
                         self.matplotCanvas()

                     def matplotCanvas(self):
                         f = Figure(figsize=(5,5), dpi=100)
                         plt = f.add_subplot(111)
                         import numpy as np
                         a_q=int(input("ENTER THE COEFFICIENT OF X^3:"))
                         a_s=int(input("ENTER THE COEFFICIENT OF X^2:"))
                         a_d=int(input("ENTER THE COEFFICIENT OF X:"))
                         a_f=int(input("ENTER THE CONSTANT:"))
                         a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
                         a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
                         x=np.linspace(a_g,a_h,256, endpoint = True)
                         y=(a_q*(x*x*x))+(a_s*(x*x))+(a_d*x)+a_f
                         plt.plot(x,y)
                         canvas = FigureCanvasTkAgg(f, self)
                         canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
                if __name__ == '__main__':
                   root = Root()
                   root.mainloop()

            elif a_y == "BIQUADRATIC":
                from tkinter import *
                from matplotlib.figure import Figure
                from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
                class Root(Tk):
                     def __init__(self):
                         super(Root, self).__init__()
                         self.title("Graphs")
                         self.minsize(640, 400)
                         self.wm_iconbitmap('py.ico')
                         self.matplotCanvas()

                     def matplotCanvas(self):
                         f = Figure(figsize=(5,5), dpi=100)
                         plt = f.add_subplot(111)
                         import numpy as np
                         a_r=int(input("ENTER THE COEFFICIENT OF X^4:"))
                         a_q=int(input("ENTER THE COEFFICIENT OF X^3:"))
                         a_s=int(input("ENTER THE COEFFICIENT OF X^2:"))
                         a_d=int(input("ENTER THE COEFFICIENT OF X:"))
                         a_f=int(input("ENTER THE CONSTANT:"))
                         a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
                         a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
                         x=np.linspace(a_g,a_h,256, endpoint = True)
                         y=(a_r*(x*x*x*x))+(a_q*(x*x*x))+(a_s*(x*x))+(a_d*x)+a_f
                         plt.plot(x,y)
                         canvas = FigureCanvasTkAgg(f, self)
                         canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
                if __name__ == '__main__':
                   root = Root()
                   root.mainloop()

        elif d == "COMPOSITION":
            import winsound
            winsound.Beep(1000,100)
            import numpy as np
            import matplotlib.pyplot as plt
            q_s =int(input("ENTER THE LOWER BOUND IN THE RANGE:"))
            t_i =int(input("ENTER THE UPPER BOUND IN THE RANGE:"))
            e_w = input("ENTER THE INNER FUNCTION:")
            w_e = input("ENTER THE OUTER FUNCTION:")
            x = np.linspace(q_s,t_i,0.1)
            y = COMPOSE(w_e, e_w)
            plt.plot(x,y)
            plt.show()
        else:
            import winsound
            winsound.Beep(1000,100)
            print("INVALID INPUT")
    i+=1
elif E == "CALCULUS":
    m=int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    for i in range(m):
        k=input("DIFFERENTIATION/INTEGRATION:")
        if k == "DIFFERENTIATION":
            print("REMEMBER! IN OUTPUT THE FIRST, SECOND, THIRD CONTAINS THE FIRST DERIVATIVE, SECOND DERIVATIVE....and so on"  )
            l=input("WHICH TYPE OF FUNCTION YOU WANT TO USE TRIGONOMETRIC,ALGEBRIC,LOGARITHMIC,EXPONENTIAL:")
            if l == "TRIGONOMETRIC":
                import winsound
                winsound.Beep(1000,100)
                m = input("ENTER THE TRIGONOMETRIC FUNCTION(sin/cos/tan/cosec/sec/cot):")
                if m == "sin":
                    import winsound
                    winsound.Beep(1000,100)
                    n=input("ENTER THE FUNCTION WHICH WILL BE WITHIN SIN():")
                    from sympy import *
                    x,y,z = symbols('x y z')
                    init_printing(use_unicode=True)
                    k_l=diff(sin(n)),"-->THE FIRST DERIVATIVE W.R.T x"
                    k_m=diff(diff(sin(n))),"-->THE SECOND DERIVATIVE W.R.T x"
                    k_n=diff(diff(diff(sin(n)))),"-->THE THIRD DERIVATIVE W.R.T x"
                    k_o=diff(diff(diff(diff(sin(n))))),"-->THE FOURTH DERIVATIVE W.R.T x"
                    print(k_l)
                    print(k_m)
                    print(k_n)
                    print(k_o)


                elif m == "cos":
                    import winsound
                    winsound.Beep(1000,100)
                    o=input("ENTER THE FUNCTION WHICH WILL BE WITHIN COS():")
                    from sympy import *
                    x,y,z = symbols('x y z')
                    init_printing(use_unicode=True)
                    j_k=(diff(cos(o)),x),"-->THE FIRST DERIVATIVE W.R.T x"
                    k_j=(diff(diff(cos(o))),x), "-->THE SECOND DERIVATIVE W.R.T x"
                    f_j=(diff(diff(diff(cos(o)))),x), "-->THE THIRD DERIVATIVE W.R.T x"
                    l_o=(diff(diff(diff(diff(cos(o))))),x), "-->THE FOURTH DERIVATIVE W.R.T x"
                    print(j_k)
                    print(k_j)
                    print(f_j)
                    print(l_o)


                elif m == "tan":
                    import winsound
                    winsound.Beep(1000,100)
                    p=input("ENTER THE FUNCTION WHICH WILL BE WITHIN TAN():")
                    from sympy import *
                    x,y,z = symbols('x y z')
                    init_printing(use_unicode=True)
                    i_j=(diff(tan(p)),x)
                    j_i=(diff(diff(tan(p))),x)
                    d_f=(diff(diff(diff(tan(p)))),x)
                    f_d=(diff(diff(diff(diff(tan(p))))),x)
                    print(i_j)
                    print(j_i)
                    print(d_f)
                    print(f_d)


                elif m == "cosec":
                    import winsound
                    winsound.Beep(1000,100)
                    q=input("ENTER THE FUNCTION WHICH IS WITHIN COSEC():")
                    from sympy import *
                    x,y,z = symbols('x y z')
                    init_printing(use_unicode=True)
                    h_i=(diff(1/sin(q)),x)
                    i_h=(diff((diff(1/sin(q)))),x)
                    g_h=(diff(diff(diff(1/sin(q)))),x)
                    h_g=(diff(diff(diff(diff(1/sin(q))))),x)
                    print(h_i)
                    print(i_h)
                    print(g_h)
                    print(h_g)


                elif m == "sec":
                    import winsound
                    winsound.Beep(1000,100)
                    r=input("ENTER THE FUNCTION WHICH WILL BE WITHIN SEC():")
                    from sympy import *
                    x,y,z = symbols('x y z')
                    init_printing(use_unicode=True)
                    g_h=(diff(1/cos(r)),x)
                    h_g=(diff(diff(1/cos(r))),x)
                    d_t=(diff(diff(diff(1/cos(r)))),x)
                    t_d=(diff(diff(diff(diff(1/cos(r))))),x)
                    print(g_h)
                    print(h_g)
                    print(d_t)
                    print(t_d)


                elif m == "cot":
                    import winsound
                    winsound.Beep(1000,100)
                    s=input("ENTER THE FUNCTION WHICH WILL BE WITHIN COT():")
                    from sympy import *
                    x,y,z = symbols('x y z')
                    init_printing(use_unicode=True)
                    f_g=(diff(1/tan(s)),x)
                    g_f=(diff(diff(1/tan(s))),x)
                    d_g=(diff(diff(diff(1/tan(s)))),x)
                    g_d=(diff(diff(diff(diff(1/tan(s))))),x)
                    print(f_g)
                    print(g_f)
                    print(d_g)
                    print(g_d)


                else:
                    print("INVALID INPUT")
            elif l == "ALGEBRIC":
                t=input("ENTER THE ALGEBRIC EXPRESSION:")
                from sympy import *
                x,y,z = symbols('x y z')
                init_printing(use_unicode=True)
                e_f=(diff(t),x)
                f_e=(diff(diff(t)),x)
                f_g=(diff(diff(diff(t))),x)
                g_f=(diff(diff(diff(diff(t)))),x)
                print(e_f)
                print(f_e)
                print(f_g)
                print(g_f)

            elif l == "LOGARITHMIC":
                u=input("ENTER THE FUNCTION WHICH WILL BE IN LOG():")
                from sympy import *
                x,y,z = symbols('x y z')
                init_printing(use_unicode=True)
                c_d=(diff(log(u)),x)
                d_c=(diff(diff(log(u))),x)
                k_j=(diff(diff(diff(log(u)))),x)
                j_k=(diff(diff(diff(diff(log(u))))),x)
                print(c_d)
                print(d_c)
                print(k_j)
                print(j_k)



            elif l == "EXPONENTIAL":
                import winsound
                winsound.Beep(1000,100)
                v=input("ENTER THE FUNCTION WHICH WILL BE IN THE POWER OF e:")
                from sympy import *
                x,y,z = symbols('x y z')
                init_printing(use_unicode=True)
                for a_b in range(4):
                    d_e=(diff(exp(v),x))
                    e_d=(diff(diff(exp(v))),x)
                    ncb=(diff(diff(diff(exp(v)))),x)
                    bcn=(diff(diff(diff(diff(exp(v))))),x)
                    print(d_e)
                    print(e_d)
                    print(ncb)
                    print(bcn)



            else:
                print("INVALID INPUT")
        elif k == "INTEGRATION":
            p = input("WHAT TYPE OF INTEGRATION?(DEFINITE/INDEFINITE):")
            if p == "INDEFINTE":
                w=input("WHICH TYPE OF FUNCTION YOU WANT TO USE (TRIGONOMETRIC,ALGEBRIC,LOGARITHMIC,EXPONENTIAL) :")
                if w == "ALGEBRIC":
                    p_q = input("WHICH TYPE OF INTEGRAL DO YOU NEED(SINGLE/DOUBLE/TRIPLE):")
                    if p_q == "LINE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(m_n, x))
                    elif p_q == "SURFACE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y=symbols('x y')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(m_n, x, y))
                    elif p_q == "VOLUME":
                        import winsound
                        winsound.Beep(1000,100)
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y,z=symbols('x y z')
                        m_n = input("ENTER THE FUNCTION:")
                        print (integrate(m_n, x, y, z))
                    else:
                        print("INVALID INPUT")

                elif w == "TRIGONOMETRIC':
                    a_y=input("WHICH TYPE FO INTEGRAL DO YOU WANT(SINGLE/DOUBLE/TRIPLE):")
                    if a_y == "SINGLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(m_n, x))
                    elif a_y == "SURFACE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y=symbols('x y')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(m_n, x, y))
                    elif a_y == "VOLUME":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y,z=symbols('x y z')
                        m_n = input("ENTER THE FUNCTION:")
                        print (integrate(m_n, x, y, z))
                    else:
                        print("INPUT INVALID")

                elif w == "LOGARITHMIC":
                    a_y=input("WHICH TYPE FO INTEGRAL DO YOU WANT(SINGLE/DOUBLE/TRIPLE):")
                    if a_y == "SINGLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(log(m_n), x))
                    elif a_y == "DOUBLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y=symbols('x y')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(log(m_n), x, y))
                    elif a_y == "TRIPLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y,z=symbols('x y z')
                        m_n = input("ENTER THE FUNCTION:")
                        print (integrate(log(m_n), x, y, z))
                    else:
                        print("INVALID INPUT")

                elif w == "EXPONENTIAL":
                    print(" exp(x) MEANS e^x")
                    a_y=input("WHICH TYPE FO INTEGRAL DO YOU WANT(LINE/SURFACE/VOLUME):")
                    if a_y == "LINE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(exp(m_n), x))
                    elif a_y == "SURFACE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y=symbols('x y')
                        m_n=input("ENTER THE FUNCTION:")
                        print(integrate(exp(m_n), x, y))
                    elif a_y == "VOLUME":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x,y,z=symbols('x y z')
                        m_n = input("ENTER THE FUNCTION:")
                        print (integrate(exp(m_n), x, y, z))
                    else:
                        print("INVALID INPUT")

            elif p == "DEFINITE":
                w=input("WHICH TYPE OF FUNCTION YOU WANT TO USE (TRIGONOMETRIC,ALGEBRIC,LOGARITHMIC,EXPONENTIAL):")
                if w == "ALGEBRIC":
                    p_q = input("WHICH TYPE OF INTEGRAL DO YOU NEED(SINGLE/DOUBLE/TRIPLE):")
                    if p_q == "SINGLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        m_n=input("ENTER THE FUNCTION:")
                        l = int(input("ENTER THE LOWER LIMIT:"))
                        u = int(input("ENTER THE UPPER LIMIT:"))
                        print(integrate(m_n, (x, l, u)))
                    elif p_q == "DOUBLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        f = lambda y, x: p
                        print(integrate.dblquad(f, l, u, lambda x: l_a, lambda x: l_b))
                    elif p_q == "TRIPLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        z_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRL W.R.T z):"))
                        z_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T z):"))
                        f = lambda z, y, x: p
                        print(integrate.tplquad(f, l, u, lambda x: l_a, lambda x: l_b, lambda x, y: z_a, lambda x, y: z_b))
                elif w == "TRIGONOMETRIC":
                    p_q = input("WHICH TYPE OF INTEGRAL DO YOU NEED(SINGLE/DOUBLE/TRIPLE):")
                    if p_q == "SINGLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        m_n=input("ENTER THE FUNCTION:")
                        l = int(input("ENTER THE LOWER LIMIT:"))
                        u = int(input("ENTER THE UPPER LIMIT:"))
                        print(integrate(m_n, (x, l, u)))
                    elif p_q == "DOUBLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        f = lambda y, x: p
                        print(integrate.dblquad(f, l, u, lambda x: l_a, lambda x: l_b))
                    elif p_q == "TRIPLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        z_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRL W.R.T z):"))
                        z_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T z):"))
                        f = lambda z, y, x: p
                        print(integrate.tplquad(f, l, u, lambda x: l_a, lambda x: l_b, lambda x, y: z_a, lambda x, y: z_b))
                elif w == "LOGARITHMIC":
                    p_q = input("WHICH TYPE OF INTEGRAL DO YOU NEED(SINGLE/DOUBLE/TRIPLE):")
                    if p_q == "SINGLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        m_n=input("ENTER THE FUNCTION:")
                        l = int(input("ENTER THE LOWER LIMIT:"))
                        u = int(input("ENTER THE UPPER LIMIT:"))
                        print(integrate(m_n, (x, l, u)))
                    elif p_q == "DOUBLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        f = lambda y, x: p
                        print(integrate.dblquad(f, l, u, lambda x: l_a, lambda x: l_b))
                    elif p_q == "TRIPLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        z_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRL W.R.T z):"))
                        z_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T z):"))
                        f = lambda z, y, x: p
                        print(integrate.tplquad(f, l, u, lambda x: l_a, lambda x: l_b, lambda x, y: z_a, lambda x, y: z_b))

                elif w == "EXPONENTIAL":
                    p_q = input("WHICH TYPE OF INTEGRAL DO YOU NEED(SINGLE/DOUBLE/TRIPLE):")
                    if p_q == "SINGLE":
                        from sympy import *
                        init_printing(use_unicode=False, wrap_line=False)
                        x= Symbol('x')
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        m_n=input("ENTER THE FUNCTION:")
                        l = int(input("ENTER THE LOWER LIMIT:"))
                        u = int(input("ENTER THE UPPER LIMIT:"))
                        print(integrate(m_n, (x, l, u)))
                    elif p_q == "DOUBLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        f = lambda y, x: p
                        print(integrate.dblquad(f, l, u, lambda x: l_a, lambda x: l_b))
                    elif p_q == "TRIPLE":
                        from scipy import integrate
                        p = input("ENTER THE FUNCTION:")
                        print("FOR ENTERING +INFINITY, WRITE math.inf AND FOR ENTERING -INFINITY, WRITE -math.inf")
                        l = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T x):"))
                        u = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T x ):"))
                        l_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        l_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T y):"))
                        z_a = int(input("ENTER THE LOWER LIMIT(IN CASE OF INTEGRL W.R.T z):"))
                        z_b = int(input("ENTER THE UPPER LIMIT(IN CASE OF INTEGRAL W.R.T z):"))
                        f = lambda z, y, x: p
                        print(integrate.tplquad(f, l, u, lambda x: l_a, lambda x: l_b, lambda x, y: z_a, lambda x, y: z_b))
                else:
                    print("INVALID INPUT")
    i=i+1
elif E == "NUMBER_THEORY":
    d = int(input("HOW MANY TIMES DO YOU WANT TO USE THIS OPERATION:"))
    for d in range(d):
        print("PyCalc HAS THE FOLLOWING FEATURES FOR NUMBER THEORY:")
        print("PRIME_IDENTIFICATION")
        print("DIVISIBILITY_TEST")
        print("DIOPHANTINE_EQUATIONS")
        print("SPLITTING_A_NUMBER")
        g = input("WHICH OPERATION DO YOU WANT TO USE:")
        if g == "PRIME_IDENTIFICATION":
          import winsound
          winsound.Beep(1000,100)
          D_R = int(input("HOW MANY TIMES YOU WANT TO IDENTIFY PRIMES:"))
          for i in range (D_R):
            a_z = int(input("ENTER THE NUMBER:"))
            if a_z>1:
              for i in range(2,a_z):
                  if a_z%i==0:
                      print("THE NUMBER IS COMPOSITE")
                      break
                  else:
                      print("THE NUMBER IS PRIME")
            else:
              import winsound
              winsound.Beep(1000,100)
              print(" ")
        elif g == "DIOPHANTINE_EQUATIONS":
            import winsound
            winsound.Beep(1000,100)
            from sympy.solvers.diophantine import diophantine
            from sympy import symbols
            x, y, z = symbols("x, y, z", integer=True)
            a = int(input("ENTER THE COEFFICIENT OF x:"))
            b = int(input("ENTER THE COEFFICIENT OF y:"))
            c = int(input("ENTER THE CONSTANT: "))
            print(diophantine(a*x+b*y-c))
        elif g == "DIVISIBILITY_TEST":
            import winsound
            winsound.Beep(1000,100)
            k = int(input("ENTER IS THE NUMBER THAT YOU WANT TO TEST:"))
            m = int(input("ENTER IS DIVISOR FOR WHICH YOU WANT TO VERIFY:"))
            if k%m == 0:
                print("{} is divisible by {}".format(k,m))
            elif k%m != 0:
                print("{} is not divisible by {}".format(k,m))
                for i in range(1, k-1):
                    if k%i == 0:
                        print("SUGGESTIONS:")
                        print("{} is divisible by {}".format(k,i))
                i+=1
        elif g == "SPLITTING_A_NUMBER":
            import winsound
            winsound.Beep(1000,100)
            S_D = int(input("ENTER THE NUMBER:"))
            for i in range (S_D):
                print(i,"+", S_D-i)
            i=i+1

    d+=1
elif E == "COMBINATORIAL_CALCULATIONS":
    import winsound
    winsound.Beep(1000,100)
    q_s = input("WHICH TYPE OF OPERATION DO YOU WANT?(FACTORIAL_CALCULATIONS/COMBINATORICS):")
    if q_s == "FACTORIAL_CALCULATIONS":
        import winsound
        winsound.Beep(1000,100)
        W_E = int(input("ENTER THE NUMBER:"))
        fact = 1
        for a in range(1,W_E+1):
         fact = fact*a
        print(fact)
    elif q_s == "COMBINATORICS":
        import winsound
        winsound.Beep(1000,100)
        a=input("WHICH TYPE DO YOU WANT(PERMUTATIN/COMBINATION):")
        if a == "PERMUTATION":
            import winsound
            winsound.Beep(1000,100)
            q_r = int(input("IN nPr, PLEASE ENTER THE VALUE OF n:"))
            r_q = int(input("IN nPr, PLEASE ENTER THE VALUE OF r:"))
            p_r = q_r-r_q
            fact = 1
            for i in range(1,q_r+1):
                fact=fact*i
            fact_b = 1
            for n in range(1,p_r+1):
                fact_b=fact_b*n
            import winsound
            winsound.Beep(1000,100)
            print(fact/fact_b)
        elif a == "COMBINATION":
            q_r = int(input("IN nCr, PLEASE ENTER THE VALUE OF n:"))
            r_q = int(input("IN nCr, PLEASE ENTER THE VALUE OF r:"))
            p_r = q_r-r_q
            fact = 1
            for i in range(1,q_r+1):
                fact=fact*i
            fact_b = 1
            for n in range(1,p_r+1):
                fact_b=fact_b*n
            fact_c=1
            for c in range(1,r_q+1):
                fact_c=fact_c*c

            import winsound
            winsound.Beep(1000,100)
            print((fact)/(fact_b*fact_c))


elif E == "AREA_CALCULATIONS":
    import winsound
    winsound.Beep(1000,100)
    a_t = input("WHICH TYPE OF SHAPE DO YOU WANT?(SQUARE/TRIANGLE/RECTANGLE/PARALLELOGRAM/RHOMBUS/SPHERE/CONE):")
    if a_t == "SQUARE":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE SIDE LENGTH:"))
        area = (D_E)**2
        print(area)
    elif a_t == "RECTANGLE":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE LENGTH:"))
        breadth = int(input("ENTER THE BREADTH:"))
        area = D_E*breadth
        print(area)
    elif a_t == "TRIANGLE":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE BASE:"))
        BASE = int(input("ENTER THE HEIGHT:"))
        area = (1/2)*(BASE)*(D_E)
        print(area)
    elif a_t == "PARALLELOGRAM":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE LENGTH OF ONE SIDE:"))
        HEIGHT = int(input("ENTER THE HEIGHT:"))
        area = D_E*HEIGHT
        print(area)
    elif a_t == "RHOMBUS":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE FIRST DIAGONAL:"))
        diagonal = int(input("ENTER THE SECOND DIAGONAL:"))
        area = 1/2*(D_E*diagonal)
        print(area)
    elif a_t == "TRAPEZIUM":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE FIRST BASE:"))
        base = int(input("ENTER THE SECOND BASE:"))
        h_t = int(input("ENTER THE HEIGHT:"))
        area = ((D_E+base)/2)*h_t
        print(area)
    elif a_t == "CIRCLE":
        import winsound
        winsound.Beep(1000,100)
        D_E = int(input("ENTER THE RADIUS:"))
        area = 3.414*(D_E)**2
    elif a_t == "CYLINDER":
            A=int(("ENTER THE RADIUS OF THE BASE:"))
            ht = int(input("ENTER THE HEIGHT:"))
            AREA_a = 2*3.414*A*ht
            print(" CURVED SURFACE AREA:" + str(AREA_a))
            AREA_b = 2*3.414*A*ht
            print("TOTAL SURFACE AREA:" + str(AREA_b))
    elif a_t == "SPHERE":
        R=int(input("ENTER THE RADIUS:"))
        AREA = 4*3.414*R**2
        print("AREA OF THE SPHERE IS:" + str(AREA))
    elif a_t == "RIGHT CIRCULAR CONE":
        R = int(input("ENTER THE RADIUS OF BASE:"))
        h = int(input("ENTER THE HEIGHT:"))
        CSA = 3.414*R*(R**2+h**2)**(1/2)
        TSA = 3.414*R*(R+(R**2+h**2)**(1/2))
        print("THE CURVED SURFACE AREA:" + str(CSA))
        print("THE TOTAL SURFACE AREA:" + str(TSA))

elif E == "VOLUME_CALCULATIONS":
        import winsound
        winsound.Beep(1000, 100)
        print("CUBE\nCUBOID\nSPHERE\nRIGHT_CIRCULAR_CONE\nRIGHT_CIRCULAR_CYLINDER\nPRISM\nRIGHT_RECTANGULAR/SQUARE_PYRAMID\nELLIPSOID\nTETRAHEDRON")
        o = input("ENTER THE SHAPE WHOSE VOULME YOU WANT TO CALCULATE:")
        if o == "CUBE":
            l = int(input("ENTER THE LENGTH OF ONE SIDE:"))
            print("THE VOULEM IS" + str(l**3))
        elif o == "CUBOID":
            l = int(input("ENTER THE LENGHT:"))
            b = int(input("ENTER THE BREADTH:"))
            h = int(input("ENTER THE HEIGHT:"))
            V = l*b*h
            print("THE VOLUME IS:" + str(V))
        elif o == "SPHERE":
            r = int(input("ENTER THE RADIUS:"))
            V = (4/3)*3.141592653589793238*(r)**3
            print("THE VOLUME IS:" + str(V))
        elif o == "RIGHT_CIRCULAR_CONE":
            r = int(input("ENTER THE RADIUS:"))
            h_l = input("DO YOU WANT TO ENTER SLANT HEIGHT OR HEIGHT [TYPE SH FOR SLANT HEIGHT AND H FOR HEIGHT]:")
            if h_l == "SH":
                s_h = int(input("ENTER THE SLANT HEIGHT:"))
                h = (((s_h)**2)-(r**2))**(1/2)
                V = (1/3)*3.141592653589793238*(r**2)*h
                print("THE VOULME IS" + str(V))
            elif h_l == "H":
                h_o = int(input("ENTER THE HEIGHT:"))
                V = (1/3)*3.141592653589793238*(r**2)*h_o
                print("THE VOULME IS:" + str(V))
        elif o == "RIGHT_CIRCULAR_CYLINDER":
            r = int(input("ENTER THE RADIUS:"))
            h = int(input("ENTER THE HEIGHT:"))
            V = 3.141592653589793238*(r**2)*h
            print("THE VOLUME IS" + str(V))
        elif o == "PRISM":
            print("FOR SQUARE PRISM,BOTH LENGTH AND BREADTH ARE THE SAME.")
            l = int(input("ENTER THE LENGTH OF THE BASE:"))
            b = int(input("ENTER THE BREADTH OF THE BASE:"))
            h = int(input("ENTER THE HEIGHT OF THE PRISM:"))
            V = (l*b)*h
            print("THE VOULME IS:" + str(V))
        elif o == "RIGHT_RECTANGULAR/SQUARE_PYRAMID":
            print("FOR SQUARE PYRAMID, BOTH THE LENGTH BREADTH ARE THE SAME.")
            l = int(input("ENTER THE BASE LENGTH:"))
            b = int(input("ENTER THE BASE WIDTH:"))
            h = int(input("ENTER THE HEIGHT:"))
            V = (l*b)*h
            print("THE VOLUME IS:" + str(V))
        elif o == "ELLIPSOID":
            a = int(input("ENTER THE FIRST SEMI AXIS:"))
            b = int(input("ENTER THE SECOND SEMI AXIS:"))
            c = int(input("ENTER THE THIRD SEMI AXIS:"))
            V = (4/3)*3.141592653589793238*a*b*c
            print("THE VOLUME IS:" + str(V))
        elif o == "TETRAHEDRON":
            l = int(input("ENTER THE LENGTH OF THE EDGE:"))
            V = (l**3)/(6*(2)**(1/2))
            print("THE VOLUME IS:" + str(V))

elif E == "SOLVING_SYSTEM_OF_LINEAR_EQUATIONS_WITH_2_UNKNOWNS":
    from sympy.interactive import printing
    printing.init_printing(use_latex=True)
    from sympy import Eq, solve_linear_system, Matrix
    from numpy import linalg
    import numpy as np
    import sympy as sp
    eq1 = sp.Function('eq1')
    eq2 = sp.Function('eq2')
    x,y = sp.symbols('x y')
    print("ENTER THE INFORMATION ABOUT EQUATION I:")
    a = int(input("ENTER THE COEFFICIENT OF x:"))
    b = int(input("ENTER THE COEFFICIENT OF y:"))
    c = int(input("ENTER THE NUMBER AFTER EQUALS TO SIGN (THE CONSTANT TERM):"))
    eq1 = Eq(a*x+b*y,c)
    display(eq1)
    print("ENTER THE INFORMATION ABOUT EQUATION II:")
    a1 = int(input("ENTER THE COEFFICIENT OF x:"))
    b1 = int(input("ENTER THE COEFFICIENT OF y:"))
    c1 = int(input("ENTER THE NUMBER AFTER EQUALS TO SIGN (THE CONSTANT TERM):"))
    eq2 = Eq(a1*x+b1*y,c1)
    display(eq2)
    row1 = [a,b,c]
    row2 = [a1,b1,c1]
    system = Matrix((row1,row2))
    display(solve_linear_system(system,x,y))

elif E == "BASE_CONVERSION":
    def take_inputs():
    while True:
        # input for initial base
        init_base = input("INITIAL BASE (BETWEEN 2 AND 36): ")
        if init_base.isdigit() == True:
            init_base = int(init_base)
            if init_base >= 2 and init_base <= 36:
                break
        print("INVALD INPUT")
    while True:
        #input for initial number
        init_num = input("NUMBER: ")
        if init_num.isalnum() == True:
            init_numl = [char for char in init_num]
            # checking if the number in that base is valid
            error = 0
            for i in range(len(init_numl)):
                if init_numl[i].isalpha() == True:
                    init_numl[i] = ord(init_numl[i].upper()) - 55
                else:
                    init_numl[i] = int(init_numl[i])
                if init_numl[i] >= init_base:
                    error += 1
            if error == 0:
                break
        print("INVAID INPUT")
    while True:
        conv_base = input("CONVERT TO BASE (BETWEEN 2 AND 36): ")
        if conv_base.isdigit() == True:
            conv_base = int(conv_base)
            if conv_base >= 2 and conv_base <= 36:
                input_error = 0
                return_t = init_base, init_numl, conv_base
                return return_t
        print("INVALID INPUT")

# converting bases

    def conv_base(ibase, inuml, cbase):
    # first conv to base10
        inuml.reverse()
        base10 = 0
        for i in range(len(inuml)):
            base10 += inuml[i] * ibase ** i
    # next conv base10 to cbase
        cnuml = []
        while base10 != 0:
            cnuml.append(base10 % cbase)
            base10 = base10 // cbase
        cnuml.reverse()
        for i in range(len(cnuml)):
            if cnuml[i] > 9:
                cnuml[i] = chr(cnuml[i] + 55)
            else:
                cnuml[i] = str(cnuml[i])
        conv_num = "".join(cnuml)
        if sum(inuml) == 0:
            conv_num = 0
        print(f"CONVERTED TO: {conv_num}")

ti = take_inputs()
conv_base(ti[0], ti[1], ti[2])
elif E == "NUMBER_THEORETIC_FUNCTIONS":
    print("WE HAVE THE OPTION OF TWO NUMBER THEORETIC FUNCTIONS, THE SIGMA FUNCTION (SUM OF ALL POSITIVE DIVISORS OF A NUMBER) AND THE TAO FUNCTION (PRODUCT OF ALL POSITIVE DIVISORS OF A NUMBER).")
    list = []
    def primeFactors(n):
        while n%2 == 0:
            list.append(2),
            n = n/2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                list.append(i),
                n = n/i
        if n>2:
            list.append(n)
    print(list)

elif E == "MiniCalc":
    import tkinter as tk
    from tkinter import *
    from math import *

    def evaluate(event):
        res.configure(text = "Result: " + str(eval(entry.get())))

    w = tk.Tk()
    tk.Label(w, text="Your Expression:").pack()
    entry = tk.Entry(w)
    entry.bind("<Return>", evaluate)
    entry.pack()
    res = tk.Label(w)
    res.pack()
    w.mainloop()

elif E == "MATRIX_OPERATIONS":
    


elif E == "MEANS":
    import winsound
    winsound.Beep(1000,100)
    print("\nARITHMETIC_MEAN\nGEOMETRIC_MEAN\nHARMONIC_MEAN:")
    a = input("WHAT TYPE OF MEAN DO YOU WANT TO CALCULATE")
    import statistics
    import numpy
    if a == "ARITHMETIC_MEAN":
      x = input("ENTER THE VALUES:")
      x = []
      print(statistics.mean(x))
elif E == "FUN_ZONE":
    import winsound
    winsound.Beep(1000,100)
    print("WELCOME TO THE FUN ZONE OF PyCalc. HERE YOU CAN DRAW DIFFERENT 3-D AND 2-D SHAPES OF DIFFERENT DIMENAIONS AND ALSO USE OUR PyCalc App.")
    a_t = input("WHAT DO YOU WANT TO CHOOSE(\nDRAW\nWORD_CLOUD\nPyCalc MATH CHALLENGE):")

    if a_t == "DRAW":
        import winsound
        winsound.Beep(1000,100)
        a_m = input("PLEASE ENTER THE DIMENSION(2-D/3-D):")
        if a_m == "2-D":
            import winsound
            winsound.Beep(1000,100)
            a_yo=input("WHICH SHAPE?(SQUARES/RECTANGLES/POLYGONS):")
            import winsound
            winsound.Beep(1000,100)
            if a_yo == "SQUARE":
                import winsound
                winsound.Beep(1000,100)
                a_oy=int(input("ENTER THE SIDE LENGTH:"))
                import winsound
                winsound.Beep(1000,100)
                import turtle
                pd=turtle.Screen()
                pd=turtle.Turtle()
                for i in range (5):
                    pd.forward(a_oy)
                    pd.left(90)
            elif a_yo == "RECTANGLE":
                import winsound
                winsound.Beep(1000,100)
                a_oy=int(input("ENTER THE LENGTH:"))
                a_ot=int(input("ENTER THE BREADTH:"))
                import turtle
                pd=turtle.Screen()
                pd=turtle.Turtle()
                pd.forward(a_oy)
                pd.left(90)
                pd.forward(a_ot)
                pd.left(90)
                pd.forward(a_oy)
                pd.left(90)
                pd.forward(a_ot)
            elif a_yo == "POLYGONS":
                import winsound
                winsound.Beep(1000,100)
                tess = int(input("ENTER THE NUMBER OF SIDES OF THE POLYGON:"))
                l_en = int(input("ENTER THE LENGTH OF EACH SIDE:"))
                cd = ((tess-2)*180)/tess
                sa = 180-cd
                import turtle
                fg = turtle.Screen()
                fg = turtle.Turtle()
                for i in range(tess+1):
                    fg.forward(l_en)
                    fg.left(sa)
            else:
                import winsound
                winsound.Beep(1000,100)
                print("INVALID")
        elif a_m == "3-D":
            import winsound
            winsound.Beep(1000,100)
            a_op = input("WHICH SHAPE?(CUBE(for now!)):")
            import winsound
            winsound.Beep(1000,100)
            if a_op == "CUBE":
                import winsound
                winsound.Beep(1000,100)
                pid = int(input("ENTER THE SIDE LENGTH:"))
                import turtle
                pd=turtle.Screen()
                pd=turtle.Turtle()
                for i in range (5):
                  pd.forward(pid)
                  pd.left(90)
                  i=i+1
                pd.right(45)
                pd.forward(pid)
                pd.left(45)
                pd.left(90)
                pd.forward(pid)
                pd.left(45)
                pd.forward(pid)
                pd.right(45)
                pd.right(90)
                pd.forward(pid)
                pd.right(45)
                pd.forward(pid)
                pd.right(45)
                pd.forward(pid)
                pd.right(90)
                pd.right(45)
                pd.forward(pid)
                pd.right(180)
                pd.forward(pid)
                pd.right(135)
                pd.forward(pid)
                pd.right(90)
                pd.forward(pid)
                pd.right(90)
                pd.forward(pid)


            else:
                import winsound
                winsound.Beep(1000,100)
                print("INVALID")

    elif a_t == "WORD_CLOUD":
        # Import packages
        import matplotlib.pyplot as plt
        #%matplotlib inline
        # Define a function to plot word cloud
        def plot_cloud(wordcloud):
        # Set figure size
         plt.figure(figsize=(40, 30))
        # Display image
         plt.imshow(wordcloud)
        # No axis details
         plt.axis("off");
        # Import package
        from wordcloud import WordCloud, STOPWORDS
        # Generate word cloud
        #wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate('text')
        # Plot
        #plot_cloud(wordcloud)

        # Generate wordcloud
        text = input("ENTER THE TEXT:")
        wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(text)
        # Plot
        plot_cloud(wordcloud)
        wordcloud.to_file("wordcloud.png")
        print("PLEASE TYPE IN THE SEARCH BAR, THE WORD WORDCLOUD.YOU WILL FIND THE FILE SAVED AS wordcloud.png")
    elif a_t == "PyCalc MATH CHALLENGE":
        import time
        import random
        import functools
        import operator
        import math
        print("WELCOME TO PyCalc MATH CHALLENGE")
        time.sleep(2)
        print("YOU HAVE TO ANSWER THE QUESTIONS BEFORE TIME RUNS OUT!")
        print("MARKING SCHEME: +5 POINTS FOR CORRECT ANSWER, 0 FOR WRONG ANSWER")
        time.sleep(3)
        print("READY FOR THE CHALLENGE? GO!")
        start_time = time.time()
        s = []
        print("Moor and Nick are running in a race. They start running at the same time from the same place in a straight line in the same direction, and both run at their own constant pace. When Moor is 100m from the starting point, Nick is 20 meters behind Moor. When Nick is 100 meters from the starting point , how far behind Moor is Nick in meters?") #question
        a1 = int(input("ENTER YOUR ANSWER:"))
        if a1 == 25:
          s.append(5)
        time.sleep(2)
        print("Let x be chosen uniformly at random from the set {1,2,3,...,100}. The probability tha x^2-95x+1500 < 0 can be expressed as a common fraction m/n, where m and n are relatively prime positive integers. Compute m + n? ")#question
        a1 = int(input("ENTER YOUR ANSWER:"))
        if a1 == 77:
          s.append(5)


er = input("DID YOU FACE ANY PROBLEM?(TYPE YES/NO):")
if er == "YES":
   print("FOR PROVIDING YOU THE REQUIRED SUPPORT, WE HAVE CHATBOT TO ASSIST YOU!")
   import tkinter
   from tkinter import *
   from random import choice

   ask   = ["I am having problem in operating the calculator",""]
   error = ["Please join our discord server and post your problem there. Invite link:https://discord.gg/KkQe48XybC" ]

   root = Tk()
   user = StringVar()
   bot  = StringVar()

   root.title("PyCalc APP BOT")
   Label(root, text=" user : ").pack(side=LEFT)
   Entry(root, textvariable=user).pack(side=LEFT)
   Label(root, text=" Bot  : ").pack(side=LEFT)
   Entry(root, textvariable=bot).pack(side=LEFT)



   def main():
       question = user.get()
       if question in ask:
             bot.set(choice(hi))
       else:
             bot.set(choice(error))

   Button(root, text="ENTER", command=main).pack(side=LEFT)

   mainloop()

   import winsound
   winsound.Beep(1000,100)
   import smtplib
   s = input("PLEASE ENTER YOUR NAME:")
   sender_email = "pythoncalc096@gmail.com"
   receiver_email = input("PLEASE ENTER YOUR EMAIL ADDRESS:")
   password = "pycalc2023"
   message = """
   Dear  {},

   Thank you for using PyCalc. Please share your feedback and experience by filling out the google form.
   Share this with your friends and family members so that they can also take benifit of this calculator. We will be adding more operations to it soon.
   We will keep you updated via email.
   Please fill out the google form:https://docs.google.com/forms/d/e/1FAIpQLScm-4xrSwI4FbetEitzBF2kd2tQgiNOlEhkfiC_lrVRQ4cVdQ/viewform?usp=sf_link
   Also please join our discord server: https://discord.gg/uhK3ptyuXZ for more updates about the versions of PyCalc. We are also providing Python classes, taught by expert coders in this server.

   REGARDS,
   Team PyCalc

   https://drive.google.com/file/d/1jrgAlfnncYNar8B3THEWRak38OMA_019/view?usp=sharing
   """.format(s)
   import socket
   socket.getaddrinfo('localhost', 8080)
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(sender_email, password)
   print("SUCCESSFUL LOGIN")
   server.sendmail(sender_email, receiver_email, message)
   print("CHECK YOUR INBOX")

elif er == "NO":
   print("TO KEEP YOU UPDATED, PLEASE ENTER YOUR INFORMATION. ALSO JOIN OUR DISCORD SERVER, INVITE LINK:https://discord.gg/mAA6vWuf")
   import winsound
   winsound.Beep(1000,100)
   import smtplib
   s = input("PLEASE ENTER YOUR NAME:")
   sender_email = "pythoncalc096@gmail.com"
   receiver_email = input("PLEASE ENTER YOUR EMAIL ADDRESS:")
   password = "pycalc2023"
   message = """
   Dear  {},

   Thank you for using PyCalc. Please share your feedback and experience by filling out the google form.
   Share this with your friends and family members so that they can also take benifit of this calculator. We will be adding more operations to it soon.
   We will keep you updated via email.
   Please fill out the google form:https://docs.google.com/forms/d/e/1FAIpQLScm-4xrSwI4FbetEitzBF2kd2tQgiNOlEhkfiC_lrVRQ4cVdQ/viewform?usp=sf_link
   Also please join our discord server: https://discord.gg/uhK3ptyuXZ for more updates about the versions of PyCalc. We are also providing Python classes, taught by expert coders in this server.

   REGARDS,
   Team PyCalc

   https://drive.google.com/file/d/1jrgAlfnncYNar8B3THEWRak38OMA_019/view?usp=sharing
   """.format(s)
   import socket
   socket.getaddrinfo('localhost', 8080)
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(sender_email, password)
   print("SUCCESSFUL LOGIN")
   server.sendmail(sender_email, receiver_email, message)
   print("CHECK YOUR INBOX")
   
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500   
    
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]    
