import random

class Character (object):

    MAX_DEXTERITY = 100
    
    def __init__ (self, name, hit_points, strength, dexterity):

        self.name = name
        self.hit_points = int(hit_points)
        self.strength = strength
        self.dexterity = dexterity
        
    def attack (self, enemy):

        success = random.randint(1,100)


        if success <= 50+(int(self.dexterity) - int(enemy.dexterity)):
            dmg = random.randint(1, int(self.strength))
            enemy.hit_points-= dmg
            print("%s hit %s for %d" % (self.name, enemy.name, dmg))

        else:
            print("%s missed %s" % (self.name, enemy.name))
        
    def die (self):
        print("%s has died!" % (self.name))
        
    def __str__ (self):

        return("%s %s %s %s %s %s %s %s" % ("Name:" , self.name, "; Hitpoints" , self.hit_points, "; Strength",  self.strength, "; Decterity" , self.dexterity))

class CharacterList (object):

    def __init__ (self, file_name):


        self.choices = []
        file = open(file_name, "r")
        for line in file:
            list = line.split(",")
            c = Character(list[0], list[1], list[2], list[3])
            self.choices.append(c)
    
    def print_list (self):
        for c in self.choices:
            print(str(c))
    
    def get_and_remove_character (self, i):
        '''
        Gets and returns the "ith" Character from the list, then removes the
        character from the list.  (Doing so prevents the user and computer from
        using the same character.
        '''

        a = self.choices[i]

        del (self.choices[i])

        return a






    def get_random_character (self):
        character = random.randrange(len(self.choices))
        # if character == 0:
        #     return list[0]
        # elif character == 1:
        #     return list[1]
        # elif character == 2:
        #     return list[2]
        # elif character == 3:
        #     return list[3]

        return self.choices[character]


    
    def get_number_of_characters (self):
        return len(self.choices)
        # ''' Returns the number of characters in the list. '''

