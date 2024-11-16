import tkinter as tk
from random import randint
from time import sleep


#Main window
def main():
    def wincheck(e):
        rcount = 0
        bcount = 0
        for i in range(4):
            for j in range(4):
                v = str(i) + str(j)
                a = buttons[buttons_pos.index(v)]
                print(a['bg'])

                if a['bg'] == 'red':
                    rcount += 1
                else:
                    bcount += 1

                if rcount == 16:
                    WinWindow = tk.Tk()
                    WinWindow.geometry('100x100')
                    WinWindow.resizable(False, False)
                    WinWindow.title('WIn')

                    Label = tk.Label(WinWindow,
                                     text="Задача решена!",
                                     font=('arrial', '14', 'Italic')
                                     )
                    Label.pack()

                    WinWindow.grab_set()
                    return True
                
                elif bcount == 16:
                    WinWindow = tk.Tk()
                    WinWindow.geometry('100x100')
                    WinWindow.resizable(False, False)
                    WinWindow.title('WIn')

                    Label = tk.Label(WinWindow,
                                     text="Задача решена!",
                                     font=('arrial', '14', 'Italic')
                                     )
                    Label.pack()

                    WinWindow.grab_set()
   
    
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
    
    
    GameWindow = tk.Tk()
    GameWindow.geometry('310x325')
    GameWindow.resizable(False, False)
    GameWindow.title('Game')

    buttons = []
    buttons_pos = []
    col = ['red', 'blue']


    GC00 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('00'))
    GC00.grid(row=0, column=0,
            padx=5, pady=5)
    GC00.bind("<Button>", wincheck)
    buttons.append(GC00)
    buttons_pos.append('00')

    GC01 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('01'))
    GC01.grid(row=0, column=1,
            padx=5, pady=5)
    GC01.bind("<Button>", wincheck)
    buttons.append(GC01)
    buttons_pos.append('01')
    

    GC02 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('02'))
    GC02.grid(row=0, column=2,
            padx=5, pady=5)
    GC02.bind("<Button>", wincheck)
    buttons.append(GC02)
    buttons_pos.append('02')
    

    GC03 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('03'))
    GC03.grid(row=0, column=3,
            padx=5, pady=5)
    GC03.bind("<Button>", wincheck)
    buttons.append(GC03)
    buttons_pos.append('03')
    

    GC10 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('10'))
    GC10.grid(row=1, column=0,
            padx=5, pady=5)
    GC10.bind("<Button>", wincheck)
    buttons.append(GC10)
    buttons_pos.append('10')
    

    GC11 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('11'))
    GC11.grid(row=1, column=1,
            padx=5, pady=5)
    GC11.bind("<Button>", wincheck)
    buttons.append(GC11)
    buttons_pos.append('11')
    

    GC12 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('12'))
    GC12.grid(row=1, column=2,
            padx=5, pady=5)
    GC12.bind("<Button>", wincheck)
    buttons.append(GC12)
    buttons_pos.append('12')
    

    GC13 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('13'))
    GC13.grid(row=1, column=3,
            padx=5, pady=5)
    GC13.bind("<Button>", wincheck)
    buttons.append(GC13)
    buttons_pos.append('13')
    

    GC20 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('20'))
    GC20.grid(row=2, column=0,
            padx=5, pady=5)
    GC20.bind("<Button>", wincheck)
    buttons.append(GC20)
    buttons_pos.append('20')
    

    GC21 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('21'))
    GC21.grid(row=2, column=1,
            padx=5, pady=5)
    GC21.bind("<Button>", wincheck)
    buttons.append(GC21)
    buttons_pos.append('21')
    

    GC22 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('22'))
    GC22.grid(row=2, column=2,
            padx=5, pady=5)
    GC22.bind("<Button>", wincheck)
    buttons.append(GC22)
    buttons_pos.append('22')
    

    GC23 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('23'))
    GC23.grid(row=2, column=3,
            padx=5, pady=5)
    GC23.bind("<Button>", wincheck)
    buttons.append(GC23)
    buttons_pos.append('23')
    

    GC30 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('30'))
    GC30.grid(row=3, column=0,
            padx=5, pady=5)
    GC30.bind("<Button>", wincheck)
    buttons.append(GC30)
    buttons_pos.append('30')
    

    GC31 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('31'))
    GC31.grid(row=3, column=1,
            padx=5, pady=5)
    GC31.bind("<Button>", wincheck)
    buttons.append(GC31)
    buttons_pos.append('31')
    

    GC32 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('32'))
    GC32.grid(row=3, column=2,
            padx=5, pady=5)
    GC32.bind("<Button>", wincheck)
    buttons.append(GC32)
    buttons_pos.append('32')
    

    GC33 = tk.Button(GameWindow,
                   bg=col[randint(0, 1)],
                   width=8,
                   height=4,
                   command=lambda : GCC('33'))
    GC33.grid(row=3, column=3,
            padx=5, pady=5)
    GC33.bind("<Button>", wincheck)
    buttons.append(GC33)
    buttons_pos.append('33')
    
            

    GameWindow.mainloop()

main()