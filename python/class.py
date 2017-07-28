class Musician:
    def __init__(self,name,genera):
        self.name = name
        self.genera = genera

    def description(self):
        return "My name is " + self.name + "and I play" + genera + self.genera

mozart = Musician('Amadeaus Mozart', 'classical')
beyonce = Musician('Beyonce', 'R&B')
pit_bull = Musician('Pitbull','Latin Pop')

print mozart.description()
