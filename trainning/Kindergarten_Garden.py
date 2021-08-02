from random import randint

plants = {1: "grass", 2:"clover", 3:"radishes", 4: "violets"}
children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Distribution:

    """it distributes for each child in the list, alphabetically, to its due plant"""
    def __init__(self, plants, children):
        self.plants =  plants.values        
        self.children = sorted(children)
        
    
    def random_num(self, plants):
        new_plants = []
        for i in range(0, 3):
            new_plants.append(plants[randint(0,3)])
        return new_plants
            

    def distribution(self, plants, children):
        for child in self.children:
            print(f"the plants of {child} are : {random_num(plants)}")
            

distribution_plant = Distribution(plants, children)  
print(distribution_plant)