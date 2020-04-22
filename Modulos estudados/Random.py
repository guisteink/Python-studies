#Modulo random
import random

print("\nRandom")
for i in range(5):
    print(random.random()) #gera numeros de 0 a 1, randomicos e quebrados

print("\nUniform")
for i in range(5):
    print(random.uniform(5,10)) #gera numeros de x à y, randomicos e quebrados

print("\nRandint")
for i in range(5):
    print(random.randint(1,100)) #gera numerso de x à y, randomicos e inteiros

jogadas = ['pedra','papel','tesoura']
print("\nChoice")
for i in range(5):
    print(random.choice(jogadas))

cartas = ['AZ','2','3','4','5','6','7','8','9','10','VALETE','DAMA','REI']
print("\nShuffle")
print(cartas)
random.shuffle(cartas)
print(cartas)

