#This is a clue game and we use logical operators to determine the answer
#this game I learnt from CS50 introduction to AI
#The game goes like we have given 3 places and 3 people and 3 weapons and we have some clues using them we need to find who did murder at which place
import termcolor
from logic import *
mustrad = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("mrscr")
characters = [mustrad,plum,scarlet]
ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom,kitchen,library]
knife = Symbol("knife")
revolver = Symbol("Revolver")
wrench = Symbol("Wrench")
weapons = [knife,revolver,wrench]
symbols = characters+rooms+weapons
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge,symbol):
            termcolor.cprint(f"{symbol}:YES","green")
        elif not model_check(knowledge,Not(symbol)):
            print(f"{symbol}:MAYBE")
knowledge = And(
    Or(mustrad,plum,scarlet),
    Or(ballroom,kitchen,library),
    Or(knife,revolver,wrench)
)

knowledge.add (Not(mustrad))
#library adds something
knowledge.add(Not(ballroom))
knowledge.add(Not(revolver))
knowledge.add(Or(
    Not(scarlet),Not(library),Not(wrench)
))
knowledge.add(Not(plum))
knowledge.add(Not(knife))
check_knowledge(knowledge)

