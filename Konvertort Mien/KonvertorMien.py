from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import json

# farby
farba1 = "#FFEFDB" #AntiqueWhite1
farba2 = "#FFC125" #Goldenrod1
farba3 = "#000000" #black

# vytvorenie okna
okno = Tk()
okno.title("Konvertor mien by Holubex")
okno.geometry("300x350")
okno.config(bg=farba1)
okno.resizable(False, False)

# vytvorenie grafiky(vrch)
vrch = Frame(okno, width=330, height=60, bg=farba2)
vrch.grid(row=0, column=0)

# vytvorenie grafiky(hlavne)
hlavne = Frame(okno, width=330, height=260, bg=farba1)
hlavne.grid(row=1, column=0)

# funkcia na konvertovanie
def konvertovanie():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    mena1 = multi_riadok.get()
    mena2 = multi_riadok2.get()
    amount = hodnota.get()

    querystring = {"from":mena1,"to":mena2,"amount":amount}

    if mena2 == 'USD':
        symbol = '$'
    elif mena2 == 'EUR':
        symbol = '€'
    elif mena2 == 'GBP':
        symbol = '£'
    elif mena2 == 'RUB':
        symbol = '₽'
    elif mena2 == 'CZK':
        symbol = 'Kč'
    elif mena2 == 'INR':
        symbol = '₹'

    headers = {
        "X-RapidAPI-Key": "c91345ffbdmshd8a9887361fed8fp1d498fjsn1344880ded93",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data['result']['convertedAmount']
    zaokruhlene = symbol + '{: .2f}'.format(converted_amount)

    vysledok['text'] = zaokruhlene


# logo aplikacie na vrchu
ikona = Image.open('change.png')
ikona = ikona.resize((40, 40)) # velkost ikony
ikona = ImageTk.PhotoImage(ikona)
nazov = Label(vrch, image=ikona, compound=LEFT, text="Konvertor mien", height=5, padx=13, pady=30, anchor=CENTER, font="Arial 16 bold", fg=farba3, bg=farba2)
nazov.place(x=25, y=0)

# vysledok
vysledok = Label(hlavne, text=" ", width=16, height=2, padx=12, pady=7, relief='solid', anchor=CENTER, font="Ivy 15 bold", fg=farba1, bg=farba2)
vysledok.place(x=45, y=10)

# vlozenie sumy

#vytvorenie listu mien
mena = ['USD', 'EUR', 'GBP', 'RUB', 'CZK', 'INR']

mena_z = Label(hlavne, text = 'Z:', width=8, height=1, pady=0, padx=0, relief='flat', anchor=NW, font= "Ivy 12 bold", fg=farba3, bg=farba1)
mena_z.place(x=40, y=100)

multi_riadok = ttk.Combobox(hlavne, width=8, justify=LEFT, font="Ivy 12 bold")
multi_riadok['values'] = (mena)
multi_riadok.place(x=42, y=125)

# vlozenie sumy do ktorej sa meni

mena_do = Label(hlavne, text = 'DO:', width=8, height=1, pady=0, padx=0, relief='flat', anchor=NE, font= "Ivy 12 bold", fg=farba3, bg=farba1)
mena_do.place(x=120, y=100)

multi_riadok2 = ttk.Combobox(hlavne, width=8, justify=LEFT, font="Ivy 12 bold")
multi_riadok2['values'] = (mena)
multi_riadok2.place(x=172, y=125)

# vlozenie
zadajSumu = Label(hlavne, text="Zadaj sumu:", width=10, height=1, pady=0, padx=0, relief='flat', anchor=NW, font="Ivy 12 bold", fg=farba3, bg=farba1)
zadajSumu.place(x=110, y=170)
hodnota = Entry(hlavne, width=20, justify=CENTER, font="Ivy 12 bold", relief=SOLID)
hodnota.place(x=62, y=195)

# tlacidlo konvertovat
konvertovat = Button(hlavne, text='Konvertovať', width=19, padx=5, height=1, bg=farba3, fg=farba1, font="Ivy 12 bold", relief=SOLID, command=konvertovanie)
konvertovat.place(x=50, y=230)

okno.mainloop()