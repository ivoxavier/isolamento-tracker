import seaborn
from tkinter import  *
from matplotlib import pyplot as plt
from PIL import ImageTk, Image


#criar a janela
root = Tk()
root.title('')
#root.config(background='black')
root.geometry('900x650')

#variaveis dos widgets
day = StringVar()
month = StringVar()
year = StringVar()
mood1 = IntVar()
mood2 = IntVar()
mood3 = IntVar()

#variaveis e listas globais e tambem caminhos
imgMood1 = ImageTk.PhotoImage(Image.open("/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/imgs/mood1.gif"))
imgMood2 = ImageTk.PhotoImage(Image.open("/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/imgs/mood2.gif"))
imgMood3 = ImageTk.PhotoImage(Image.open("/Users/ivo/Documents/isolamentoTracker/isolamento-tracker/imgs/mood3.gif"))

dayList = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20', '21','22','23', '24','25', '26', '27', '28', '29', '30', '31']
monthList = ['March', 'April', 'May','June', 'July']
yearList =  ['2020', '2021']

#definicao dos GUI widgets
labelAppName = Label(root, text='isolamento mood tracker', font=('Lucida Grande', 24)).grid(row=0, column=2, ipady=10)

imgMood1GridPlace = Label(root, image = imgMood1)
imgMood2GridPlace = Label(root, image = imgMood2)
imgMood3GridPlace = Label(root, image = imgMood3)

imgMood1GridPlace.grid(row=2,column=1, pady=5, padx=5)
imgMood2GridPlace.grid(row=2,column=2, pady=5, padx=5)
imgMood3GridPlace.grid(row=2,column=3, pady=5, padx=5)

rButtonMood1 = Radiobutton(root, variable = mood1, value=1).grid(row=3, column=1) 
rButtonMood2 = Radiobutton(root, variable = mood2, value=2).grid(row=3, column=2) 
rButtonMood3 = Radiobutton(root, variable = mood3, value=3).grid(row=3, column=3) 

#labelDate = Label(root, text='Dia').grid(row=1, column=0) / se o day.set('Dia') nao der resultado uncomment this line
dayDroplist = OptionMenu(root, day, *dayList)
dayDroplist.grid(row=4, column=1, ipady=50)
day.set('Day')

#labelMonth = Label(root, text='Mês').grid(row=1, column=3) / ver comentario acima
monthDroplist = OptionMenu(root, month, *monthList)
monthDroplist.grid(row=4, column=2, ipadx=9, ipady=50)
month.set('Month')

#labelYear = Label(root, text='Ano').grid(row=1, column=5) / ver comentarios acima
yearDroplist = OptionMenu(root, year, *yearList)
yearDroplist.grid(row=4, column=3, ipadx=6, ipady=50)
year.set('Year')

storeButton = Button(root, text="Save").grid(row=5, column=1, ipady=100)
reportButton = Button(root, text="Report").grid(row=5, column=3)
root = mainloop()
