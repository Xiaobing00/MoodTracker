# This is the main program for my mood tracker
# English comment only

import matplotlib.pyplot as plt

# Greeting
print("Hello, welcome to my mood tracker!")
print("I hope you're having a good day :)")

# Initialize mood and note variables
monday_mood = 0
tuesday_mood = 0
wednesday_mood = 0
thursday_mood = 0
friday_mood = 0
saturday_mood = 0
sunday_mood = 0

monday_note = ""
tuesday_note = ""
wednesday_note = ""
thursday_note = ""
friday_note = ""
saturday_note = ""
sunday_note = ""

# Main options
while True:
    print("")
    print("--- Mood Tracker Options ---")
    print("1. Record Mood")
    print("2. View Summary")
    print("3. Plot Mood Graph (show)")
    print("4. Save All and Exit")

    choice_input = input("Choose option: ")
    choice = int(choice_input)

    # Option 1: Record mood
    if choice == 1:
        print("")
        print("Which day is it?")
        print("1 - Monday")
        print("2 - Tuesday")
        print("3 - Wednesday")
        print("4 - Thursday")
        print("5 - Friday")
        print("6 - Saturday")
        print("7 - Sunday")

        day_input = input("Type the number of the day: ")
        day_num = int(day_input)

        mood_input = input("Mood from 1 to 10: ")
        mood = int(mood_input)

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

        note_input = input("Short note (press Enter to skip): ")

        if day_num == 1:
            monday_mood = mood
            monday_note = note_input
            print("You recorded Monday.")
        elif day_num == 2:
            tuesday_mood = mood
            tuesday_note = note_input
            print("You recorded Tuesday.")
        elif day_num == 3:
            wednesday_mood = mood
            wednesday_note = note_input
            print("You recorded Wednesday.")
        elif day_num == 4:
            thursday_mood = mood
            thursday_note = note_input
            print("You recorded Thursday.")
        elif day_num == 5:
            friday_mood = mood
            friday_note = note_input
            print("You recorded Friday.")
        elif day_num == 6:
            saturday_mood = mood
            saturday_note = note_input
            print("You recorded Saturday.")
        elif day_num == 7:
            sunday_mood = mood
            sunday_note = note_input
            print("You recorded Sunday.")
        else:
            print("Invalid day number")

        # Print
        print("Your mood number is:", mood)
        print("Your feeling is:", mood_word)
        print("Your note is:", note_input)

    # Option 2: See summary
    elif choice == 2:
        print("")
        print("--- Weekly Summary ---")
        print("Monday Mood:", monday_mood, "Note:", monday_note)
        print("Tuesday Mood:", tuesday_mood, "Note:", tuesday_note)
        print("Wednesday Mood:", wednesday_mood, "Note:", wednesday_note)
        print("Thursday Mood:", thursday_mood, "Note:", thursday_note)
        print("Friday Mood:", friday_mood, "Note:", friday_note)
        print("Saturday Mood:", saturday_mood, "Note:", saturday_note)
        print("Sunday Mood:", sunday_mood, "Note:", sunday_note)

    # Option 3: Plot graph
    elif choice == 3:
        x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        y = [monday_mood, tuesday_mood, wednesday_mood, thursday_mood, friday_mood, saturday_mood, sunday_mood]

        plt.plot(x, y, marker='o')
        plt.ylim(0, 10)
        plt.title("Weekly Mood Trend")
        plt.xlabel("Day")
        plt.ylabel("Mood (1-10)")
        plt.grid(True)
        plt.show()

    # Option 4: Save and exit
    elif choice == 4:
        file = open("mood_week.txt", "w")
        file.write("Monday Mood: " + str(monday_mood) + " Note: " + monday_note + "\n")
        file.write("Tuesday Mood: " + str(tuesday_mood) + " Note: " + tuesday_note + "\n")
        file.write("Wednesday Mood: " + str(wednesday_mood) + " Note: " + wednesday_note + "\n")
        file.write("Thursday Mood: " + str(thursday_mood) + " Note: " + thursday_note + "\n")
        file.write("Friday Mood: " + str(friday_mood) + " Note: " + friday_note + "\n")
        file.write("Saturday Mood: " + str(saturday_mood) + " Note: " + saturday_note + "\n")
        file.write("Sunday Mood: " + str(sunday_mood) + " Note: " + sunday_note + "\n")
        file.close()

        plt.figure()
        plt.plot(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                 [monday_mood, tuesday_mood, wednesday_mood, thursday_mood, friday_mood, saturday_mood, sunday_mood],
                 marker='o')
        plt.ylim(0, 10)
        plt.title("Weekly Mood Trend")
        plt.xlabel("Day")
        plt.ylabel("Mood (1-10)")
        plt.grid(True)
        plt.savefig("mood_week_graph.pdf")
        plt.close()

        print("Text saved as mood_week.txt")
        print("Graph saved as mood_week_graph.pdf")
        print("All saved. Bye!")
        break

    else:
        print("Invalid choice")