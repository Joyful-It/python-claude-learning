class Pet:
    def __init__(self,name,color,):
        self.name=name
        self.color=color
    def play(self):
        print(f"{self.name} is playing")
        
mimi=Pet("mimi","red")
mimi.play()