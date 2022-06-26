import googletrans
from googletrans import Translator
import ctypes
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
import tkinter as tk

translator = Translator(service_urls=['translate.googleapis.com'])

def google_translate(word, metin_dil, cev_dil):
    translator = Translator()
    translator.raise_Exception = True
    translated = translator.translate(word, src=metin_dil, dest=cev_dil).text
    return translated
   

window = tk.Tk()

window.resizable(False, False)
window.title("Translator")
window.geometry("500x500")
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 2)

####### listbox for text language ########
list_items = tk.StringVar(value = list(googletrans.LANGUAGES.values()))
label_textLANG = tk.Label(window, text = "metnin dilini seçiniz:")
label_textLANG.grid(column = 0, row = 0)
listbox_textLANG = tk.Listbox(window, listvariable = list_items, height = 6, selectmode = "extended")
listbox_textLANG.grid(column = 0, row = 1, sticky = "nwes", padx = 5, pady = 5)



###### listbox for trasnlate language #######
label_translateLANG = tk.Label(window, text = "metnin çevrileceği dili seçin:")
label_translateLANG.grid(column = 1, row = 0)
listbox_translateLANG = tk.Listbox(window, listvariable = list_items, height = 6, selectmode = "browse") # browse > tekli seçim, extended > çoklu seçim
listbox_translateLANG.grid(column = 1, row = 1, sticky = "nwes", padx = 5, pady = 5)


# a function
def chooseONE():
    selected_indices = listbox_textLANG.curselection() # for text lang listbox
    selectedLang = listbox_textLANG.get(selected_indices)

    selected_indicesTrans = listbox_translateLANG.curselection() # for translate lang text box
    selectedLangTranslate = listbox_translateLANG.get(selected_indicesTrans)

    label_LANG1.config(text = selectedLang)

    lang_values = list(googletrans.LANGUAGES.values())

    for each in range(len(lang_values)):
        if selectedLang == lang_values[each]:
            metinDili = list(googletrans.LANGUAGES.keys())[each]
            print(metinDili)

        if selectedLangTranslate == lang_values[each]:
            ceviriDili = list(googletrans.LANGUAGES.keys())[each]
            print(ceviriDili)


###### button for text lang ######

button_textLANG = tk.Button(window, text = "çevir", command = chooseONE)
button_textLANG.grid(column = 1, row = 2)
label_LANG1 = tk.Label(window, text = "")
label_LANG1.grid(column = 0, row = 3)
window.mainloop()
"""
############   cod of cursor position   ###############

#==== GLOBAL VARIABLES ======================

gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))


def move (y, x):
   # Move cursor to position indicated by x and y.
   value = x + (y << 16)
   ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))


def addstr (string):
   # Write string
   ctypes.windll.kernel32.WriteConsoleW(gHandle, c_wchar_p(string), c_ulong(len(string)), c_void_p(), None)

# move(0,0)
# addstr("a")
#######################################################


metnin_dili = str()
cevrilecek_dil = str()
eski_metin = str()
eski_sonuc = str()

while True:
    print("metnin dili(en, tr vb.):")
    move(0, 24)
    addstr("   ")#çeviri bittikten sonra tekrar dili sorarken öncekini siliyor
    move(1, 27)
    addstr("   ")#çeviri bittikten sonra tekrar dili sorarken öncekini siliyor
    move(0, 24)
    metnin_dili = input()
    

    try:
        if metnin_dili in googletrans.LANGUAGES.keys():
            
            while True:
                print("çevrilecek dil(en, tr vb.):")
                move(1, 27)
                cevrilecek_dil = input()
                

                if cevrilecek_dil in googletrans.LANGUAGES.keys():
                    move(2, 0)
                    addstr(" "*21)
                    move(4, 0)
                    print("çevrilecek metin:")
                    move(4, 17)
                    addstr(" "*len(eski_metin))#yeni çeviri için sayfayı temizliyor
                    move(5, 7)
                    addstr(" "*len(eski_sonuc))
                    move(4, 17)
                    metin = input()
                    eski_metin = metin
                    
                    sonuc = google_translate(metin, metnin_dili, cevrilecek_dil)
                    eski_sonuc = sonuc
                    print(f"çeviri:{sonuc}")
                    move(0, 0)
                    break

                else:
                   move(1, 27)
                   addstr(len(cevrilecek_dil)*" ")
                   move(2, 0)
                   print("dil seçiminiz hatalı!")
                   move(1, 0)

        else:
           move(0, 24)
           addstr(len(metnin_dili)*" ")
           move(1, 0)
           print("dil seçiminiz hatalı!      ")# sondaki boşluklar ilk kullanımdan sonra 2.dil seçimindeki hatadan ötürü var
           move(0, 0)

    except TypeError:
        move(0, 0)

"""