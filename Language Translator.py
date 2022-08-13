from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
import os
app=Tk()
app.geometry('500x550')
app.title('Language Translator')
app.resizable(0,0)
frame=Frame(app).pack(side=BOTTOM)

def get():
    s=source_language.get()
    d=destination_language.get()
    message=source_Text.get(1.0,END)
    text=Translator().translate(text=message,src=s,dest=d)
    trans=text.text
    destination_Text.delete(1.0,END)
    destination_Text.insert(END,trans)

def speak():
    dic = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
           'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
           'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
           'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
           'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
           'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
           'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
           'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
           'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
           'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
           'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
           'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
           'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
           'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
           'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
           'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',
           'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi',
           'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil',
           'Hebrew': 'he'}
    lan=destination_language.get()
    voice=destination_Text.get(1.0,END)
    if os.path.exists("abc.mp3"):
        os.remove("abc.mp3")
    obj=gTTS(text=voice,lang=dic[lan.lower()],slow=False)
    obj.save("abc.mp3")
    playsound("abc.mp3")

languages=list(LANGUAGES.values())
source_language=ttk.Combobox(frame,values=languages,width=10)
source_language.place(x=20,y=10)
source_language.set("English")
destination_language=ttk.Combobox(frame,values=languages,width=10)
destination_language.place(x=400,y=10)
destination_language.set('Bengali')

source_Text=Text(frame,font=('arial',10),height=10,wrap=WORD)
source_Text.pack(side=TOP,pady=35,padx=50)
button=Button(frame,text="Translate",font=('arial',10,'bold'),fg='blue',activebackground='green',relief=GROOVE,command=get)
button.pack(side=TOP)
destination_Text=Text(frame,font=('arial',10),height=11,wrap=WORD)
destination_Text.pack(side=TOP,padx=50,pady=15)

button=Button(frame,text="Speak",font=('arial',10,'bold'),fg='blue',activebackground='green',relief=GROOVE,command=speak)
button.pack(side=TOP,pady=10)
app.mainloop()