from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox



def sort(txt_input, txt_input_number):
    for i in range(len(txt_input)-1 ):
        for j in range(len(txt_input) - i-1 ):
            if txt_input_number[j] <= txt_input_number[j + 1]:
                txt_input_number[j], txt_input_number[j + 1] = txt_input_number[j + 1], txt_input_number[j]
                temp_input=txt_input
                txt_input=txt_input.replace(txt_input[j],'$')
                txt_input=txt_input.replace(txt_input[j+1], '%')
                txt_input=txt_input.replace('$', str(temp_input[j+1]))
                txt_input=txt_input.replace('%', str(temp_input[j]))

    return txt_input, txt_input_number

def clicked():
    txt_original = txt.get("1.0", 'end-1c').lower()
    #alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    txt2.delete(1.0, END)
    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz '
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    alphabet=''
    for i in txt_original:
        if i!=' ':
            if eng_low_alphabet.find(i,0)!=-1:
                alphabet=eng_low_alphabet
                break
            elif rus_low_alphabet.find(i,0)!=-1:
                alphabet=rus_low_alphabet
                break
    if alphabet=='':
        temp_flag=1
        messagebox.showinfo('Ошибка!', f'Не удалось определить алфавит!')
    txt_input=''
    txt_input_number=[]
    for i in txt_original:
        if alphabet.find(i)!=-1:
            if txt_input.find(i)==-1:
                txt_input+=str(i)
                txt_input_number.append(1)
            else:
                txt_input_number[txt_input.find(i)]+=1
    txt_input, txt_input_number=sort(txt_input,txt_input_number)
    for i in range(len(txt_input)):
        txt3.insert(INSERT,f'{txt_input[i]}-{txt_input_number[i]/len(txt_original)}\n')
        txt_input_number[i]=txt_input_number[i]/len(txt_original)

def clicked2():
    txt_original = txt2.get("1.0", 'end-1c').lower()
    #alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    #txt2.delete(1.0, END)
    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz '
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    alphabet=''
    for i in txt_original:
        if i!=' ':
            if eng_low_alphabet.find(i,0)!=-1:
                alphabet=eng_low_alphabet
                break
            elif rus_low_alphabet.find(i,0)!=-1:
                alphabet=rus_low_alphabet
                break
    if alphabet=='':
        temp_flag=1
        messagebox.showinfo('Ошибка!', f'Не удалось определить алфавит!')
    txt_input=''
    txt_input_number=[]
    for i in txt_original:
        if alphabet.find(i)!=-1:
            if txt_input.find(i)==-1:
                txt_input+=str(i)
                txt_input_number.append(1)
            else:
                txt_input_number[txt_input.find(i)]+=1
    txt_input, txt_input_number=sort(txt_input,txt_input_number)
    for i in range(len(txt_input)):
        txt4.insert(INSERT,f'{txt_input[i]}-{txt_input_number[i]/len(txt_original)}\n')
        txt_input_number[i]=txt_input_number[i]/len(txt_original)


def histogramm():
    gist_input=txt3.get("1.0", 'end-1c').lower()
    part=gist_input.split('\n')
    a = []
    b = []
    for i in range(len(part)-1):
        inside_part=part[i].split('-')
        a.append(inside_part[0])
        b.append(float(inside_part[1]))
    plt.bar(a,b)
    plt.show()


def histogramm2():
    gist_input=txt4.get("1.0", 'end-1c').lower()
    part=gist_input.split('\n')
    a = []
    b = []
    for i in range(len(part)-1):
        inside_part=part[i].split('-')
        a.append(inside_part[0])
        b.append(float(inside_part[1]))
    plt.bar(a,b)
    plt.show()

def open_file():
    txt.delete(1.0, END)
    filename = askopenfilename()
    print(filename)
    with open(filename, "r", encoding='utf-8') as fin:
        for line in fin.readlines():
            txt.insert(INSERT, line)


def fixed():
    txt2.delete(1.0, END)
    txt_original = txt.get("1.0", 'end-1c').lower()
    txt_replace=txt5.get("1.0", 'end-1c').lower()
    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz '
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    #alphabet = ''
    for i in txt_original:
        if i != ' ':
            if eng_low_alphabet.find(i, 0) != -1:
                frequency_alphabet=[' ','e','t','a','o','n','i','s','r','h',
                                    'l','d','c','u','p','f','m','w','y',
                                    'b','g','v','k','q','x','j','z']
                txt_replace_part=txt_replace.split('\n')
                for i in range(len(txt_replace_part)-1):
                    frequency_alphabet[i]=txt_replace_part[i][2]
                print(frequency_alphabet)
                break
            elif rus_low_alphabet.find(i, 0) != -1:
                frequency_alphabet=[' ','о', 'е', 'а', 'и','н', 'т',
                                    'с','р','в','л','к','м','д','п','у',
                                    'я','ы','з','ъ','б','г','ч','й','х',
                                    'ж','ю','ш','ц','щ','э','ф','ь','ё',]
                txt_replace_part = txt_replace.split('\n')
                for i in range(len(txt_replace_part) - 1):
                    frequency_alphabet[i] = txt_replace_part[i][2]
                break
    #if alphabet == '':
    #    temp_flag = 1
     #   messagebox.showinfo('Ошибка!', f'Не удалось определить алфавит!')


    false_frequency_table = txt3.get("1.0", 'end-1c').lower()
    part = false_frequency_table.split('\n')
    false_letter = []
    false_frequency = []
    for i in range(len(part) - 1):
        inside_part = part[i].split('-')
        false_letter.append(inside_part[0])
        false_frequency.append(float(inside_part[1]))
    #print(false_letter)
    #print(frequency_alphabet)

    #print(len(false_letter), len(frequency_alphabet))
    count=0
    for i in false_letter:
        #print(f'Исправляю {i} на {chr(count)}')
        txt_original=txt_original.replace(i,chr(count))
        count+=1
    count=0
    for i in false_letter:
        if len(txt_replace)==0:
            txt5.insert(INSERT,f'{i}-{frequency_alphabet[count]}\n')
        txt_original=txt_original.replace(chr(count), frequency_alphabet[count])
        count+=1

    txt2.insert(INSERT, txt_original)




window = Tk()
window.title("Частотный криптоанализ")
window.geometry('1400x700')


lbl = Label(window, text="Ваше сообщение")
lbl.grid(column=0, row=0)

txt = scrolledtext.ScrolledText(window, width=45, height=20)
txt.grid(column=1, row=0)

txt3 = scrolledtext.ScrolledText(window, width=45, height=20)
txt3.grid(column=3, row=0)

txt4 = scrolledtext.ScrolledText(window, width=45, height=20)
txt4.grid(column=3, row=4)


lbl = Label(window, text="Результат:")
lbl.grid(column=0, row=4)


txt2 = scrolledtext.ScrolledText(window, width=45, height=20)
txt2.grid(column=1, row=4)

btn = Button(window, text="Вывести частотную характеристику", command=clicked)
btn.grid(column=1, row=1)
lbl = Label(window)


btn = Button(window, text="Вывести частотную характеристику", command=clicked2)
btn.grid(column=1, row=3)
lbl = Label(window)

btn = Button(window, text="Вывести гистограмму", command=histogramm)
btn.grid(column=3, row=1)
lbl = Label(window)

btn = Button(window, text="Вывести гистограмму", command=histogramm2)
btn.grid(column=3, row=3)
lbl = Label(window)

btn = Button(window, text="Исправить основной текст в соответствии с частотными характеристиками", command=fixed)
btn.grid(column=1, row=2)
lbl = Label(window)

btn = Button(window, text="Выбрать файл", command=open_file)
btn.grid(column=0, row=1)
lbl = Label(window)

txt5 = scrolledtext.ScrolledText(window, width=20, height=20)
txt5.grid(column=4, row=0)



window.mainloop()

