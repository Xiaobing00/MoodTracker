# This file uses if-else for days and mood recording, very basic.

monday_mood = 0
tuesday_mood = 0
wednesday_mood = 0
thursday_mood = 0
friday_mood = 0
saturday_mood = 0
sunday_mood = 0

print("Mood Tracker")
print("1 Monday  2 Tuesday  3 Wednesday  4 Thursday  5 Friday  6 Saturday  7 Sunday")

day_number = int(input("Type the number of the day: "))
mood = int(input("Type your mood 1 to 10: "))

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

print("Recorded mood number:", mood)