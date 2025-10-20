# This file adds mood to feeling words with emoji and a simple summary.

monday_mood = 0
tuesday_mood = 0
wednesday_mood = 0
thursday_mood = 0
friday_mood = 0
saturday_mood = 0
sunday_mood = 0

print("Mood Tracker")
print("1 Monday  2 Tuesday  3 Wednesday  4 Thursday  5 Friday  6 Saturday  7 Sunday")

day_number = int(input("Day number: "))
mood = int(input("Mood 1 to 10: "))

if mood <= 2:
    mood_word = "really down 😢"
elif mood <= 4:
    mood_word = "a bit low 🙁"
elif mood <= 6:
    mood_word = "so-so 😐"
elif mood <= 8:
    mood_word = "pretty good 🙂"
else:
    mood_word = "super happy 🤩"

if day_number == 1:
    monday_mood = mood
elif day_number == 2:
    tuesday_mood = mood
elif day_number == 3:
    wednesday_mood = mood
elif day_number == 4:
    thursday_mood = mood
elif day_number == 5:
    friday_mood = mood
elif day_number == 6:
    saturday_mood = mood
elif day_number == 7:
    sunday_mood = mood

print("You recorded mood:", mood)
print("Your feeling is:", mood_word)