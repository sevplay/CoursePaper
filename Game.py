import tkinter as tk

def Settings():
    mainWindow.destroy()

    settingsWindow = tk.Tk()
    settingsWindow.configure(width=1000,
                         height=500)
    settingsWindow.resizable(False, False)
    settingsWindow.title('Settings')

    settingsWindow.mainloop()
    main()


def main():
    global mainWindow
    mainWindow = tk.Tk()
    mainWindow.configure(width=1000,
                         height=500)
    mainWindow.resizable(False, False)
    mainWindow.title('Main')

    settings = tk.Button(mainWindow,
                         width=1,
                         height=10,
                         command=Settings,
                         )
    settings.place(x=10, y=10)





    mainWindow.mainloop()

main()