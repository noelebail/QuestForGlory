# QuestForGlory
Game creation report for QuestForGlory.

[<kbd> <br> Download <br> </kbd>](https://github.com/noelebail/QuestForGlory/releases/latest)

## Le plan du projet
Pour réaliser notre projet nous avons suivi le plan suivant.

![Capture](https://user-images.githubusercontent.com/99325966/235665537-bce6cf95-b4fd-4969-be83-ba1b640d2206.PNG)

## Scénario 
Pour construire notre scénario pour Quest For Glory, nous avons demandé à **ChatGPT** de nous proposer des idées pour un jeu textuel d'aventure. Nous avons employé le prompt suivant :
> *Propose une histoire de jeu d'aventure textuel.*

A la suite de la proposition de **ChatGPT** nous avons écrit le script dans un document texte sur visual studio code. 
Nous avons attribué à chaque type de phrase est associé à un symbole : 
- le "=" correspond à un texte avec un changement d'image
- le "+" correspond à un texte pour lequel on ne change pas d'image
- le "#" correspond aux différentes scènes
- le "?" correspond à un choix à faire pour le joueur

Pour ce qui est du titre du jeu nous avons demandé à **ChatGPT** de nous proposer différents titres avec le prompt  : 
> *Propose des titres qui correspondent au jeu.*

Et nous avons ainsi choisi **Quest For Glory**.
Pour créer l'histoire nous avons créé un système de choix qui permet au joueur de choisir plusieurs choix et donc de suivre différentes branches de l'histoire. L'histoire est construite sur un tronc principal et les choix annexes amènent à un fin d'histoire qui diffère.

## Illustration et Concept art
Afin de créer un univers singulier à notre jeu nous avons généré dess images correspondant à notre aventure sur **Leonardo AI**.On utilise des prompts précis pour obtenir l'image la plus proche de ce que l'on souhaite.  On choisit parmi les proposotionsde l'IA se qui correspond le mieux pour le jeu. On crée également quelques images avec **DALL-E** pour compléter notre banque d'images. 

> **Leonardo AI :**

![7d1f1a15208d784f6aa7ac6bec5bf326-xl](https://user-images.githubusercontent.com/99325966/236392472-bd7d99f5-d357-451d-bae6-65c4704a2509.jpg)
![dhrl](https://user-images.githubusercontent.com/99325966/236391638-2601657f-e8b1-4cbb-929c-2eb3c5c63614.jpg) 
![3cef5e9aeddd1d66664568dc1b3dacbc-l](https://user-images.githubusercontent.com/99325966/236391900-b32096ad-f89e-4368-8f63-c41d4aba3fdb.jpg)
![71e8c10c607bd7147406fd271ab3e3ad-l](https://user-images.githubusercontent.com/99325966/236392782-8fd9892d-1b2d-42f5-9bbb-eeacc929fe59.jpg)

> **DALL-E :**

![OIG (2)](https://user-images.githubusercontent.com/99325966/236393668-c4ff61ca-c632-4192-b72c-2f524da39ac7.jpg)
![OIG 1HRiCckgy8kwCBit](https://user-images.githubusercontent.com/99325966/236393949-1c5285f2-e89e-4703-84d7-b9d2f09928b2.jpg)
![OIG (1)](https://user-images.githubusercontent.com/99325966/236392939-d8c90d15-9f09-4465-9d05-368909d36b93.jpg)
![5276a4ec3e17e8dc0c89-xl](https://github.com/noelebail/QuestForGlory/assets/99325966/dada30a3-71ba-4601-aaf8-3cb9d0f96f80)

Après une concertation avec les différents membres de l'équipe nous avons constaté une meilleure qualité dans le style *jeu vidéo*, pour **DALL-E**. Pour pouvoir créer une identité propre à notre jeu nous avons chercher des images dans un style cohérent. Nous avons donc selectionné le style GC Society Landscape qui correspond bien à l'univers que nous avons voulu donner à  **Quest For Glory**. 

> **Trame des images du script**
Voilà quelques images importantes du script

![image](https://github.com/noelebail/QuestForGlory/assets/99325966/1d62cc9a-46af-4db6-928d-501e23d21c24)
![image (1)](https://github.com/noelebail/QuestForGlory/assets/99325966/cae46b66-1fb1-41d6-9c9f-50824c48f803)
![image (2)](https://github.com/noelebail/QuestForGlory/assets/99325966/574179c8-0f40-453a-ac72-037510fabe51)
![image (3)](https://github.com/noelebail/QuestForGlory/assets/99325966/097f5ff2-ff23-42a5-8179-f1b4bdf0259b)


## Code / Partie programmation

> **Fonctionnement du jeu**

On a créé un moteur de texte qui permet d'afficher le texte au bon endroit (si c'est un titre de scène il s'affiche en haut ou encore si c'est un choix il s'affiche dans une case en bas à droite). Cette partie du programme regarde le préfixe devant chaque phrase (#, +, =, ou ?) et permet ainsi de traiter différemment chague phrase.
```python
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

```
    
On code également dans cette partie différentes fonctions annexes
        

>  **Interface graphique**

On emploie customtkinter pour créer une interface graphique dans laquelle on peut effectuer des choix, afficher des images ou afficher le titre de la scène. 
*Pour plus d'infos sur le code voir les commentaires.*

![qfg](https://github.com/noelebail/QuestForGlory/assets/99325966/500cc1d6-bbde-4191-8598-2cebcfb608b6)


> **Gestion d'image**

Pour la gestion des images on utilise les préfixes devant les phrases. Si on a un "=" on change d'image, si on a un "+", l'image reste la même.
Les images sont gérées grâce à un compteur, elles sont numérotées. L'image affichée correspond au nombre du compteur. On commence par l'image numéro 1 avec le compteur = 1. Dès qu'on a un égal on ajoute 1, on passe donc à l'image 2.

```python
if script[line][0] == "=":  # Si le premier arguments du texte est un = alors
        narrativelabel.configure(text=script[line][1:])  # On affiche le texte dans la frame narrative
        imagecount += 1
        narrativeimg.configure(light_image=PIL.Image.open(f"./img/{imagecount}.jpg"))
 ```

> **Gestion des choix**

Si jamais le choix de l'utilisateur est bon on passe à la suite de l'histoire, si le choix est mauvais le joueur est redirigé vers une fin du jeu.

> **Intérêt du programme**

Avec ce programme on produit un jeu mais également un moteur de jeu car on peut réemployer la structure pour créer de nouveaux jeux textuels.

## Conclusion 

Avec ce jeu on nous avons voulu proposer une histoire originale avec de simples choix entre deux propositions. Pour le deuxième projet nous avons pour ambition de proposer un deuxième volet de ce jeu avec quelques améliorations comme par exemple des énigmes.

![logor](https://github.com/noelebail/QuestForGlory/assets/99325966/c886b0d3-6c65-4c9e-ac7f-590a72d3f68d)
H2AN Corporation
