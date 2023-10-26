import random
import string
import PySimpleGUI as sg
import pyperclip

# GUI našej aplikácie.

sg.theme('BlueMono')  # Farba
sg.set_options(font='calibri 15')
okno = [    [sg.Text('Počet veľkých písmen:'), sg.Push(), sg.InputText(size=15, key='-UP-')],
            [sg.Text('Počet malých písmen:'), sg.Push(), sg.InputText(size=15, key='-LOW-')],
            [sg.Text('Počet čísiel:'), sg.Push(), sg.InputText(size=15, key='-NUM-')],
            [sg.Text('Počet znakov:'), sg.Push(), sg.InputText(size=15, key='-SYM-')],
            [sg.Button('Ok'), sg.Button('Zrušiť'), [sg.Button('Skopírovať'),  sg.Text('', size=(15, 1), key='-VYSTUP-')]],
            [sg.Text('Heslo:'), sg.Multiline(size=50, no_scrollbar=True, disabled=True, key='HESLO')]]

window = sg.Window('Jakubov generátor hesiel', okno, size=(500, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Zrušiť':
        break

    if event == 'Ok':
        try:
            # variabilne, ktore obsahuju vsetky pismena, cisla, symboly
            hesloV = int(values['-UP-'])
            velkePismena = random.sample(string.ascii_uppercase, hesloV)
            hesloM = int(values['-LOW-'])
            malePismena = random.sample(string.ascii_lowercase, hesloM)
            hesloC = int(values['-NUM-'])
            cisla = random.sample(string.digits, hesloC)
            hesloS = int(values['-SYM-'])
            symboly = random.sample(string.punctuation, hesloS)

            heslo = velkePismena + malePismena + cisla + symboly
            heslo = random.sample(heslo, len(heslo))
            heslo = "".join(heslo)
            window['HESLO'].update(heslo)

            # zobrazenie nespravneho vstupu
        except ValueError:
            window['HESLO'].update('Nesprávne vstupy.')

            # skopirovanie vystupu
    if event == 'Skopírovať':
        pyperclip.copy(window['HESLO'].get())
        window['-VYSTUP-'].update('Heslo skopírované.')

window.close()