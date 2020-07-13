import tkinter as tk

root = tk.Tk()
s1 = ""
s2 = ""
operation = None

def fDelete():
    global s1,s2,operation
    if operation:
        if len(s2):
            s2 = s2[:len(s2) - 1]
        res.delete(0,tk.END)
        res.insert(0,s2)
    else:
        if len(s1):
            s1 = s1[:len(s1) - 1]
        res.delete(0,tk.END)
        res.insert(0,s1)


root.title("Calculator")
res = tk.Entry(root, bg = "green", fg = "white", width = 30, font = "44")
res.grid(row = 0, column = 0, columnspan = 3)

bDelete = tk.Button(root, text = "DEL", font = "44",width = 5, height = 3, command = fDelete)
bDelete.grid(row = 0, column = 3)

def ver(a):
    return (len(a) < 12)

tk.Label(root, text = " ").grid(row = 1)
tk.Label(root, text = " ").grid(row = 3)
tk.Label(root, text = " ").grid(row = 5)
tk.Label(root, text = " ").grid(row = 7)
tk.Label(root, text = " ").grid(row = 9)

def fClear():
    global s2,s1
    res.delete(0, tk.END)
    s1 = ""
    s2 = ""
    operation = None

def f1():
    global operation,s1,s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '1'
            res.delete(0, tk.END)
            res.insert(0,s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '1'
            res.delete(0, tk.END)
            res.insert(0,s1)

def f2():
    global operation, s1, s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '2'
            res.delete(0, tk.END)
            res.insert(0, s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '2'
            res.delete(0, tk.END)
            res.insert(0, s1)

def f0():
    global operation,s1,s2
    if operation:
        if ver(s2):
            if s2 == '0':
                return
            s2 += '0'
            res.delete(0, tk.END)
            res.insert(0,s2)
    else:
        if ver(s1):
            if s1 == '0':
                return
            s1 += '0'
            res.delete(0, tk.END)
            res.insert(0,s1)

def f3():
    global operation, s1, s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '3'
            res.delete(0, tk.END)
            res.insert(0, s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '3'
            res.delete(0, tk.END)
            res.insert(0, s1)

def f4():
    global operation,s1,s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '4'
            res.delete(0, tk.END)
            res.insert(0,s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '4'
            res.delete(0, tk.END)
            res.insert(0,s1)

def f5():
    global operation, s1, s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '5'
            res.delete(0, tk.END)
            res.insert(0, s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '5'
            res.delete(0, tk.END)
            res.insert(0, s1)

def f9():
    global operation,s1,s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '9'
            res.delete(0, tk.END)
            res.insert(0,s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '9'
            res.delete(0, tk.END)
            res.insert(0,s1)

def f8():
    global operation, s1, s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '8'
            res.delete(0, tk.END)
            res.insert(0, s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '8'
            res.delete(0, tk.END)
            res.insert(0, s1)

def f7():
    global operation,s1,s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '7'
            res.delete(0, tk.END)
            res.insert(0,s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '7'
            res.delete(0, tk.END)
            res.insert(0,s1)

def f6():
    global operation, s1, s2
    if operation:
        if ver(s2):
            if s2 == '0':
                s2 = ''
            s2 += '6'
            res.delete(0, tk.END)
            res.insert(0, s2)
    else:
        if ver(s1):
            if s1 == '0':
                s1 = ''
            s1 += '6'
            res.delete(0, tk.END)
            res.insert(0, s1)


def fEgal():
    global operation, s1, s2
    if operation:
        if s2:
            if operation == '+':
                s1 = str(float(s1) + float(s2))
            if operation == '-':
                s1 = str(float(s1) - float(s2))
            if operation == '*':
                s1 = str(float(s1) * float(s2))
            if operation == '/' and s2 != '0':
                s1 = str(float(s1) / float(s2))
    res.delete(0, tk.END)
    res.insert(0, s1)
    operation = None
    s2 = ''

def fPlus():
    global operation,s1, s2
    if operation:
        if s2:
            if operation == '+':
                s1 = str(float(s1) + float(s2))
            if operation == '-':
                s1 = str(float(s1)-float(s2))
            if operation == '*':
                s1 = str(float(s1)*float(s2))
            if operation == '/' and s2 != '0':
                s1 = str(float(s1)/float(s2))
    res.delete(0,tk.END)
    res.insert(0,s1)
    operation = '+'
    s2 = ''


def fOri():
    global operation,s1, s2
    if operation:
        if s2:
            if operation == '+':
                s1 = str(float(s1) + float(s2))
            if operation == '-':
                s1 = str(float(s1)-float(s2))
            if operation == '*':
                s1 = str(float(s1)*float(s2))
            if operation == '/' and s2 != '0':
                s1 = str(float(s1)/float(s2))
    res.delete(0,tk.END)
    res.insert(0,s1)
    operation = '*'
    s2 = ''

def fImp():
    global operation, s1, s2
    if operation:
        if s2:
            if operation == '+':
                s1 = str(float(s1) + float(s2))
            if operation == '-':
                s1 = str(float(s1) - float(s2))
            if operation == '*':
                s1 = str(float(s1) * float(s2))
            if operation == '/' and s2 != '0':
                s1 = str(float(s1) // float(s2))
    res.delete(0, tk.END)
    res.insert(0, s1)
    operation = '/'
    s2 = ''

def fMinus():
    global s2,s1,operation
    if operation:
        if s2 != '' and s2 != '0':
            s2 = str(-float(s2))
            res.delete(0, tk.END)
            res.insert(0, s2)
    else:
        if s1 != '' and s1 != '0':
            s1 = str(-float(s1))
            res.delete(0, tk.END)
            res.insert(0, s1)

b1 = tk.Button(root, text = " 1 ", width = 5, height = 3, font = "44 ", command = f1)
b1.grid(row = 2, column = 0)

b2 = tk.Button(root, text = " 2 ", width = 5, height = 3, font = "44 ", command = f2)
b2.grid(row = 2, column = 1)

b3 = tk.Button(root, text = " 3 ", width = 5, height = 3, font = "44 ", command = f3)
b3.grid(row = 2, column = 2)

b4 = tk.Button(root, text = " 4 ", width = 5, height = 3, font = "44 ", command = f4)
b4.grid(row = 4, column = 0)

b5 = tk.Button(root, text = " 5 ", width = 5, height = 3, font = "44 ", command = f5)
b5.grid(row = 4, column = 1)

b6 = tk.Button(root, text = " 6 ", width = 5, height = 3, font = "44 ", command = f6)
b6.grid(row = 4, column = 2)

b7 = tk.Button(root, text = " 7 ", width = 5, height = 3, font = "44 ", command = f7)
b7.grid(row = 6, column = 0)

b8 = tk.Button(root, text = " 8 ", width = 5, height = 3, font = "44 ", command = f8)
b8.grid(row = 6, column = 1)

b9 = tk.Button(root, text = " 9 ", width = 5, height = 3, font = "44 ", command = f9)
b9.grid(row = 6, column = 2)

b0 = tk.Button(root, text = " 0 ", width = 5, height = 3, font = "44 ", command = f0)
b0.grid(row = 6, column = 3)

bPlus = tk.Button(root, text = " + ", width = 5, height = 3, font = "44 ", command = fPlus)
bPlus.grid(row = 2, column = 3)

bMinus = tk.Button(root, text = " - ", width = 5, height = 3, font = "44 ", command = fMinus)
bMinus.grid(row = 4, column = 3)

bEgal = tk.Button(root, text = " = ", width = 5, height = 3, font = "44 ", command = fEgal)
bEgal.grid(row = 8, column = 3,rowspan = 2)

bOri = tk.Button(root, text = " * ", width = 5, height = 3, font = "44 ", command = fOri)
bOri.grid(row = 8, column = 0)

bImp = tk.Button(root, text = " / ", width = 5, height = 3, font = "44 ", command = fImp)
bImp.grid(row = 8, column = 1)

bClear = tk.Button(root, text = " clear ", width = 5, height = 3, font = "44 ", command = fClear)
bClear.grid(row = 8, column = 2)

root.mainloop()