import random

rank = random.choice(('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'))
suit = random.choice(('Clubs', 'Diamonds', 'Hearts', 'Spades'))

print("The card you picked is the",rank, "of", suit)
