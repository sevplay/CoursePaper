import tkinter as tk
from random import randint


#Main window
def main():
    def GCC(v):
        a = buttons[buttons.index(f'<tkinter.Button object .butt{v}>')]
        if a['bg'] == 'red': 
            a['bg'] = 'blue'
        else:
            a['bg'] = 'red'

    GameWindow = tk.Tk()
    GameWindow.geometry('400x400')
    GameWindow.resizable(False, False)
    GameWindow.title('Game')

    buttons = []
    buttons_pos = []
    col = ['red', 'blue']

    for i in range(4):
        for j in range(4):
            GC = tk.Button(GameWindow,
                           bg=col[randint(0, 1)],
                           name=f'butt{i}{j}',
                           width=8,
                           height=4,
                           command=lambda : GCC(f'{i}{j}'))
            GC.grid(row=i, column=j,
                    padx=5, pady=5)
            buttons_pos.append(GC.winfo_name()[4:6])
            buttons.append(GC)
            

    GameWindow.mainloop()

main()
