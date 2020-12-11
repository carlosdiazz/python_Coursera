class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category="reptile"

#print(Turtle.category)

class Snake(Animal):
    category="reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

print("----------------------------------------------------------------------------------")















#Lboratorio 1

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}


  def __init__(self,name):
    material = ""
    self.name = name


  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)

    
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"

class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")

sweatpants = pants("Sweatpants")

polo.add_item(polo.name, polo.material, 4)

sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


















class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        
        self.bottom=bottom
        self.top=top
        self.current=current
        pass
    
    def up(self):
        
        if self.current<self.top and self.current>=self.bottom:
            self.current+=1              
        pass
    
    def down(self):
        
        """Makes the elevator go down one floor."""
        if self.current>self.bottom and self.current<=self.top:
            self.current-=1
        pass
    
    def go_to(self, floor):
        self.floor=floor
        """Makes the elevator go to the specific floor."""
        
        if self.floor>=self.bottom and self.floor<=self.top:
            self.current=self.floor
        
        pass
    
    def __str__(self):
        
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)

