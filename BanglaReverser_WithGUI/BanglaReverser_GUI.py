
import PySimpleGUI as sg
import os, clipboard

os.system('cls')

def reverse(text):
    vowels = ['া','ি','ী','ু','ূ','ৃ','ে','ৈ','ো','ৌ']
    chondrobindu = 'ঁ'
    hosonto = '্'
    rev = ""
    temp = ''
    temp2 = ''
    i = 1
    while i <= len(text):
        ginipig = text[-i]
        if ginipig == chondrobindu:
            temp2 = ginipig
            i = i + 1
        elif ginipig in vowels:
            temp = ginipig
            i = i + 1
        else:
            if len(text)-i >= 1:
                if text[-i-1] != hosonto:
                    rev += ginipig
                    rev += temp
                    rev += temp2
                    temp = ''
                    temp2 = ''
                    i = i + 1
                else:
                    if len(text)-i >= 4:
                        if text[-i-3] == hosonto:
                            rev += text[-i-4]
                            rev += hosonto
                            rev += text[-i-2]
                            rev += hosonto
                            rev += ginipig
                            rev += temp
                            rev += temp2
                            temp = ''
                            temp2 = ''
                            i = i + 5
                        else:
                            rev += text[-i-2]
                            rev += hosonto
                            rev += ginipig
                            rev += temp
                            rev += temp2
                            temp = ''
                            temp2 = ''
                            i = i + 3
                    else:
                        rev += text[-i-2]
                        rev += hosonto
                        rev += ginipig
                        rev += temp
                        rev += temp2
                        temp = ''
                        temp2 = ''
                        i = i + 3
            else:
                rev += ginipig
                rev += temp
                rev += temp2
                temp = ''
                temp2 = ''
                i = i + 1
    return rev

      
sg.theme('DarkBlue')
   
layout = [[sg.Text(text='Type anything in Bangla or English:', text_color='White')],
        [sg.Multiline(key='-IN-',  text_color='Pink', size=(70,4), focus=True)],
        [sg.Text(text='Reversed:', text_color='Yellow')],
        [sg.Multiline( key='-OUTPUT-', text_color='White',disabled=True, size=(70,5))]]


window = sg.Window('Bangla and English Reverser by KMFRuhan', layout, location=(380,220), keep_on_top = False, return_keyboard_events=True, finalize=True)

window.bind("<Control-KeyPress-w>", "ctrl-w")
window.bind("<Control-KeyPress-W>", "ctrl-w")
window.bind("<KeyPress>", "KP")
window.bind("<Control-KeyPress-c>", "ctrl-c")
window.bind("<Control-KeyPress-C>", "ctrl-c")

# Enable the undo mechanism:
text = window['-IN-'].Widget
text.configure(undo=True)

while True:
    event, values = window.read()
    

    if event in  (None, 'ctrl-w'):
        break

    if event == 'KP':
        result = reverse(values['-IN-'].strip())
        window['-OUTPUT-'].update(result)

    if event == "ctrl-c" and result != '':
        clipboard.copy(result)

    

window.close()

os.system('cls')