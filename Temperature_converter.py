import tkinter as tk
from functools import partial

# Declaration of global variable
temp_Val = "Celsius"

# Function to update result labels based on selected temperature unit
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp
    
    # Update result labels based on selected temperature unit
    if temp_Val == 'Celsius':
        f_label.config(text="Fahrenheit")
        k_label.config(text="Kelvin")
    elif temp_Val == 'Fahrenheit':
        f_label.config(text="Celsius")
        k_label.config(text="Kelvin")
    elif temp_Val == 'Kelvin':
        f_label.config(text="Fahrenheit")
        k_label.config(text="Celsius")

# Conversion of temperature
def convert_temp(f_entry, k_entry, inputn):
    temp = inputn.get()
    
    try:
        temp = float(temp)
        
        if temp_Val == 'Celsius':
            # Conversion from Celsius to Fahrenheit and Kelvin
            f = (temp * 9 / 5) + 32
            k = temp + 273.15
            f_entry.config(state=tk.NORMAL)  # Enable entry to update value
            k_entry.config(state=tk.NORMAL)  # Enable entry to update value
            f_entry.delete(0, tk.END)
            f_entry.insert(0, "%.1f" % f)
            k_entry.delete(0, tk.END)
            k_entry.insert(0, "%.2f" % k)

        elif temp_Val == 'Fahrenheit':
            # Conversion from Fahrenheit to Celsius and Kelvin
            c = (temp - 32) * 5 / 9
            k = (temp + 459.67) * 5 / 9
            f_entry.config(state=tk.NORMAL)  # Enable entry to update value
            k_entry.config(state=tk.NORMAL)  # Enable entry to update value
            f_entry.delete(0, tk.END)
            f_entry.insert(0, "%.1f" % c)
            k_entry.delete(0, tk.END)
            k_entry.insert(0, "%.2f" % k)

        elif temp_Val == 'Kelvin':
            # Conversion from Kelvin to Celsius and Fahrenheit
            c = temp - 273.15
            f = (temp * 9 / 5) - 459.67
            f_entry.config(state=tk.NORMAL)  # Enable entry to update value
            k_entry.config(state=tk.NORMAL)  # Enable entry to update value
            f_entry.delete(0, tk.END)
            f_entry.insert(0, "%.2f" % f)
            k_entry.delete(0, tk.END)
            k_entry.insert(0, "%.2f" % c)

    except ValueError:
        f_entry.config(state=tk.NORMAL)  # Enable entry to update value
        k_entry.config(state=tk.NORMAL)  # Enable entry to update value
        f_entry.delete(0, tk.END)
        f_entry.insert(0, "Invalid")
        k_entry.delete(0, tk.END)
        k_entry.insert(0, "Input")
    
    f_entry.config(state=tk.DISABLED)  # Disable entry to prevent further editing
    k_entry.config(state=tk.DISABLED)  # Disable entry to prevent further editing

# Function to clear all input and result fields
def clear_fields(f_entry, k_entry, inputn):
    # Clear all input and result fields
    inputn.set("")
    f_entry.config(state=tk.NORMAL)  # Enable entry to clear value
    k_entry.config(state=tk.NORMAL)  # Enable entry to clear value
    f_entry.delete(0, tk.END)
    k_entry.delete(0, tk.END)
    f_entry.config(state=tk.DISABLED)  # Disable entry after clearing
    k_entry.config(state=tk.DISABLED)  # Disable entry after clearing

# Function to switch from welcome screen to main application
def show_main_screen():
    welcome_frame.pack_forget()  # Hide welcome screen
    main_frame.pack(fill=tk.BOTH, expand=True)  # Show main screen

# Function to handle the "Enter" button click
def enter_pressed():
    show_main_screen()

# Creating Tk window
root = tk.Tk()

# Setting geometry of Tk window
root.geometry('415x250')
root.configure(bg='#f0f0f0')

# Using title() to display a message in the title bar
root.title('Temperature Converter')

# Welcome screen frame
welcome_frame = tk.Frame(root, bg='#f0f0f0')
welcome_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to the Temperature Converter!", font=('Helvetica', 16, 'bold'), bg='#f0f0f0')
welcome_label.pack(pady=30)

enter_button = tk.Button(welcome_frame, text="Enter", font=('Helvetica', 12), command=enter_pressed)
enter_button.pack(pady=10)

# Main application frame
main_frame = tk.Frame(root, bg='#f0f0f0')

# Lay out widgets for the main application
inputNumber = tk.StringVar()
var = tk.StringVar()

# Label and entry field for input
input_label = tk.Label(main_frame, text="Enter Temperature", bg='#f0f0f0')
input_label.grid(row=0, column=0, padx=5, pady=10, sticky='W')
input_entry = tk.Entry(main_frame, textvariable=inputNumber)
input_entry.grid(row=0, column=1, padx=5, pady=10)

# Drop-down setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
var.set(dropDownList[0])  # Set default value
drop_down = tk.OptionMenu(main_frame, var, *dropDownList, command=store_temp)
drop_down.grid(row=0, column=2, padx=5, pady=10)

# Result Labels and Entries
f_label = tk.Label(main_frame, text="Fahrenheit", bg='#f0f0f0')
f_label.grid(row=1, column=0, padx=5, pady=5, sticky='E')
f_result = tk.Entry(main_frame, width=20, font=('Helvetica', 12, 'bold'), fg='red', state=tk.DISABLED)
f_result.grid(row=1, column=1, padx=5, pady=5)

k_label = tk.Label(main_frame, text="Kelvin", bg='#f0f0f0')
k_label.grid(row=2, column=0, padx=5, pady=5, sticky='E')
k_result = tk.Entry(main_frame, width=20, font=('Helvetica', 12, 'bold'), fg='red', state=tk.DISABLED)
k_result.grid(row=2, column=1, padx=5, pady=5)

# Button widget for conversion
convert_action = partial(convert_temp, f_result, k_result, inputNumber)
result_button = tk.Button(main_frame, text="Convert", command=convert_action)
result_button.grid(row=3, column=1, pady=10)

# Button widget for clearing fields
clear_action = partial(clear_fields, f_result, k_result, inputNumber)
clear_button = tk.Button(main_frame, text="Clear", command=clear_action)
clear_button.grid(row=3, column=0, pady=10)

# Start the Tkinter main loop
root.mainloop()
