import tkinter as tk
from Player import Player

empty_grid = {
    "1" : None,
    "2" : None,
    "3" : None,
    "4" : None,
    "5" : None,
    "6" : None,
    "bonus" : None,
    "brelan" : None,
    "carre" : None,
    "full" : None,
    "petite_suite" : None,
    "grande_suite" : None,
    "yahtzee" : None,
    "chance" : None,
    "bonus_yahtzee" : None,
    "total" : None,
}

players = []
tour = 0
player_count = 0
final_dees = []
dees_list = []

def ouvrir_troisieme_fenetre():
    
    labels = []
    chkbox = []
    
    # Crée une troisième fenêtre
    troisieme_fenetre = tk.Tk()
    troisieme_fenetre.wm_state("zoomed")
    troisieme_fenetre.title("Yahtzee")
    
    # Ajoutez ici le contenu souhaité pour la troisième fenêtre
    label_nom = tk.Label(troisieme_fenetre, text="appuyer sur 'Jouer' pour commencer la partie...")
    label_nom.grid(row=0, column=0, padx=5, pady=5)

    for i in range(1, 6):
        # Création du label
        label = tk.Label(troisieme_fenetre, text=f"[0]")
        label.grid(row=1, column=i, padx=5, pady=5)
        labels.append(label)
        
        # Création de la checkbox
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(troisieme_fenetre, text=f"", variable=var)
        checkbox.grid(row=2, column=i, padx=5, pady=5)
        chkbox.append(var)

    def jouer():
        if(0<tour<3) :
            dees_list = chk_liste()
            dees_list = set(dees_list)
            final_dees = []
            for dee in dees_list :
                final_dees.append(dees[dee-1])
            
            final_dees.sort()
            if(len(final_dees) == 5) :
                tour=2
        label_nom.config(text=f"{players[player_count]}, jouez votre tour N°{tour+1}")
        dees = final_dees.copy()
        dees += players[player_count].throw_dees(5-len(final_dees))
        dees.sort()
        set_dees(dees)
        tour+=1
        if tour >=3:
            player_count+=1
            if player_count == len(players) :
                player_count=0
            tour=0
            final_dees = []
            dees_list = []


    # Création d'un bouton qui va appeler la fonction 'valider' lorsqu'on clique dessus
    bouton_jouer = tk.Button(troisieme_fenetre, text="Jouer", command=jouer)
    bouton_jouer.grid(row=3, column=0, padx=5, pady=5)
    
    # Lancement de la boucle principale de la troisième fenêtre
    troisieme_fenetre.mainloop()

    
    
    def chk_liste() :
        liste = []
        for i in range(len(chkbox)) :
            if chkbox[i] == True :
                liste.append(i)
        return(liste)
    
    def set_dees(dees) :
        for i in range(len(labels)) :
            labels[i].config(text=f"[{dees[i].point}]")



        





def ouvrir_deuxieme_fenetre(nombre):
    # Crée une nouvelle fenêtre (deuxième fenêtre)
    nouvelle_fenetre = tk.Tk()
    nouvelle_fenetre.wm_state("zoomed")
    nouvelle_fenetre.title("Noms des Joueurs")

    label = tk.Label(nouvelle_fenetre, text="entrer les noms des joueurs :")
    label.pack()
    
    # Liste pour stocker les références des champs de texte
    champs_texte = []

    # Génère un nombre de champs de texte égal à 'nombre'
    for i in range(nombre):
        champ = tk.Entry(nouvelle_fenetre)
        champ.pack()
        champs_texte.append(champ)
    
    # Fonction pour récupérer les valeurs des champs de texte et ouvrir la troisième fenêtre
    def recuperer_valeurs_et_ouvrir_troisieme_fenetre():
        # Récupère les valeurs ici si nécessaire
        for i in range(len(champs_texte)) :
            nom = champs_texte[i].get()
            if type(nom) == type(" ") and " " not in nom :
                players.append(Player(nom, empty_grid))
            
        
        # Ferme la deuxième fenêtre
        nouvelle_fenetre.destroy()
        
        # Ouvre la troisième fenêtre
        ouvrir_troisieme_fenetre()

    # Bouton pour récupérer les valeurs et ouvrir la troisième fenêtre
    bouton_recuperer = tk.Button(nouvelle_fenetre, text="Valider", command=recuperer_valeurs_et_ouvrir_troisieme_fenetre)
    bouton_recuperer.pack()

    # Lancement de la boucle principale de la nouvelle fenêtre
    nouvelle_fenetre.mainloop()

def valider():
    # Récupère la valeur du champ de texte et la convertit en entier
    try :
        nombre_joueurs = int(champ_texte.get())
        if nombre_joueurs<=0 :
            raise ValueError()
        # Ferme la fenêtre actuelle
        fenetre.destroy()
        
        # Ouvre la nouvelle fenêtre avec le nombre de champs spécifié
        ouvrir_deuxieme_fenetre(nombre_joueurs)
    except :
        label2.config(text=f"Entrer un nombre positif!!")
        

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.wm_state("zoomed")
fenetre.title("Nombre de joueurs")

# Création d'un label
label = tk.Label(fenetre, text="Entrer le nombre de joueurs")
label.pack()

# Création d'un champ de texte
champ_texte = tk.Entry(fenetre)
champ_texte.pack()

label2 = tk.Label(fenetre, text="", fg="red")
label2.pack()

# Création d'un bouton qui va appeler la fonction 'valider' lorsqu'on clique dessus
bouton_valider = tk.Button(fenetre, text="Valider", command=valider)
bouton_valider.pack()

# Lancement de la boucle principale
fenetre.mainloop()