class Pokemon:
  def __init__(self, name, type, skill):
    self.name = name
    self.type = type
    self.skill = skill

  def Attack(self, damage):
    return f"Pikachu attack using {self.skill} inflicting {damage} life points"

  def __str__(self):
    return f"Pokemon's name is {self.name} and pokemon type is {self.type}"

pikachu = Pokemon("Pikcachu", "Electric", "Thunder Bolt")
charmander = Pokemon("Charmander", "Fire", "Burn")


print(pikachu.type)
print(pikachu.skill)

pikachu.skill = "Iron Fail"
print(pikachu.skill)

print(pikachu.Attack(10))


print(pikachu)


"""class Pokemon:
  def __init__(self, name, type, skill):
    self.name = name
    self.type = type
    self.skill = skill

  def Attack(self, damage):
    return f"Pikachu attack using {self.skill} inflicting {damage} life points"

  def __str__(self):
    return f"Pokemon's name is {self.name} and pokemon type is {self.type}"

pikachu = Pokemon("Pikcachu", "Electric", "Thunder Bolt")
charmander = Pokemon("Charmander", "Fire", "Burn")


print(pikachu.type)
print(pikachu.skill)

pikachu.skill = "Iron Fail"
print(pikachu.skill)

print(pikachu.Attack(10))


print(pikachu)"""
