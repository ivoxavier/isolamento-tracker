import seaborn
from tkinter import  *
from matplotlib import pyplot as plt

#criar a janela
root = Tk()
root.title('')
#root.config(background='black')
#root.geometry('1024x800')

#variaveis dos widgets
day = StringVar()
month = StringVar()
year = StringVar()

#variaveis e listas globais
dayList = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20', '21','22','23', '24','25', '26', '27', '28', '29', '30', '31']
monthList = ['March', 'April', 'May','June', 'July']
yearList =  ['2020', '2021']

test = 'hell'
#definicao dos GUI widgets
labelAppName = Label(root, text='isolamento tracker', font=('Lucida Grande', 24)).grid(row=0, column=2)

labelDate = Label(root, text='Dia').grid(row=1, column=0)
dayDroplist = OptionMenu(root, day, *dayList)
dayDroplist.grid(row=1, column=1)


labelMonth = Label(root, text='Mês').grid(row=1, column=3)
monthDroplist = OptionMenu(root, month, *monthList)
monthDroplist.grid(row=1, column=4)

labelYear = Label(root, text='Ano').grid(row=1, column=5)
yearDroplist = OptionMenu(root, year, *yearList)
yearDroplist.grid(row=1, column=6)

root.grid()
root = mainloop()