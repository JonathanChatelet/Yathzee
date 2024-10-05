def demander_saisie_nombre(invite : str) -> int :
    """demande la saisi d'un nombre, en evitant les caractère autre que numérique"""
    while True:
        user_input = input(invite)
        try:
            result = int(user_input)
            return result
        except ValueError:
            print("Seul les caractères [0-9] sont autorisés")

def demander_saisie_nombre_borne(invite : str, minimum=1, maximum=10, concat = True) -> int:
    """demande la saisi d'un nombre, en evitant les caractère autre que numérique et compris entre minimum et maximum"""
    if concat:
        invite += f" entre {minimum} et {maximum} "
    while True:
        nombre_input = demander_saisie_nombre(invite)
        if minimum <= nombre_input <= maximum:
            return nombre_input

def demander_saisie_nombre_positif(invite : str) ->int:
    """demande la saisi d'un nombre, en evitant les caractère autre que numérique et positif"""
    invite += " (positif) "
    while True:
        nombre_input = demander_saisie_nombre(invite)
        if nombre_input > 0:
            return nombre_input

def demander_saisir_mot(invite : str) -> str :
    """demande de saisir uniquement un mot"""
    while True:
        saisie = input(invite)
        if type(saisie) == type(" ") and " " not in saisie :
            return saisie
        print("Merci d'entrer un nom sans espace")

def demander_O_N(invite : str) -> str:
    """demande une réponse oui ou non"""
    while True:
        saisie = input(invite)
        if type(saisie) == type(" ") and (saisie.lower() =='o' or saisie.lower() =='n') :
            return saisie
        print("Merci d'entrer o ou n")

def entrer_une_liste_de_chiffres(invite : str, max=5) -> list:
    """permet de verifier la saisie d'une liste de chiffre
    args : invite : str - la phrase à afficher, max = le choix max
    return : list de int - liste de chiffre <= max """
    figure_list = []
    while True:
        saisie = input(invite)
        if(saisie=="" or saisie.isspace()) :
            return []
        if type(saisie) == type(" ") :
            figures = saisie.split(" ")
            try :
                for figure in figures :
                    if 1<=int(figure)<=max :
                        figure_list.append(int(figure))
                    else : 
                        raise ValueError("")
            except : 
                print("veuillez respecter la saisie...")
            else :
                return figure_list
    
