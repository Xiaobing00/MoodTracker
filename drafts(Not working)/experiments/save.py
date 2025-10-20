# This file tests saving mood to txt file.

mood = 7
note = "Feeling okay today."

file = open("test_mood.txt", "w")
file.write("Mood: " + str(mood) + "\n")
file.write("Note: " + note + "\n")
file.close()

print("File saved.")