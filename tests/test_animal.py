import sys
sys.path.insert(0, "./src")

from texttool.animal import Animal
from texttool.animal import Bird

animal = Animal("Fluff")
bird = Bird("Feathers")

print(bird.whoami())
print(str(animal))