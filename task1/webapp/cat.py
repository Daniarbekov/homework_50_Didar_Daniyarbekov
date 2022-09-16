
from random import randint


class Cat:
    
    name = ''    
    age = 1
    mood = 40
    satiety = 40
    is_sleeping = False
    
    @staticmethod
    def play():
        chance = randint(1,3)
        if chance == 1:
            Cat.mood = 0 
        else:
            if not Cat.is_sleeping:
                Cat.mood += 15
                Cat.satiety -= 10
            else:  
                Cat.mood -= 5
                Cat.is_sleeping = False
        Cat.check()        
        
    @staticmethod
    def feed():
        if Cat.is_sleeping:
            pass
        else:
            Cat.satiety += 15
            if Cat.satiety > 100:
                Cat.mood -= 30
            else:
                Cat.mood += 5 
            Cat.check()

    @staticmethod
    def get_sleep():
        Cat.is_sleeping = True

    @staticmethod
    def check():
        if Cat.satiety > 100:
            Cat.satiety = 100
        if Cat.mood > 100:
            Cat.mood = 100
        if Cat.satiety < 0 :
            Cat.satiety = 0
        if Cat.mood < 0:
            Cat.mood = 0

    @staticmethod
    def set_img():
        if Cat.is_sleeping:
            return '/media/sleep.jpg'
        elif Cat.mood >=60:
            return '/media/happy.jpg'
        elif Cat.mood <= 10:
            return '/media/mad.jpg'
        elif Cat.mood < 40:
            return '/media/sad.jpg'
        elif Cat.mood >= 40:
            return '/media/ca.jpg'
        
        
