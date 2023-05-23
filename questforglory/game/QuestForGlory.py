# Quest For Glory
#   Adrien briec: Code/GUI - PDG
#   Noé Le Bail: Site/Images/Scénario - DRH (admirateur du PDG)
#   Hedi Othman: Images/Scénario - Directeur artistique et scénariste
#   Arran Godefroy: Images/Commentaires - Simple employé pas utile de fou (c'est une blague :))
#   Github Copilot: Commentaires - Assistant explication
#   ChatGPT: Scénario - Assistant scénariste


import tkinter  # On importe une librairie permettant de faire une interface graphique
import customtkinter  # On importe une librairie avec laquelle on affiche une interface graphique
import PIL # On importe une librairie permettant de faire des images
import webbrowser

WIDTH = 700 # On définie une variable WIDTH qui a pour valeur 700
LENGTH = 600 # On définie une variable LENGTH qui a pour valeur 600

with open("script.txt", "r", encoding="utf-8") as file:
    tempscript = file.readlines()
    script = [i.replace("\n", "") for i in tempscript]

line=0  # On définie une variable line qui a pour valeur 0
imagecount = 0 # On définie une variable imagecount qui a pour valeur 0
questioncount = 0

def text_engine():  # On définie une fonction text_engine qui a pour argument text permettant d'afficher de façon différentes certaines partie du texte
    global line # On définie la variable line comme étant globale
    global imagecount
    global questioncount

    if script[line][0] == "#":  # Si le premier arguments du texte est un # alors
        titlelabel.configure(text=script[line][1:])  # On affiche ce texte en titre de la fenêtre
        line += 1 # On ajoute 1 à la variable line
        #text_engine() # On rappelle la fonction text_engine

    if script[line][0] == "=":  # Si le premier arguments du texte est un = alors
        narrativelabel.configure(text=script[line][1:])  # On affiche le texte dans la frame narrative
        imagecount += 1
        narrativeimg.configure(light_image=PIL.Image.open(f"./img/{imagecount}.jpg"))

    if script[line][0] == "+":  # Si le premier arguments du texte est un + alors
        narrativelabel.configure(text=script[line][1:])  # On affiche le texte dans la frame narrative
    
    if script[line][0] == "?":
        questioncount += 1
        tempquestion = script[line].split(";")
        narrativelabel.configure(text=tempquestion[0][1:])
        validatebutton.configure(command=validaterealchoice)
        choiceb1.configure(text=tempquestion[1].split(",")[0])
        choiceb2.configure(text=tempquestion[1].split(",")[1])
    
    if script[line][:3] == "END":
        templine = script[line].split(";")
        narrativelabel.configure(text=templine[1])
        validatebutton.configure(state="disabled")
        choiceb1.configure(state="disabled")
        choiceb2.configure(state="disabled")
        validatebutton.configure(text="Fin!")


def validaterealchoice():
    global line
    tempquestion = script[line].split(";")

    if choicevar.get() == int(tempquestion[2]):
        validatebutton.configure(command=validatechoice)
        line += 1 # On ajoute 1 à la variable line
        choiceb1.configure(text="Continuer")
        choiceb2.configure(text="Continuer")
        text_engine()
    
    else:
        narrativelabel.configure(text=tempquestion[3])
        validatebutton.configure(state="disabled")
        choiceb1.configure(state="disabled")
        choiceb2.configure(state="disabled")
        validatebutton.configure(text="Dommage!")
        narrativeimg.configure(light_image=PIL.Image.open(f"./img/w{questioncount}.jpg"))

def validatechoice():
    global line

    if choicevar.get() == 1:
        line += 1 # On ajoute 1 à la variable line
        text_engine()
    
    elif choicevar.get() == 2:
        line += 1 # On ajoute 1 à la variable line
        text_engine()
    
    else:
        pass

def changeobjectstate(object, state):
    object.configure(state=state)

def openurl(url):
    webbrowser.open(url)

def creditsf():
    if creditswin.winfo_exists:
        creditswin.deiconify()

# Appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Main app
app = customtkinter.CTk()  # Mainframe
app.geometry(f"{WIDTH}x{LENGTH}")  # On définit les dimensions de l'interface graphique
app.resizable(False,False)
app.title("Quest for Glory")  # On donne comme titre de la fenêtre Quest for Glory

# Title frame
titleframe = customtkinter.CTkFrame(app, height=35)
titleframe.pack(padx=10, pady=10, fill="both")
titleframe.pack_propagate(False)

# Title label
titlelabel = customtkinter.CTkLabel(titleframe, text=script[line][1:])
titlelabel.pack(padx=5, pady=5, side="bottom")

# Picture frame
pictureframe = customtkinter.CTkFrame(app)
pictureframe.pack(padx=10, pady=10, fill="both", expand=True)
pictureframe.pack_propagate(False)

# Bottom frame
bottomframe = customtkinter.CTkFrame(app, height=150)
bottomframe.pack(padx=10, pady=10, fill="both")  # On definie la frame tel qu'il a un écart avec les autres de 10 pixels sur les côtés + en haut et en bas  et on l'affiche sur le bas de l'interface
bottomframe.pack_propagate(False)

# Narrative frame
narrativeframe = customtkinter.CTkFrame(bottomframe)
narrativeframe.pack(padx=10, pady=10, side="left", fill="both", expand=True)
narrativeframe.pack_propagate(False)

# Choice frame
choiceframe = customtkinter.CTkFrame(bottomframe)
choiceframe.pack(padx=10, pady=10, side="right")

# Image
narrativeimg = customtkinter.CTkImage(light_image=PIL.Image.open(f"./img/{imagecount}.jpg"), size=(500,500))
narrativeimglabel = customtkinter.CTkLabel(pictureframe, image = narrativeimg, text=None)
narrativeimglabel.pack(padx=10, pady=10)

# Narrative label
narrativelabel = customtkinter.CTkLabel(narrativeframe, text="Dans une contrée lointaine...", wraplength=400)
narrativelabel.pack(padx=10, pady=10)

# Credits button
creditsbutton = customtkinter.CTkButton(narrativeframe, text="Credits", command=creditsf)
creditsbutton.pack(padx=10, pady=10, side="bottom", anchor="sw")

# Choice buttons
choicevar = tkinter.IntVar()
choiceb1 = customtkinter.CTkRadioButton(choiceframe, text="Continuer", variable=choicevar, value=1, command=lambda: changeobjectstate(validatebutton, "normal"))
choiceb1.pack(padx=10, pady=10)
choiceb2 = customtkinter.CTkRadioButton(choiceframe, text="Continuer", variable=choicevar, value=2, command=lambda: changeobjectstate(validatebutton, "normal"))
choiceb2.pack(padx=10, pady=10)

validatebutton = customtkinter.CTkButton(choiceframe, text="Valider", state="disabled", command=validatechoice)  # On créer un bouton sur lequel on peut cliquer et ou est affiché JKBDVHUHLV
validatebutton.pack(padx=10, pady=10)  # On definie le bouton tel qu'il a un ecart avec les autres de 10 pixels sur les côtés + en haut et en bas 

# Credits window
creditswin = customtkinter.CTkToplevel(app)
creditswin.title("Credits")
creditswin.geometry(f"{500}x{400}")
creditswin.resizable(False,False)
creditswin.withdraw()

creditstitle = customtkinter.CTkLabel(creditswin, text="Quest for Glory")
creditstitle.pack(padx=10, pady=10)

logoimg = customtkinter.CTkImage(PIL.Image.open("./img/logo.png"), size=(100,100))

logolabel = customtkinter.CTkLabel(creditswin, image=logoimg, text=None)
logolabel.pack(padx=10, pady=10)

corpname = customtkinter.CTkLabel(creditswin, text="H2AN Corporation")
corpname.pack()

creditstext = """Adrien briec: Code/GUI - PDG
Noé Le Bail: Site/Images/ - DRH (admirateur du PDG)
Hedi Othman: Images/Scénario - Directeur artistique et scénariste
Arran Godefroy: Images/Commentaires - Simple employé pas utile de fou (blague)
Github Copilot: Commentaires - Assistant explication
ChatGPT: Scénario - Assistant scénariste"""

creditslabel = customtkinter.CTkLabel(creditswin, text=creditstext)
creditslabel.pack(padx=10, pady=10)

creditslink = customtkinter.CTkLabel(creditswin, text="https://noelebail.github.io/QuestForGlory", text_color="blue", cursor="hand2")
creditslink.pack(padx=10, pady=10)
creditslink.bind("<Button-1>", lambda e: openurl("https://noelebail.github.io/QuestForGlory"))

cheatbutton = customtkinter.CTkButton(creditswin, text="Cheat codes", command=lambda: openurl("https://www.youtube.com/watch?v=xvFZjo5PgG0"))
cheatbutton.pack(padx=10, pady=10, side="bottom", anchor="sw")

app.mainloop()