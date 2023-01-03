# Hangman
import random

#generování náhodného slova

names = ("Hermione Granger", "Ronald weasley", "Fred Weaslye", "George Weasley",
"Ginevra Weasley", "Molly Weasley", "Arthur Weasley", "Percy Weasley", "Harry Potter",
"James Potter", "Dobby", "Kreacher", "Sirius Black", "Albus Dumbledore", "Fillius Flitwick",
"Rubeus Hagrid", "Minerva McGonagall", "Remus Lupin", "Sybill Trelawney", "Severus Snape",
"Gilderoy Lockhart", "Errol", "Fawkes", "Buckbeak", "Hedwig", "AKA Nearly Headless Nick",
"Salazar Slytherin", "Rowena Ravenclaw", "Helga Hufflepuff", "Godric Gryffindor", "Vincent Crabbe"
"Gregory Goyle", "Neville Longbottom", "Draco Malfoy", "Igor Karkaroff", "Peter Pettigrew",
"Lucius Malfoy", "Bellatrix Lestrange", "Barty Crouch Jr.", "Tom Marvolo Riddle - Lord Voldemort")

random_word = random.choice(names)
print(random_word)

#Podrtžítka (z kolika to bude pismen)
hidden_word = [len(random_word) * "_"]

letter = input("Enter a possible letter:\n").lower()
for index in range(0, len(random_word)):
    if letter == random_word[index]:
        hidden_word[index] = letter

print(hidden_word)