from tkinter import*

window = Tk()

def tombol_klik(item):
    global ekspresi
    ekspresi += str(item)
    input_teks.set(ekspresi)

def tombol_reset():
    global ekspresi
    ekspresi = ""
    input_teks.set("")

def samadengan():
    try:
        result = eval(ekspresi)
        input_teks.set(result)
    except Exception as e:
        input_teks.set("Error")

def plus_minus():
    current_value = input_teks.get()
    if current_value:
        if current_value[0] == '-':
            input_teks.set(current_value[1:])
        else:
            input_teks.set('-' + current_value)

# Variabel global untuk ekspresi
ekspresi = ""
input_teks = StringVar()

# Frame dan label untuk tampilan
frame = Frame(window, bg="black", width=500, height=300)
frame.pack()

frame2 = Frame(window, bg="black", width=500, height=300)
frame2.pack()

# Label 1
label = Label(frame, text="kalkulator Hilmy XII pplg 1", width=50, anchor="w", font=("Arial", 8))
label.pack(padx=20, pady=20)

# Label 2, samakan width dengan label 1
label2 = Label(frame, text="Hallo, Hilmy XII Pplg 1", font=("Arial", 24), anchor="e", width=50, bg="gray", fg="white", textvariable=input_teks)
label2.pack(padx=20, pady=20)

button1 = Button(frame2, text="C",bg="gray",fg="white",command=tombol_reset)
button1.grid(row=0, column=1, padx=10, pady=10)

button_plus_minus = Button(frame2, text="±", bg="gray", fg="white", width=1, height=1, command=plus_minus)
button_plus_minus.grid(row=0, column=2)

buttonpersen= Button(frame2, text="%", bg="gray",fg="white",command=lambda: tombol_klik("%"))
buttonpersen.grid(row=0, column=3)

buttonbagi= Button(frame2, text="/", bg="orange",fg="white",command=lambda: tombol_klik("/"))
buttonbagi.grid(row=0, column=4, padx=20, pady=20)

button5 = Button(frame2, text="7",bg="darkgray",fg="white",command=lambda: tombol_klik("7"))
button5.grid(row=1, column=1, padx=20, pady=20)

button6 = Button(frame2, text="8",bg="darkgray",fg="white",command=lambda: tombol_klik("8"))
button6.grid(row=1, column=2, padx=20, pady=20)

button7 = Button(frame2, text="9",bg="darkgray",fg="white",command=lambda: tombol_klik("9"))
button7.grid(row=1, column=3, padx=20, pady=20)

buttonkali= Button(frame2, text="x", bg="orange",fg="white",command=lambda: tombol_klik("*"))
buttonkali.grid(row=1, column=4, padx=20, pady=20)

button9 = Button(frame2, text="4",bg="darkgray",fg="white",command=lambda: tombol_klik("4"))
button9.grid(row=2, column=1, padx=20, pady=20)

button10 = Button(frame2, text="5",bg="darkgray",fg="white",command=lambda: tombol_klik("5"))
button10.grid(row=2, column=2, padx=20, pady=20)

button11 = Button(frame2, text="6",bg="darkgray",fg="white",command=lambda: tombol_klik("6"))
button11.grid(row=2, column=3, padx=20, pady=20)

button12 = Button(frame2, text="–", bg="orange",fg="white",command=lambda: tombol_klik("–"))
button12.grid(row=2, column=4, padx=20, pady=20)

button13 = Button(frame2, text="1",bg="darkgray",fg="white",command=lambda: tombol_klik("1"))
button13.grid(row=3, column=1, padx=20, pady=20)

button14 = Button(frame2, text="2",bg="darkgray",fg="white",command=lambda: tombol_klik("2"))
button14.grid(row=3, column=2, padx=20, pady=20)

button15 = Button(frame2, text="3",bg="darkgray",fg="white",command=lambda: tombol_klik("3"))
button15.grid(row=3, column=3, padx=20, pady=20)

buttonsamadengan= Button(frame2, text="=", bg="orange",fg="white",command=samadengan)
buttonsamadengan.grid(row=4, column=4, padx=20, pady=20)

buttonplus= Button(frame2, text="+", bg="orange",fg="white",command=lambda: tombol_klik("+"))
buttonplus.grid(row=3, column=4, padx=20, pady=20)

button19 = Button(frame2, text="0",bg="darkgray",fg="white",command=lambda: tombol_klik("0"), width=10)
button19.grid(row=4, column=1, columnspan=2, padx=20, pady=20)

button20 = Button(frame2, text=" . ",bg="darkgray",fg="white",command=lambda: tombol_klik(" . "))
button20.grid(row=4, column=3, padx=20, pady=20)

# Menjalankan loop aplikasi
window.mainloop()

