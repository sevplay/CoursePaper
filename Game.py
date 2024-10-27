import tkinter as tk


def main():
    mainWindow = tk.Tk()
    mainWindow.configure(width=1000,
                         height=500,)
    mainWindow.resizable(False, False)
    mainWindow.title('Main')

    settings = tk.Button(mainWindow,
                         width=1,
                         height=10,
                         command=main,
                         )
    settings.place(x=10, y=10)





    mainWindow.mainloop()

main()