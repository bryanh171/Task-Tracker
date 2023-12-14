from tkinter import *
import tkinter as window

root = window.Tk()
f= open("savefile.txt","a+")
root.geometry('1100x700')
root.title('Application Helper')

def save():
    data = [fnEntry.get() for entries in saveFile]
    for i in saveFile:
        f.write(fnEntry.get())

   ## for i in entries:
    #    for x in f:
    #        if f[x] == "":
    #            f[x].write(fnEntry.get)
    ##        else:
   ###             f[x] == 0

for i in range(12):
    fnLabel = window.Label(root, text = entries[i], font=('calibre',10, 'bold'), anchor="w", width=20)
    fnEntry = window.Entry(root,textvariable = saveFile[i], font=('calibre',10,'normal'))
    fnCopy = Button(root, text = 'Copy', bd = '5', command = root.destroy)
    fnLabel.grid(row=i, column=0, padx=10, pady=10)
    fnEntry.grid(row=i, column=1, padx=10, pady=10)
    fnCopy.grid(row=i, column=2, padx=10, pady=10)

entryList = []
saveFile = []
for i in fnEntry():
    saveFile.append(fnEntry[i])
entries = ["First name", "Last Name", "Email", "Phone Number", "Address", "City", "State", "Zip Code", "Institution", "Degree", "Work Title", "Work Description"]

#First Name entry and label initialize 


    

#Submit Button
fnButton = Button(root, text = 'Save Changes', bd = '5', command = save)
fnButton.grid(row=i+1, column=1, padx=10, pady=10)

root.mainloop()

print(saveFile)


f= open("savefile.txt","w+")