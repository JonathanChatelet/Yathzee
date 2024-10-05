from Player import Player 
from tools.userinput import entrer_une_liste_de_chiffres,demander_saisie_nombre_borne,demander_saisie_nombre_positif,demander_saisir_mot

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

def count(values : list, val = None) -> int:
    """calcule la somme d'une liste ou la sommme d'un meme nombre dans cette list si val != None
    args : values : une liste de int, val : la valeur à compter (option)
    return : int"""
    counter = 0
    if val == None :
        for value in values :
            counter += value
    else :
        for value in (item for item in values if item == val) :
                counter += value
    return counter

def check_iteration(values : list, first=0, last=6) -> int :
    """calcule le nombre maximum d'iteration dans une liste et renvoi le nombre correspondant ainsi que son nombre d'itération
    args : values : une liste de int, first : int : le premier nombre à chercher dans la liste, last : int : le dernier nombre à chercher dans la liste
    return : un tuple de int"""
    max_iteration = 0
    max_value =0 
    for i in range(first,last) :
        current = values.count(i)
        if (current>max_iteration) :
            max_iteration = current
            max_value = i
    return max_iteration, max_value 

def check_following(values : list,n : int) -> bool:
    """verifie si il y a une suite de n chiffre dans la liste
    args : values : une liste de int, n : int
    return : bool : True si la liste possède une suite de n, False sinon"""
    copy_values = set(values.copy())
    copy_values = list(copy_values)
    copy_values.sort()
    checker_counter = 1
    old_value = None
    
    for value in copy_values :
        if old_value!= None :
            if value == old_value+1 :
                checker_counter += 1
                if(checker_counter>=n) :
                    return True
            else :
                checker_counter = 1
        old_value = value
    return False
    
def check_brelan(values : list) ->int :
    """verifie si il y a un brelan dans la liste
    args : values : une liste de int
    return : int : la somme des int de la liste s'il y a un brelan, 0 sinon"""
    max_iteration, max_value = check_iteration(values)
    if max_iteration >= 3 :
        return count(values)
    else :
        return 0

def check_carre(values : list) ->int :
    """verifie si il y a un carre dans la liste
    args : values : une liste de int
    return : int : la somme des int de la liste s'il y a un carre, 0 sinon"""
    max_iteration, max_value = check_iteration(values)
    if max_iteration >= 4 :
        return count(values)
    else :
        return 0

def check_full(values : list) ->int :
    """verifie si il y a un full dans la liste
    args : values : une liste de int
    return : int : 25 s'il y a un brelan, 0 sinon"""
    copy_values = values.copy()
    max_iteration, max_value = check_iteration(copy_values)
    if(max_iteration==3) :
        for i in range(max_iteration) :
            copy_values.remove(max_value)
        min_iteration, min_value = check_iteration(copy_values)
        if(min_iteration==2) :
            return 25
    return 0

def check_petite_suite(values : list) ->int :
    """verifie si il y a une petite suite dans la liste
    args : values : une liste de int
    return : int : 30 s'il y a un brelan, 0 sinon"""
    if check_following(values,4) :
        return 30
    else :
        return 0
    
def check_grande_suite(values : list) ->int :
    """verifie si il y a une grande suite dans la liste
    args : values : une liste de int
    return : int : 40 s'il y a un brelan, 0 sinon"""
    if check_following(values,5) :
        return 40
    else :
        return 0

def check_yahtzee(values : list) ->int :
    """verifie si il y a un yahtzee dans la liste
    args : values : une liste de int
    return : int : 50 s'il y a un brelan, 0 sinon"""    
    max_iteration, max_value = check_iteration(values)
    if max_iteration >= 5 :
        return 50
    else :
        return 0



def check_dees(dees : list,player : Player) :
    """Cette fonction permet de remplir la grille du joueur en fonction de son lancer de dées
    args : dees : liste de Dees - liste de dées du tours en cours, player : Player - le joueur ayant joué"""

    possibilities = ["1.les uns", "2.les deux", "3.les trois", "4.les quatres", "5.les cinqs", "6.les six", 
                     "7.brelan", "8.carre", "9.full", "10.petite suite", "11.grande suite", "12.yahtzee", "13.chance"]
   
    corresponding_possibilities = ["1", "2", "3", "4", "5", "6", "brelan", "carre", "full", "petite_suite", 
                                   "grande_suite", "yahtzee", "chance"]
    
    values = []
    proposition1 = ""
    proposition2 = ""
    yahtzee_on = False

    for i in range(len(possibilities)) :
        if player.grid[corresponding_possibilities[i]] == None and i<6:
            proposition1 += (possibilities[i] + (" "))
        elif player.grid[corresponding_possibilities[i]] == None and i>=6:
            proposition2 += (possibilities[i] + (" "))

    for dee in dees :
        values.append(dee.point)
    values.sort()

    if check_yahtzee(values)!=0:
        yahtzee_on=True
        if player.grid["bonus_yahtzee"] == None :
            player.grid["bonus_yahtzee"] = 50
        else :
            player.grid["bonus_yahtzee"] += 50

    print("Dans quelle ligne souhaitez vous placer vos points :")
    if proposition1 != "" :
        print(proposition1)
    if proposition2 != "" :
        print(proposition2)
    input_user = demander_saisie_nombre_borne("saisir votre choix ? ",1,13,False)

    print(str(input_user)," ")
    print(values)

    match (str(input_user)) :
        case "1" :
            player.grid["1"] = count(values,1)
        case "2" :
            player.grid["2"] = count(values,2)
        case "3" :
            player.grid["3"] = count(values,3)
        case "4" :
            player.grid["4"] = count(values,4)
        case "5" :
            player.grid["5"] = count(values,5)
        case "6" :
            player.grid["6"] = count(values,6)
        case "7" :
            player.grid["brelan"] = check_brelan(values)
        case "8" :
            player.grid["carre"] = check_carre(values)
        case "9" :
            if yahtzee_on :
                values= [1,1,1,2,2]
                yahtzee_on = False
            player.grid["full"] = check_full(values)
        case "10" :
            if yahtzee_on :
                values= [1,2,3,4,5]
                yahtzee_on = False
            player.grid["petite_suite"] = check_petite_suite(values)
        case "11" :
            if yahtzee_on :
                values= [1,2,3,4,5]
                yahtzee_on = False
            player.grid["grande_suite"] = check_grande_suite(values)
        case "12" :
            temp = check_yahtzee(values)
            if temp == 0 :
                player.grid["bonus_yahtzee"] = 0
            player.grid["yahtzee"] = temp
        case "13" :
            player.grid["chance"] = count(values)

def ask_players () -> list:
    """cette fonction permet d'initialiser le jeu en definissant le nombre de joueur ainsi que leurs noms respectif
    return : list Player - Liste de joueurs"""

    saisie = demander_saisie_nombre_positif("entrer le nombre de joueurs ? ")
    print("les noms ne doivent comporter aucun espace...")
    for i in range(saisie) :
        name = demander_saisir_mot(f"entrer le nom du joueur {i+1} : ")
        player = Player(name,empty_grid)
        players.append(player)

    return players

def set_turn(player : Player) -> list:
    """permet de simuler un tour de jeu
    args : player : Player - joueur en cours
    return : list Dees - la liste de dées a la fin du tour"""
    final_dees = []
    dees_list = []

    for i in range(3) :
        input(f"{player.name} appuyer sur une touche pour votre lancer n°{i+1} de dés")
        dees = final_dees.copy()
        dees += player.throw_dees(5-len(final_dees))
        if(i<2) :
            print(f"""{player.name} vous obtenez : 
[{dees[0].point}][{dees[1].point}][{dees[2].point}][{dees[3].point}][{dees[4].point}]
 1  2  3  4  5 """ )
            dees_list = entrer_une_liste_de_chiffres("entrer les des à conserver séparé par un espace : ",5)
            dees_list = set(dees_list)
            final_dees = []
            for dee in dees_list :
                final_dees.append(dees[dee-1])
            
            final_dees.sort()
            if(len(final_dees) == 5) :
                break
    dees.sort()
    print(f"""{player.name} vous obtenez : 
[{dees[0].point}][{dees[1].point}][{dees[2].point}][{dees[3].point}][{dees[4].point}]""")
    return dees

def final_score(players):
    """affiche les scores et retourne la personne victorieuse
    args : players : list Player - liste de joueurs"""

    print("la partie est terminée, voici les scores : ")
    score=0
    for player in players :
        if score < player.grid["total"] :
            score = player.grid["total"]
        print(f"{player.name} vous obtebez le score de {player.grid["total"]} points.")

    if (Player.nb_player>1) :
        for player in players and score == player.grid["total"] :
            print(f"BRAVO!!! {player.name} vous etes victorieux.")


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

players = ask_players()
print("la partie peut commencer...")

while True :
    for i in range(len(players)) :
        dees = set_turn(players[i])
        check_dees(dees, players[i])
        players[i].end_of_top()
        players[i].get_total()
        players[i].print_score()
    
    if players[0].end_of_game():
            break

final_score(players)

    


     
    

    





