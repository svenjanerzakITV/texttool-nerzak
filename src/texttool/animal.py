class Animal:
    def __init__(self, name: str):
        print(f"Creating an animal named {name}")
        self.name = name
    
    def __str__(self):
        return(f"I am an animal named {self.name}")
    
    @staticmethod
    def is_animal(obj: object) -> bool:
        return isinstance(obj, Animal)

class Bird(Animal):
    def whoami(self) -> str:
        return f"I am a bird. My name is irrelevant."