import tkinter as tk
from random import randint

#Game window
def Game():
    def GCC():
        buttons[1]['bg'] = 'Blue'


    mainWindow.destroy()
    GameWindow = tk.Tk()
    GameWindow.configure(width=400,
                         height=400)
    GameWindow.resizable(False, False)
    GameWindow.title('Game')

    buttons = []
    for i in range(4):
        row_buttons = []
        for j in range(4):
            GC = tk.Button(GameWindow,
                           name=f'Button{i}{j}',
                           bg='red',
                           width=8,
                           height=4,
                           command=GCC())
            GC.place(x=10 + 100*i, y=10 + 100*j)
            row_buttons.append(GC)
        buttons.append(row_buttons)


    print(buttons)
    GameWindow.mainloop()
    main()



#Settings window
def Settings():
    mainWindow.destroy()

    settingsWindow = tk.Tk()
    settingsWindow.configure(width=1000,
                             height=500)
    settingsWindow.resizable(False, False)
    settingsWindow.title('Settings')

    settingsWindow.mainloop()
    main()



#Main window
def main():
    global mainWindow
    
    mainWindow = tk.Tk()
    mainWindow.configure(width=1000,
                         height=500)
    mainWindow.resizable(False, False)
    mainWindow.title('Main')

    settingsButton = tk.Button(mainWindow,
                         width=1,
                         height=10,
                         command=Settings,
                         )
    settingsButton.place(x=10, y=10)
    GameButton = tk.Button(mainWindow,
                         width=10,
                         height=1,
                         command=Game,
                         )
    GameButton.place(x=100, y=10)





    mainWindow.mainloop()

main()
