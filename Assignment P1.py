##Laila Grey
###Assignment P1:First GUI Development Project
####Graph User Interface Development


import tkinter as tk

# Function to update lblFrench text
#This is my function and varialbe that will define the numbers in French
#here I am coloring the font
#make label visible
def show_french(number):
    french_numbers = {1: "Un", 2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq"}
    lblFrench.config(text=french_numbers[number], fg="blue")
    lblFrench.pack()  

# Create main window
root = tk.Tk()
root.title("French Numbers")
root.geometry("300x250")
root.resizable(False, False)  # Removes maximize/minimize buttons (bonus)

# Instructions label
#here I am guiding the user to click which ever number to see it in French
lblInstructions = tk.Label(root, text="Click a number to see it in French:")
lblInstructions.pack()

# French word label (initially empty and hidden)
lblFrench = tk.Label(root, text="", font=("Arial", 14))
lblFrench.pack_forget()  # Starts hidden

# Buttons for numbers 1-5
#here I am ranging it from 1 to 6 because python will not read the 6
for i in range(1, 6):
    btn = tk.Button(root, text=str(i), command=lambda i=i: show_french(i))
    btn.pack()

# This is my Exit button and I used the object(name) from the chart on the assigment sheet 
btnExit = tk.Button(root, text="Exit", command=root.quit)
btnExit.pack()

# Run the GUI
# I got this code from stack overflow
#here is the website https://stackoverflow.com/questions/22698980/python-tkinter-why-is-it-root-mainloop-and-not-app-mainloop
root.mainloop()
