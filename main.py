# This is the main program for my mood tracker
# The purpose of the prototype is to be able to track user's mood daily with a scale of 1 to 10
# The user can optionally write a short note about the day
# User will also be able to see a line graph of their mood trend over the week
# The end of the week, the user can see a summary of their moods and notes
# Finally, the user can save all data to a text file and a PDF graph file
# By doing this, user can understand their mood patterns better
# Questions and feedbacks are welcome!

import matplotlib.pyplot as plt  # we use matplotlib to make a line graph later

# Greeting message to the user
print("Hello, welcome to my mood tracker!")  # say hello
print("I hope you're having a good day :)")  # friendly message

# Create variables to save mood number for each day
# Here we set all to 0 first because user has not recorded anything yet
monday_mood = 0
tuesday_mood = 0
wednesday_mood = 0
thursday_mood = 0
friday_mood = 0
saturday_mood = 0
sunday_mood = 0

# Create variables to save note for each day
# Here we set all to empty string "" first
monday_note = ""
tuesday_note = ""
wednesday_note = ""
thursday_note = ""
friday_note = ""
saturday_note = ""
sunday_note = ""

# This is the main loop
# I use while True because I want the menu to keep showing until the user exits
# I learned this loop idea from:
# EyeHunt. (2021). How to keep asking for user input Python | Example code. https://tutorial.eyehunts.com/python/how-to-keep-asking-for-user-input-python-example-code/
# Reddit. (2025). Creating a loop until user enters a specific value to exit program. https://www.reddit.com/r/learnpython/comments/fc2ors/creating_a_loop_until_user_enters_a_specific/
# GeeksforGeeks. (2025). How to use while True in Python. https://www.geeksforgeeks.org/python/how-to-use-while-true-in-python/
while True:
    print("")  # empty line to make the menu look clean
    print("--- Mood Tracker Options ---")  # menu title
    print("1. Record Mood")
    print("2. View Summary")
    print("3. Plot Mood Graph (show)")
    print("4. Save All and Exit")

    choice_input = input("Choose option: ")  # ask user to choose
    # I learned here that input() always gives string
    # If I do not change to int, the program will crash when I compare
    # I learned this from error message and tutorial: https://www.w3schools.com/python/python_datatypes.asp
    choice = int(choice_input)

    # Option 1: Record mood
    # User should choose which day first
    if choice == 1:
        print("") # new line
        print("Which day is it?")
        print("1 - Monday")
        print("2 - Tuesday")
        print("3 - Wednesday")
        print("4 - Thursday")
        print("5 - Friday")
        print("6 - Saturday")
        print("7 - Sunday")

        # I ask user to input the day number
        # I change it to int to use it in condition
        day_input = input("Type the number of the day: ")
        day_num = int(day_input)

        # Then I ask for mood number
        # Here also must change to int, or it will not work in the if condition below
        mood_input = input("Mood from 1 to 10: ")
        mood = int(mood_input)

        # Determine mood word
        # Feedback from class tutor: not just show number, but show mood feeling word
        # I add emoji to make it more easy to understand and fun
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

        # Ask user for short note
        note_input = input("Short note: ")

        # Save the mood and note to correct day
        # I use if condition to match the input number
        # I learn this logic from examples in class and tutorial: https://www.w3schools.com/python/python_conditions.asp
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
        else: # My friend tested with invalid number 8, so I add this to catch invalid input
            print("Invalid day number")

        # Print what the user recorded as a quik summary
        # I do this to help user check and to debug myself
        print("Your mood number is:", mood)
        print("Your feeling is:", mood_word)
        print("Your note is:", note_input)

    # Option 2: Summary
    # I use print to show all records
    # This helps user check their data and also helps me see bugs quickly
    elif choice == 2:
        print("") # new line
        print("--- Weekly Summary ---")
        print("Monday Mood:", monday_mood, "Note:", monday_note)
        print("Tuesday Mood:", tuesday_mood, "Note:", tuesday_note)
        print("Wednesday Mood:", wednesday_mood, "Note:", wednesday_note)
        print("Thursday Mood:", thursday_mood, "Note:", thursday_note)
        print("Friday Mood:", friday_mood, "Note:", friday_note)
        print("Saturday Mood:", saturday_mood, "Note:", saturday_note)
        print("Sunday Mood:", sunday_mood, "Note:", sunday_note)

    # Option 3: Plot graph using matplotlib
    # I learn how to plot a line chart from Matplotlib official doc and tutorial:
    # Matplotlib Development Team. (2025). https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    # W3Schools. (2025). https://www.w3schools.com/python/matplotlib_intro.asp
    # Real Python. (2025). https://realpython.com/read-write-files-python/
    elif choice == 3:
        x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # Create x axis labels with an array
        y = [monday_mood, tuesday_mood, wednesday_mood, thursday_mood, friday_mood, saturday_mood, sunday_mood] # Create y axis values with an array

        plt.plot(x, y, marker='o') # plot the line with circle markers
        plt.ylim(0, 10) # set y axis limit; 10 is the max mood, 0 is the default min when user has not recorded
        plt.title("Weekly Mood Trend") # title of the graph
        plt.xlabel("Day")   # x axis label
        plt.ylabel("Mood (1-10)") # y axis label
        plt.grid(True) # add grid for better visualization
        plt.show()

    # Option 4: Save to file and exit
    # I use file.write to save my record
    # I learned how to use write() and '\n' from:
    # W3Schools. https://www.w3schools.com/python/python_file_write.asp
    # Programiz. https://www.programiz.com/python-programming/file-operation
    # Web Physics Utah. https://web.physics.utah.edu/~detar/lessons/python/fileio_formatting/node14.html
    # freeCodeCamp. https://www.freecodecamp.org/news/print-newline-in-python/
    elif choice == 4:
        file = open("mood_week.txt", "w")
        file.write("Monday Mood: " + str(monday_mood) + " Note: " + monday_note + "\n") # we use \n to make new line
        #\n is a escape character. Lerned about escape characters from:
        #https://www.geeksforgeeks.org/python/python-new-line-add-print-a-new-line/
        file.write("Tuesday Mood: " + str(tuesday_mood) + " Note: " + tuesday_note + "\n") # we use str to convert int to string. Leraned from:
        #https://www.google.com/url?q=https://www.shecodes.io/athena/2142-converting-an-integer-to-string-in-python&sa=D&source=docs&ust=1761144207339882&usg=AOvVaw1ewUlB067DpaLcVd19Ex7a
        file.write("Wednesday Mood: " + str(wednesday_mood) + " Note: " + wednesday_note + "\n")
        file.write("Thursday Mood: " + str(thursday_mood) + " Note: " + thursday_note + "\n")
        file.write("Friday Mood: " + str(friday_mood) + " Note: " + friday_note + "\n")
        file.write("Saturday Mood: " + str(saturday_mood) + " Note: " + saturday_note + "\n")
        file.write("Sunday Mood: " + str(sunday_mood) + " Note: " + sunday_note + "\n")
        file.close()

        # I learned how to save plot as PDF from:
        # Matplotlib Development Team. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
        plt.figure()
        #Same as above, we just move x and y values directly into plt.plot()
        plt.plot(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], # x axis labels
                 [monday_mood, tuesday_mood, wednesday_mood, thursday_mood, friday_mood, saturday_mood, sunday_mood],# y axis values
                 marker='o') # plot the line with circle markers
        plt.ylim(0, 10) #set y axis limit; 10 is the max mood, 0 is the default min when user has not recorded
        plt.title("Weekly Mood Trend") # title of the graph
        plt.xlabel("Day") # x axis label
        plt.ylabel("Mood (1-10)") # y axis label
        plt.grid(True)  # add grid for better visualization
        plt.savefig("mood_week_graph.pdf") # save as PDF
        plt.close() #remeber to close the plot

        print("Text saved as mood_week.txt")
        print("Graph saved as mood_week_graph.pdf")
        print("All saved. Bye!")

        # Important to use break to make while true loop to exit
        # We usually use a index number i for for loop, or while loop with condition
        # Here we can't use a index number since we are not sure how many times user will use the program
        # So we use while true to create an infinite loop, and use break to exit when needed
        break

    else:
        # I learned about input validation after my friend typed 5 and program froze
        # In future I want to add better input checks
        print("Invalid choice")
