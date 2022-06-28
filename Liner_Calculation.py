from tkinter import *
from tkinter import messagebox
import os
import sys
import datetime
from Calculation import makeCalculation
from Options import options, varArr, myLabel, csg

try:
    import pyi_splash  # type: ignore
    pyi_splash.close()
except:
    pass


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, 'src\\', relative_path)


def getTimeNowText():
    time = datetime.datetime.now()
    return f'{time.hour}_{time.minute}_{time.second}'


def readLocalFile(filename):
    f = open(filename, 'r')
    txt = f.read()
    f.close()

    return txt


def writeLocalFile(filename, txt):
    f = open(filename, 'w')
    f.write(txt)
    f.close()


def getCSVData():
    text = readLocalFile(f'Liner_Calc_Config.csv')

    result = []

    for line in text.splitlines():
        result.append(line.split(",")[1])

    return result


def saveConfig(values):
    arr = []
    for idx, v in enumerate(values):
        arr.append(f'{varArr[idx]},{v}')

    txt = '\n'.join(arr)
    writeLocalFile(f'Liner_Calc_Config.csv', txt)


def getInput():
    values = []
    for i, v in enumerate(myVars):
        if (i not in [2, 3, 7, 9, 10]) and v.get() == '':
            messagebox.showerror(
                'Error', f'This field [{myLabel[i]}] cant be empty')
            return
        if i <= 8:
            values.append(v.get())
        else:
            if v.get() == '':
                v.set(0)
            values.append(float(v.get()))
    saveConfig(values)
    calcResult = makeCalculation(values)
    for i, x in enumerate(calcResult.keys()):
        l = Label(root, text=x, background='#06283D', foreground='#EC994B')
        xPlace = 10 if i <= 2 else 290
        yPlace = (i*30)+505 if i <= 2 else (i*30)+415
        l.place(x=xPlace, y=yPlace, width=160, height=25)
        e = Entry(root, background='#06283D', justify=CENTER,
                  foreground='#EC994B', font=('Arial', 15, 'bold'))
        xPlace = 180 if i <= 2 else 460
        e.place(x=xPlace, y=yPlace, width=100, height=25)
        e.insert(END, calcResult[x])
        myResultsLabelsEntry.append(l)
        myResultsLabelsEntry.append(e)

    saveStatusVar.set('Result')
    return values


def updateOptions(i, var):
    if len(myVars) > 5 and len(myEntry) > 5:
        sizesOptions = [i['grd'] for i in csg[var.get()]]
        myVars[i+1].set(sizesOptions[0])
        menu = myEntry[i+1]['menu']
        menu.delete(0, 'end')
        for size in sizesOptions:
            menu.add_command(
                label=size, command=lambda size=size: myVars[i+1].set(size))
        if var.get() == '':
            myEntry[i+1].config(state="disabled")
        else:
            myEntry[i+1].config(state="normal")


def clearSaveStatusVar(saveStatusVar):
    saveStatusVar.set('')
    for x in myResultsLabelsEntry:
        x.destroy()

########""" GUI """########


root = Tk()
saveStatusVar = StringVar(root, '')
global myResultsLabelsEntry
myResultsLabelsEntry = []

myVars = []
myEntry = []
for i in range(len(varArr)):
    label = Label(root, text=myLabel[i],
                  background='#06283D', foreground='#DFF6FF')
    xPlace = 10 if i <= 5 else (10 if i <= 11 else 290)
    yPlace = i*40 if i <= 5 else (i*40 if i <= 11 else (i-6)*40)
    label.place(x=xPlace, y=yPlace, width=160, height=35)

    var = StringVar(root, value='')

    myVars.append(var)
    if i == 0 or i == 2 or i == 4:
        entry = OptionMenu(root, myVars[i], *csg.keys())
    elif i == 1 or i == 3 or i == 5:
        entry = OptionMenu(root, myVars[i], '')
    elif i == 6 or i == 7 or i == 8:
        entry = OptionMenu(root, myVars[i], *options[varArr[i]])
    else:
        entry = Entry(root, textvariable=myVars[i], background='#fff', borderwidth=2,
                      relief="ridge", font=('Arial', 12, 'bold'))
    myEntry.append(entry)

    xPlace = 180 if i <= 5 else (180 if i <= 11 else 460)
    wPlace = 380 if i <= 5 else 100
    entry.place(x=xPlace, y=yPlace, width=wPlace, height=35)

    if i == 0 or i == 2 or i == 4:
        var.trace('w', lambda var, index, mode,
                  idx=i, varia=var: updateOptions(idx, varia))
    else:
        var.trace('w', lambda var, index, mode,
                  sv=saveStatusVar: clearSaveStatusVar(sv))

result = getCSVData() if os.path.exists(
    'Liner_Calc_Config.csv') else ['' for i in range(len(varArr))]

for i, v in enumerate(myVars):
    if (i == 0 or i == 2 or i == 4) and result[i] == '':
        v.set('')
    else:
        v.set(result[i])

saveStatusVar.set('Started')

saveStatus = Label(root, textvariable=saveStatusVar,
                   background='#06283D', foreground='#DFF6FF')
saveStatus.place(x=10, y=480, width=550, height=20)

calculateBtn = Button(root, text="Calculate", background='#06283D',
                      foreground='#EC994B', borderwidth=2, relief="groove",
                      padx=5, pady=5, command=getInput)
calculateBtn.place(x=290, y=440, width=270, height=35)

root.title('Liner_Calculation')
root.geometry('570x600')
root.configure(bg='#000')

root.resizable(False, False)
# Setting icon of master window
root.iconbitmap(resource_path('Liner_Calculation.ico'))
# Start program
root.mainloop()
