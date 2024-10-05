from Dee import Dee

class Player :
    """Classe permettant de créer un joueur
    défini par son nom et l'etat de sa grille de jeu"""
    nb_player=0

    def __init__(self, name, grid) :
        self.__set_name(name)
        self.__set_grid(grid)
        Player.nb_player +=1

    def __get_name(self):
        return self.__name

    def __set_name(self, value):
        if type(value) != type(" "):
            raise ValueError("le nom doit etre une chaine")
        self.__name = value

    def __get_grid(self):
        return self.__grid

    def __set_grid(self, value):
        if type(value) != type({}) :
            raise ValueError("la grille doit etre un dictionnaire")
        self.__grid = value

    name = property(__get_name, __set_name, None, """""")
    grid = property(__get_grid, __set_grid, None, """""")

    def __str__(self):
        return f"le joueur est {self.name}"
    
    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name
    
    def throw_dees(self,n=5) -> list [int]:
        """génère un jet de n dées donc à une action du joueur"""
        new_dees = []
        for i in range(n) :
            dee = Dee()
            dee.throw()
            new_dees.append(dee)
        return new_dees
        
    def end_of_top(self) -> bool:
        """return True si la partie haute est terminée et False sinon"""
        top_points = 0
        item=""
        for item in self.grid :
            if item.isdigit() :
                if self.grid[item]==None :
                    return False
                else :
                    top_points += self.grid[item]
        
        if top_points>=63 :
            self.grid["bonus"] = 35
        else :
            self.grid["bonus"] = 0
        return True

    def get_total(self):
        """calcul le score total"""
        all_points = 0
        for item in self.grid :
            if self.grid[item]!=None and item!="total":
                all_points += self.grid[item]
        self.grid["total"] = all_points
     
    def end_of_game(self) -> bool:
        """return True si la partie est terminée et False sinon"""
        for item in self.grid :
            if self.grid[item]==None :
                return False
        return True
    
    def print_score(self):
        """imprime la grille de jeu"""
        print(f"grille de {self.name} : ")
        print(f"1 = {self.grid["1"]}, 2 = {self.grid["2"]}, 3 = {self.grid["3"]}, 4 = {self.grid["4"]}, 5 = {self.grid["5"]}, 6 = {self.grid["6"]}, bonus = {self.grid["bonus"]}")    
        print(f"brelan = {self.grid["brelan"]}, carre = {self.grid["carre"]}, full = {self.grid["full"]}, petite suite = {self.grid["petite_suite"]}, grande suite = {self.grid["grande_suite"]}")
        print(f"yahtzee = {self.grid["yahtzee"]}, chance = {self.grid["chance"]}, bonus yahtzee = {self.grid["bonus_yahtzee"]}, total = {self.grid["total"]}")

    @classmethod
    def return_nb_players (cls):
        """retourne le nombre de joueur créé."""
        print(f"il y a {Player.nb_player} joueur(s).")

        
         
