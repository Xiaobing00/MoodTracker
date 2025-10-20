# This is the main program for my mood tracker
# The purpose of the prototype is to be able to track user's mood daily with a scale of 1 to 10
# The user can optionally write a short note about the day
# The end of the week, the user can see a summary of their moods and notes
# By doing this, user can understand their mood patterns better
# Questions and feedbacks are welcome!


import matplotlib.pyplot as plt

# Greeting
print("Hello, welcome to my mood tracker!")
print("I hope you're having a good day :)")

# Create mood and note variables
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
# 3 options: 1. Record mood, 2. See summary, 3. Plot graph, 4. Save and exit
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
    # Use should choose the which day is it first from 1-7
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

        # Save the inputs in day_input
        day_input = input("Type the number of the day: ")
        # Type casting: convert string to integer
        day_num = int(day_input)

        #Save the mood in mood_input
        mood_input = input("Mood from 1 to 10: ")
        # Type casting: convert string to integer
        mood = int(mood_input)


        # Determine mood word. 
        # Feedback in class: We don't want to show the number only, we want to show actual word of the mood
        # I added emoji to each to make it more vivid
        if mood <= 2:
            mood_word = "really down 😢"
        elif mood <= 4:
            mood_word = "a bit low 🙁"
        elif mood <= 6:
            mood_word = "so so 😐"
        elif mood <= 8:
            mood_word = "pretty good 🙂"
        else:
            mood_word = "super happy 🤩"


        # Ask use if they want to write a short note
        note_input = input("Short note: ")


        # Check which day is it, save the mood and note to the corsponding variables
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

        # Print the user's input
        print("Your mood number is:", mood)
        print("Your feeling is:", mood_word)
        print("Your note is:", note_input)

    # Option 2: See summary to allow user to see which day is recorded and which is not
    elif choice == 2:
        print("") #new line
        print("--- Weekly Summary ---")
        print("Monday Mood:", monday_mood, "Note:", monday_note)
        print("Tuesday Mood:", tuesday_mood, "Note:", tuesday_note)
        print("Wednesday Mood:", wednesday_mood, "Note:", wednesday_note)
        print("Thursday Mood:", thursday_mood, "Note:", thursday_note)
        print("Friday Mood:", friday_mood, "Note:", friday_note)
        print("Saturday Mood:", saturday_mood, "Note:", saturday_note)
        print("Sunday Mood:", sunday_mood, "Note:", sunday_note)

    # Option 3: Plot graph using matplotlib
    # Reference:
    # Matplotlib Development Team. "matplotlib.pyplot.plot — Plotting in Pyplot." Matplotlib.org
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    # Tutorial used: https://matplotlib.org/stable/users/explain/quick_start.html
    # I follow tutorial example to learn how to plot line and show it
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
    # Reference:
    # Matplotlib Development Team. "matplotlib.pyplot.savefig — Save the current figure." Matplotlib.org
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    # Tutorial used: https://matplotlib.org/stable/users/explain/quick_start.html#save-figures
    # I learn how to save figure to pdf file from this tutorial
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