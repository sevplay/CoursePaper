import tkinter as tk

#Game window
def Game():
    mainWindow.destroy()
    GameWindow = tk.Tk()
    GameWindow.configure(width=1000,
                         height=500)
    GameWindow.resizable(False, False)
    GameWindow.title('Game')

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
