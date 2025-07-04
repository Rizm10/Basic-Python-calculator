import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#000000")

# Entry display
entry = tk.Entry(
    root, font=("Helvetica", 26), bd=0,
    bg="#1C1C1E", fg="white",
    insertbackground="white", justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Responsive grid
for i in range(6): root.grid_rowconfigure(i, weight=1)
for i in range(4): root.grid_columnconfigure(i, weight=1)

# Logic functions
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def insert_bracket():
    current = entry.get()
    open_count = current.count("(")
    close_count = current.count(")")
    if not current or current[-1] in "+-*/(":
        entry.insert(tk.END, "(")
    elif open_count > close_count:
        entry.insert(tk.END, ")")
    else:
        entry.insert(tk.END, "(")

def toggle_negative():
    current = entry.get()
    if current.startswith("-"):
        entry.delete(0, tk.END)
        entry.insert(0, current[1:])
    else:
        entry.insert(0, "-")

def percent():
    try:
        current = entry.get()
        if current:
            value = float(current) / 100
            entry.delete(0, tk.END)
            entry.insert(0, str(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button styling
button_colors = {
    "num": {"bg": "#1C1C1E", "fg": "black"},
    "op": {"bg": "#1C1C1E", "fg": "black"},
    "util": {"bg": "#1C1C1E", "fg": "black"},
}

# Buttons: (label, command, type, row, col)
buttons = [
    ("AC", clear, "util", 1, 0), ("+/-", toggle_negative, "util", 1, 1), ("%", percent, "util", 1, 2), ("/", lambda: click("/"), "op", 1, 3),
    ("7", lambda: click("7"), "num", 2, 0), ("8", lambda: click("8"), "num", 2, 1), ("9", lambda: click("9"), "num", 2, 2), ("*", lambda: click("*"), "op", 2, 3),
    ("4", lambda: click("4"), "num", 3, 0), ("5", lambda: click("5"), "num", 3, 1), ("6", lambda: click("6"), "num", 3, 2), ("-", lambda: click("-"), "op", 3, 3),
    ("1", lambda: click("1"), "num", 4, 0), ("2", lambda: click("2"), "num", 4, 1), ("3", lambda: click("3"), "num", 4, 2), ("+", lambda: click("+"), "op", 4, 3),
    ("0", lambda: click("0"), "num", 5, 0), (".", lambda: click("."), "util", 5, 1), ("()", insert_bracket, "util", 5, 2), ("=", evaluate, "op", 5, 3)
]

# Create buttons
for label, cmd, btype, row, col in buttons:
    colors = button_colors[btype]
    tk.Button(
        root, text=label, command=cmd,
        bg=colors["bg"], fg=colors["fg"],
        font=("Helvetica", 20), bd=0, padx=20, pady=20,
        activebackground=colors["bg"], activeforeground=colors["fg"],
        highlightthickness=0
    ).grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

# Run app
root.mainloop()

