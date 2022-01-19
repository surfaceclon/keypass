from tkinter import *
import shelve
import os

paths = 'Your path'

def child_window():
    child = Toplevel(root)
    #child.overrideredirect(1)
    child['bg'] = '#696969'
    child.title('SETINGS DB')
    child.geometry('550x345')
    child.resizable(width=False, height=False)

    def create_db(event):
        cr_db = setEnt.get()
        key_db = keyEnt.get()
        val_db = valEnt.get()
        with shelve.open(paths + cr_db) as cr_file:
            cr_file[key_db] = val_db + '\n'
            cr_file.close()
        with open(paths + 'val' + cr_db + '.txt', 'a') as val_file:
            val_file.write(key_db + '\n')
        infoLab = Label(child, text='CREATED ' + cr_db, font=('Bold', 14), bg='#696969')
        infoLab.place(x=50, y=50)
        keyEnt.delete(0, END)
        valEnt.delete(0, END)

    def delete_db(*args):
        try:
            de_db = setEnt.get()
            os.remove(paths +  de_db + '.bak')
            os.remove(paths +  de_db + '.dat')
            os.remove(paths +  de_db + '.dir')
            os.remove(paths +  'val' + de_db + '.txt')
            infoLab = Label(child, text='DELETED ' + de_db, font=('Bold', 14), bg='#696969')
            infoLab.place(x=50, y=50)
            setEnt.delete(0, END)
        except:
            pass

    setValuesFrame = Frame(child, bg='#696969')
    setValuesFrame.place(x=10, y=120) 

    setEnt = Entry(setValuesFrame, width=50, bg='#A9A9A9')
    setEnt.pack()
    dialogSet = Label(setValuesFrame, text='NAME FILE', font=('Bold', 7), bg='#696969')
    dialogSet.pack()

    keyEnt = Entry(setValuesFrame, width=50, bg='#A9A9A9')
    keyEnt.pack()
    dialogKey = Label(setValuesFrame, text='NAME KEY', font=('Bold', 7), bg='#696969')
    dialogKey.pack()

    valEnt = Entry(setValuesFrame, width=50, bg='#A9A9A9')
    valEnt.pack()
    dialogVal = Label(setValuesFrame, text='VALUE', font=('Bold', 7), bg='#696969')
    dialogVal.pack()

    setBut = Frame(child)
    setBut.place(x=10, y=250)

    butCreate = Button(setBut, text='CREATE', height=1, width=15, bg='#696969')
    butCreate.pack()
    butCreate.bind("<Button-1>", create_db)

    butDelete = Button(setBut, text='DELETE', height=1, width=15, bg='#696969', command=delete_db)
    butDelete.pack()


def get_values(*args):
    try:
        s = leftEntry.get()
        vals = []
        valsend = []
        with open(paths +  'val'+ s +'.txt') as val:
            for item in val:
                vals.append(item[:-1])
        
            with shelve.open(paths +  s) as db:
                for ico in vals:
                    stat = ico + ': ' + db[ico]
                    valsend.append(stat)
        
                topText.delete(1.0, END)
                topText.insert(END, valsend)
    except:
        topText.delete(1.0, END)
        topText.insert(END, 'SELECT NOT FILE')

def show_dir():
    while True:
        for s_db in os.listdir(paths):
            show_f = Label(inLeftFrame, text=s_db[:-4], font=('Bold', 15), bg='#F0FFFF')
            show_f.pack()

root = Tk()
#root.overrideredirect(1)
root['bg'] = '#696969'
root.geometry('860x560')
root.title('DABPAS')
root.resizable(width=False, height=False)

leftFrame = Frame(root, height=473, width=200, bg='#808080')
leftFrame.place(x=5, y=75)

inLeftFrame = Frame(leftFrame, height=400, width=190, bg='#808080')
inLeftFrame.place(x=30, y=70)

if not os.path.isdir(paths):
        os.mkdir(paths)


def update_dir(*args):
    try:
        for s_db in os.listdir(paths):
            show_f = Label(inLeftFrame, text=s_db[:-4], font=('Helvetica', 15), bg='#808080')
            show_f.pack()
    except:
        show_f = Label(inLeftFrame, text='NO FILE', font=('Helvetica', 15), bg='#808080')
        show_f.pack()

leftEntry = Entry(leftFrame, width=30, bg='#A9A9A9')
leftEntry.place(x=5, y=10)

ButtonFile = Button(leftFrame, text='GET', height=1, width=12, bg='#696969', command=get_values)
ButtonFile.place(x=100, y=35)

ButtonFileUpdate = Button(leftFrame, text='UPDATE', height=1, width=12, bg='#696969', command=update_dir)
ButtonFileUpdate.place(x=4, y=35)

ButtonSetings = Button(root, text='SETINGS DB', height=1, width=15, bg='#696969',command=child_window)
ButtonSetings.place(x=693, y=45)

topText = Text(root, height=26, width=65, font="12", bg='#A9A9A9',wrap=WORD)
topText.place(x=220, y=78)

root.mainloop()