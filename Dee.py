import random

class Dee :
    """Classe permettant de créer un dé associé à une valeur"""
    def __init__(self, point=1) :
        self.__set_point(point)

    def __get_point(self):
        return self.__point

    def __set_point(self, value):
        if type(value) != type(1) and not (1 <= value <= 6):
            raise ValueError("le nombre de point doit être compris entre 1 et 6")
        self.__point = value
    
    point = property(__get_point, __set_point, None, """""")
    
    def __str__(self):
        return f"la valeur du dé est {self.point}"
    
    def __eq__(self, other):
        return type(self) == type(other) and self.point == other.point
    
    def __lt__(self, other):
        return type(self) == type(other) and self.point<other.point
    
    def __gt__(self, other):
        return type(self) == type(other) and self.point>other.point
    
    def __leq__(self, other):
        return type(self) == type(other) and self.point<=other.point
    
    def __geq__(self, other):
        return type(self) == type(other) and self.point>=other.point
    
    def __neq__(self, other):
        return type(self) == type(other) and self.point!=other.point
    
    def throw(self) -> int :
        """permet de retourner une valeur aléatoire au dé"""
        self.point = random.randint(1,6)

    
    

