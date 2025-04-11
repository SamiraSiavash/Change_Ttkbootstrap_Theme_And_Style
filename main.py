from ttkbootstrap import Window, Button, Radiobutton, Checkbutton, StringVar, BooleanVar, OUTLINE, TOOLBUTTON, TOGGLE, \
    ROUND, SQUARE, Combobox

window = Window(title="Change Theme")

theme_list = window.style.theme_names()
theme_variable = StringVar(value=window.style.theme_use())


def change_theme(event):
    window.style.theme_use(combobox.get())


row = 0
column = 0
combobox = Combobox(window, text=theme_variable)
combobox['values'] = theme_list
combobox.grid(row=row, column=column, columnspan=2, padx=10, pady=10)
window.bind("<<ComboboxSelected>>", change_theme)

column = 0
row += 1
for theme in theme_list:
    radiobutton = Radiobutton(window, text=theme, variable=theme_variable, value=theme, command=lambda: theme_update(),
                              width=10)
    radiobutton.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1
    if column > 7:
        row += 1
        column = 0

column = 0
row += 1
for style in window.style.colors:
    button = Button(window, text=style, bootstyle=style)
    button.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1

column = 0
row += 1
for style in window.style.colors:
    button = Button(window, text=style, bootstyle=style + OUTLINE)
    button.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1

column = 0
row += 1
boolean_variable = BooleanVar(value=True)
for style in window.style.colors:
    checkbutton = Checkbutton(window, text=style, bootstyle=style + TOOLBUTTON, variable=boolean_variable)
    checkbutton.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1

column = 0
row += 1
for style in window.style.colors:
    checkbutton = Checkbutton(window, text=style, bootstyle=style, variable=boolean_variable)
    checkbutton.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1

column = 0
row += 1
for style in window.style.colors:
    checkbutton = Checkbutton(window, text=style, bootstyle=style + ROUND + TOGGLE, variable=boolean_variable)
    checkbutton.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1

column = 0
row += 1
for style in window.style.colors:
    checkbutton = Checkbutton(window, text=style, bootstyle=style + SQUARE + TOGGLE, variable=boolean_variable)
    checkbutton.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    column += 1


def theme_update():
    window.style.theme_use(theme_variable.get())


window.mainloop()
