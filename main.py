import seaborn
import pandas as pd
import csv
import numpy as np
from tkinter import  *
from tkinter import  messagebox
from matplotlib import pyplot as plt
from PIL import ImageTk, Image

#criar a janela
root = Tk()
root.title('')
#root.config(background='black')
root.geometry('900x500')
root.resizable(False, False)

#variaveis dos widgets
day = StringVar()
month = StringVar()
year = StringVar()
mood = IntVar()
#mood2 = IntVar()
#mood3 = IntVar()

#variaveis e listas globais e tambem caminhos
imgMood1 = ImageTk.PhotoImage(Image.open("/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/mood1.gif"))
imgMood2 = ImageTk.PhotoImage(Image.open("/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/mood2.gif"))
imgMood3 = ImageTk.PhotoImage(Image.open("/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/mood3.gif"))

dayList = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20', '21','22','23', '24','25', '26', '27', '28', '29', '30', '31']
monthList = ['March', 'April', 'May','June', 'July']
yearList =  ['2020', '2021']

""""""""""""
#+++espaco de dedicado a criacao das funcoes+++
def storeData():
    usermoodChoice =  mood.get()
    userdayChoice = day.get()
    usermonthChoice = month.get()
    useryearChoice = year.get()
    with open('/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/data.csv', 'a') as csvfile:
        saveOnCsv = csv.writer(csvfile)
        saveOnCsv.writerow([usermoodChoice,userdayChoice,usermonthChoice,useryearChoice])
    csvfile.close()
    #messagebox.showinfo( ' ','Mood stored, thank you!', command=messagebox.destroy)
    return print("Stored: " + str(usermoodChoice)  + " on day "+ str(userdayChoice) + ' of ' + str(usermonthChoice) + ' of ' + str(useryearChoice))
    
    
def createPlotGraph():
    csvData = pd.read_csv('/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/data.csv')
    moodData = csvData['mood']
    dayData = csvData['day']
    monthData = csvData['month']
    moodMean = np.average(moodData)
    plt.plot(dayData,moodData)
    #plt.axvline(moodMean, color='r', linestyle='solid', linewidth=2, label="Mean")
    plt.axhline(moodMean, color='b', linestyle='solid', linewidth=2, label="Mean")
    plt.legend()
    plt.title("Mood Evolution")
    plt.xlabel('Day')
    plt.ylabel('Mood')
    plt.show()
    #print(moodData)
    return print("Graph created")

#definicao dos GUI widgets
labelAppName = Label(root, text='isolamento mood tracker', font=('Lucida Grande', 24)).place(x=300, y=0)

imgMood1GridPlace = Label(root, image = imgMood1)
imgMood2GridPlace = Label(root, image = imgMood2)
imgMood3GridPlace = Label(root, image = imgMood3)

imgMood1GridPlace.place(x=0,y=43)
imgMood2GridPlace.place(x=300,y=43)
imgMood3GridPlace.place(x=600,y=43)

rButtonMood1 = Radiobutton(root, variable = mood, value=1).place(x=135, y=320)
rButtonMood2 = Radiobutton(root, variable = mood, value=2).place(x=425,y=320)
rButtonMood3 = Radiobutton(root, variable = mood, value=3).place(x=735, y=320) 

dayDroplist = OptionMenu(root, day, *dayList)
dayDroplist.place(x = 316, y = 400)
dayDroplist.configure(padx=12)
day.set('Day')

monthDroplist = OptionMenu(root, month, *monthList)
monthDroplist.place(x = 410, y = 400)
monthDroplist.configure(padx=12)
month.set('Month')

yearDroplist = OptionMenu(root, year, *yearList)
yearDroplist.place(x = 510, y = 400)
yearDroplist.configure(padx=12)
year.set('Year')

labelReport = Label(root, text = "Report Commands").place(x=0, y=450)
storeButton = Button(root, text = "Save", command=storeData).place(x = 830, y = 450)
plotButton = Button(root, text= "Graph", command=createPlotGraph).place(x = 0, y=470)
root = mainloop()
