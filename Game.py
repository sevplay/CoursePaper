import tkinter as tk
from random import randint
from time import sleep


#Main window
def main():
    def wincheck():
        def WinWindow():
                global WinWindow

                WinWindow = tk.Tk()
                WinWindow.geometry('300x150')
                WinWindow.resizable(False, False)
                WinWindow.title('WIn')
            
                Label = tk.Label(WinWindow,
                                 text="Задача решена!",
                                 font=('Arial', '16')
                                 )
                Label.place(x=70, y=10)
            
                winrestartB = tk.Button(WinWindow,
                                  bg='White',
                                  width=10,
                                  height=1,
                                  text='Перезапуск',
                                  font=('Arial', '14'),
                                  command=RestartC)
                winrestartB.place(x=87, y=50)

                exitB = tk.Button(WinWindow,
                                  bg='White',
                                  width=10,
                                  height=1,
                                  text='Выход',
                                  font=('Arial', '14'),
                                  command=lambda: exit(0))
                exitB.place(x=87, y=95)


                WinWindow.grab_set()
                

        rcount = 0
        bcount = 0
        for i in range(4):
            for j in range(4):
                v = str(i) + str(j)
                a = buttons[buttons_pos.index(v)]

                if a['bg'] == 'red':
                    rcount += 1
                else:
                    bcount += 1

                if rcount == 16:
                    WinWindow()
                elif bcount == 16:
                    WinWindow()
   
    
    def GCC(v):
        a = buttons[buttons_pos.index(v)]
        if a['bg'] == 'red': 
            a['bg'] = 'blue'
        else:
            a['bg'] = 'red'
        try:
            a = buttons[buttons_pos.index(v[0]+str(int(v[1])-1))]
            if a['bg'] == 'red': 
                a['bg'] = 'blue'
            else:
                a['bg'] = 'red'
        except:
            pass
        try:
            a = buttons[buttons_pos.index(v[0]+str(int(v[1])+1))]
            if a['bg'] == 'red': 
                a['bg'] = 'blue'
            else:
                a['bg'] = 'red'
        except:
            pass
        try:
            a = buttons[buttons_pos.index(str(int(v[0])-1)+v[1])]
            if a['bg'] == 'red': 
                a['bg'] = 'blue'
            else:
                a['bg'] = 'red'
        except:
            pass
        try:
            a = buttons[buttons_pos.index(str(int(v[0])+1)+v[1])]
            if a['bg'] == 'red': 
                a['bg'] = 'blue'
            else:
                a['bg'] = 'red'
        except:
            pass

        wincheck()
    
    
    def RestartC():
        global WinWindow
        
        try:
            GameWindow.destroy()
        except:
            pass
        
        try:
            WinWindow.destroy()
        except:
            pass
        

        main()


    GameWindow = tk.Tk()
    GameWindow.geometry('310x370')
    GameWindow.resizable(False, False)
    GameWindow.title('Game')

    buttons = []
    buttons_pos = []
    col = ['red', 'blue']
    col_list = []

    while True:
        for i in range(16):
            col_list.append(col[randint(0, 1)])
        
        if col_list.count('red') % 2 == 0:
            break
        elif col_list.count('red') % 2 == 0:
            break
        else:
            col_list = []


    GC00 = tk.Button(GameWindow,
                   bg=col_list[0],
                   width=8,
                   height=4,
                   command=lambda : GCC('00'))
    GC00.grid(row=0, column=0,
            padx=5, pady=5)
    buttons.append(GC00)
    buttons_pos.append('00')

    GC01 = tk.Button(GameWindow,
                   bg=col_list[1],
                   width=8,
                   height=4,
                   command=lambda : GCC('01'))
    GC01.grid(row=0, column=1,
            padx=5, pady=5)
    buttons.append(GC01)
    buttons_pos.append('01')
    

    GC02 = tk.Button(GameWindow,
                   bg=col_list[2],
                   width=8,
                   height=4,
                   command=lambda : GCC('02'))
    GC02.grid(row=0, column=2,
            padx=5, pady=5)
    buttons.append(GC02)
    buttons_pos.append('02')
    

    GC03 = tk.Button(GameWindow,
                   bg=col_list[3],
                   width=8,
                   height=4,
                   command=lambda : GCC('03'))
    GC03.grid(row=0, column=3,
            padx=5, pady=5)
    buttons.append(GC03)
    buttons_pos.append('03')
    

    GC10 = tk.Button(GameWindow,
                   bg=col_list[4],
                   width=8,
                   height=4,
                   command=lambda : GCC('10'))
    GC10.grid(row=1, column=0,
            padx=5, pady=5)
    buttons.append(GC10)
    buttons_pos.append('10')
    

    GC11 = tk.Button(GameWindow,
                   bg=col_list[5],
                   width=8,
                   height=4,
                   command=lambda : GCC('11'))
    GC11.grid(row=1, column=1,
            padx=5, pady=5)
    buttons.append(GC11)
    buttons_pos.append('11')
    

    GC12 = tk.Button(GameWindow,
                   bg=col_list[6],
                   width=8,
                   height=4,
                   command=lambda : GCC('12'))
    GC12.grid(row=1, column=2,
            padx=5, pady=5)
    buttons.append(GC12)
    buttons_pos.append('12')
    

    GC13 = tk.Button(GameWindow,
                   bg=col_list[7],
                   width=8,
                   height=4,
                   command=lambda : GCC('13'))
    GC13.grid(row=1, column=3,
            padx=5, pady=5)
    buttons.append(GC13)
    buttons_pos.append('13')
    

    GC20 = tk.Button(GameWindow,
                   bg=col_list[8],
                   width=8,
                   height=4,
                   command=lambda : GCC('20'))
    GC20.grid(row=2, column=0,
            padx=5, pady=5)
    buttons.append(GC20)
    buttons_pos.append('20')
    

    GC21 = tk.Button(GameWindow,
                   bg=col_list[9],
                   width=8,
                   height=4,
                   command=lambda : GCC('21'))
    GC21.grid(row=2, column=1,
            padx=5, pady=5)
    buttons.append(GC21)
    buttons_pos.append('21')
    

    GC22 = tk.Button(GameWindow,
                   bg=col_list[10],
                   width=8,
                   height=4,
                   command=lambda : GCC('22'))
    GC22.grid(row=2, column=2,
            padx=5, pady=5)
    buttons.append(GC22)
    buttons_pos.append('22')
    

    GC23 = tk.Button(GameWindow,
                   bg=col_list[11],
                   width=8,
                   height=4,
                   command=lambda : GCC('23'))
    GC23.grid(row=2, column=3,
            padx=5, pady=5)
    buttons.append(GC23)
    buttons_pos.append('23')
    

    GC30 = tk.Button(GameWindow,
                   bg=col_list[12],
                   width=8,
                   height=4,
                   command=lambda : GCC('30'))
    GC30.grid(row=3, column=0,
            padx=5, pady=5)
    buttons.append(GC30)
    buttons_pos.append('30')
    

    GC31 = tk.Button(GameWindow,
                   bg=col_list[13],
                   width=8,
                   height=4,
                   command=lambda : GCC('31'))
    GC31.grid(row=3, column=1,
            padx=5, pady=5)
    buttons.append(GC31)
    buttons_pos.append('31')
    

    GC32 = tk.Button(GameWindow,
                   bg=col_list[14],
                   width=8,
                   height=4,
                   command=lambda : GCC('32'))
    GC32.grid(row=3, column=2,
            padx=5, pady=5)
    buttons.append(GC32)
    buttons_pos.append('32')
    

    GC33 = tk.Button(GameWindow,
                   bg=col_list[15],
                   width=8,
                   height=4,
                   command=lambda : GCC('33'))
    GC33.grid(row=3, column=3,
            padx=5, pady=5)
    buttons.append(GC33)
    buttons_pos.append('33')

    restartB = tk.Button(GameWindow,
                         bg='White',
                         width=10,
                         height=1,
                         text='Перезапуск',
                         font=('Arial', '14'),
                         command=RestartC)
    restartB.place(x=90, y=325)
    

    GameWindow.mainloop()


main()
