from tkinter import *
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
    text = readLocalFile(f'Cement_Calc_Config.csv')

    result = []

    for line in text.splitlines():
        result.append(line.split(",")[1])

    return result


def saveConfig(values):
    arr = []
    for idx, v in enumerate(values):
        arr.append(f'{varArr[idx]},{v}')

    txt = '\n'.join(arr)
    writeLocalFile(f'Cement_Calc_Config.csv', txt)


def getInput():
    values = []
    for i, v in enumerate(myVars):
        if i <= 8:
            values.append(v.get())
        else:
            values.append(float(v.get()))
    saveConfig(values)
    calcResult = makeCalculation(values)
    saveStatusVar.set(calcResult)
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

########""" GUI """########


root = Tk()
saveStatusVar = StringVar(root, '')

myVars = []
myEntry = []
for i in range(len(varArr)):
    label = Label(root, text=myLabel[i],
                  background='#06283D', foreground='#DFF6FF')
    xPlace = 10 if i <= 5 else (10 if i <= 12 else (290 if i <= 19 else 570))
    yPlace = i*40 if i <= 5 else (i*40 if i <=
                                  12 else ((i-7)*40 if i <= 19 else (i-14)*40))
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

    xPlace = 180 if i <= 5 else (180 if i <= 12 else (460 if i <= 19 else 740))
    # yPlace = i*40 if i <= 10 else (i-11)*40
    wPlace = 380 if i <= 5 else 100
    entry.place(x=xPlace, y=yPlace, width=wPlace, height=35)

    if i == 0 or i == 2 or i == 4:
        var.trace('w', lambda var, index, mode,
                  idx=i, varia=var: updateOptions(idx, varia))
    else:
        var.trace('w', lambda var, index, mode,
                  sv=saveStatusVar: clearSaveStatusVar(sv))

result = getCSVData() if os.path.exists(
    'Cement_Calc_Config.csv') else ['' for i in range(len(varArr))]

for i, v in enumerate(myVars):
    if (i == 0 or i == 2 or i == 4) and result[i] == '':
        v.set('')
    else:
        v.set(result[i])

saveStatusVar.set('Started')

saveStatus = Label(root, textvariable=saveStatusVar,
                   background='#06283D', foreground='#DFF6FF')
saveStatus.place(x=570, y=5, width=270, height=225)

calculateBtn = Button(root, text="Calculate", background='#06283D',
                      foreground='#DFF6FF', borderwidth=2, relief="groove",
                      padx=5, pady=5, command=getInput)
calculateBtn.place(x=325, y=600, width=200, height=35)

root.title('Cement_Calculation')
root.geometry('850x640')
root.configure(bg='#000')

root.resizable(False, False)
# Setting icon of master window
# root.iconbitmap(resource_path('Cement_Calculation.ico'))
# Start program
root.mainloop()
