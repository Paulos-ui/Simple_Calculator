import tkinter as tk

def on_click(button_text):
    """Handles button clicks and updates the entry field."""
    if button_text == "=":
        try:
            result = eval(entry_var.get())  # Evaluate the expression
            entry_var.set(result)
        except:
            entry_var.set("Error")  # Display error for invalid input
    elif button_text == "C":
        entry_var.set("")  # Clear the input field
    else:
        entry_var.set(entry_var.get() + button_text)  # Append button text

# Create the main window
root = tk.Tk()
root.title("Mini Calculator")
root.geometry("350x500")  # Set window size

# Entry field to display calculations
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify='right', bd=10, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons and place them in the window
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda t=text: on_click(t), width=6, height=2)
        btn.grid(row=r+1, column=c, padx=5, pady=5)

# Run the main event loop
root.mainloop()

