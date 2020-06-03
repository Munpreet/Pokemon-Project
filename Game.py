class Pokemon:
  def __init__(self, name, level, type, is_knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = self.level * 5
    self.current_health = self.max_health
    self.is_knocked_out = is_knocked_out
    print("""
    New Pokemon created! 
    Name: {}
    Level: {}
    Type: {}
    Max Health: {}
    Current Health: {}
    Knock Out status: {}""".format(self.name, self.level, self.type, self.max_health, self.current_health, self.is_knocked_out))


  def greater_class(self, other_pokemon):
    if self.type == other_pokemon.type:
      return "Both pokemon are of same type"
    elif self.type == "Fire" and other_pokemon.type == "Water":
      return other_pokemon.name
    elif self.type == "Water"  and other_pokemon.type == "Fire":
      return self.name
    elif self.type == "Fire"  and other_pokemon.type == "Grass":
      return self.name
    elif self.type == "Grass"  and other_pokemon.type == "Fire":
      return other_pokemon.name
    elif self.type == "Water"  and other_pokemon.type == "Grass":
      return other_pokemon.name
    elif self.type == "Grass"  and other_pokemon.type == "Water":
      return self.name


  def lose_health(self, losing_health_point)  :
    self.current_health = max(0, self.current_health - losing_health_point)
    if self.current_health == 0:
      self.knock_out()
    else:
      print("{} Pokemon has lost {} health points.".format(self.name, losing_health_point))

  def gain_health(self, gaining_health_point)  :
    if self.current_health == 0:
      self.current_health = min(self.max_health, self.current_health + gaining_health_point)
      self.revive()
    else:
      self.current_health = min(self.max_health, self.current_health + gaining_health_point)
      print("{} Pokemon has gained {} health points".format(self.name, gaining_health_point))

  def knock_out(self):
    self.is_knocked_out = True
    print("Pokemon {} has been knocked out".format(self.name))

  def revive(self)  :
    self.is_knocked_out = False
    print("Pokemon {} has been revived".format(self.name))

  def attack(self, other_pokemon):
    if self.is_knocked_out == True or other_pokemon.is_knocked_out == True:
      print("Unable to attack as one of the pokemons is knocked out.")
    else:  
      print("{} has attacked {}".format(self.name, other_pokemon.name))
      if self.greater_class(other_pokemon) == "Both pokemons are of same type":
        print("The attack is moderately effective")
        other_pokemon.lose_health(self.level)      
      elif  self.greater_class(other_pokemon) == self.name:
        print("The attack is very effective")
        other_pokemon.lose_health(2 * self.level)
      else:
        print("The attack is not effective")
        other_pokemon.lose_health(self.level / 2)   


class Trainer:
  def __init__(self, name, potions, pokemons, currently_active):
    self.name = name
    self.potions = potions
    if len(pokemons) > 3:
      print("Maximum 6 Pokemons allowed!")
    else:
      self.pokemons = pokemons
      self.pokemon_list = []
      for a in pokemons:
        self.pokemon_list.append(a.name)

    self.currently_active = self.pokemons[currently_active] 
    self.curr_active = self.pokemon_list[currently_active] 
    print("""
    New Trainer created! 
    Name: {}
    Number of potions: {}
    List of Pokemons: {}
    Active Pokemon: {}""".format(self.name, self.potions, self.pokemon_list, self.curr_active))


  def use_potion(self)    :
    if self.potions == 0:
      print("No potions left")
    elif self.currently_active.current_health == self.currently_active.max_health:
      print("Active Pokemon is already having full health")
    else:
      print("{} has used 1 potion".format(self.name))
      self.currently_active.gain_health(10)  
      self.potions -= 1
      
  def attack_trainer(self, other_trainer):
    print("{} has launched an attack with {} on {} of {}".format(self.name, self.curr_active, other_trainer.curr_active, other_trainer.name))
    self.currently_active.attack(other_trainer.currently_active)

  def switch_pokemon(self, new_num):
    if self.pokemons[new_num].is_knocked_out == True:
      print("Unable to switch pokemon as the concerned pokemon is knocked out!") 
    else:
      print("{} has switched his active pokemon from {} to {}".format(self.name, self.curr_active, self.pokemon_list[new_num]))
      self.currently_active = self.pokemons[new_num]  


class Charmander(Pokemon):
  def __init__(self, name, level, type, is_knocked_out, experience):
    super().__init__(name, level, type, is_knocked_out)
    if experience >=10:
      print("Experience must be from 0 - 5")
    else:
      self.experience = experience
    

  def update_experience(self):
    self.experience += 1
    if self.experience ==10:
      self.experience = 0
      self.level += 1

  def attack(self, other_pokemon)    :
    super().attack(other_pokemon)
    if self.is_knocked_out == False and other_pokemon.is_knocked_out == False:
      self.update_experience()
      if hasattr(other_pokemon, "update_experience") == True:
        other_pokemon.update_experience()






pikachu = Pokemon("Pikachu", 10, "Fire", is_knocked_out = False)
may = Pokemon("May", 18, "Water", is_knocked_out = True)
lillie = Pokemon("Lillie", 9, "Grass", is_knocked_out = False)

charmander = Charmander("Charmander", 20, "Fire", False, 0)


Dragon = Trainer("Dragon", 5,  [pikachu, may], currently_active = 0)
Dad = Trainer("Dad", 10, [pikachu, may, lillie], currently_active = 2)