class Building:

    total = 0
    def __init__(self, floors = 0):
        Building.total += 1
        self.floors = floors
    def __str__(self):
        return f'{self.floors}-этажный дом'

for i in range(1, 41):
    new_building = Building(i)
    print(new_building)
print ('Всего домов:', Building.total)



