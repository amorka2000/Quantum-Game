import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1000
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_910=tk.Label(root)
        GLabel_910["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_910["font"] = ft
        GLabel_910["fg"] = "#333333"
        GLabel_910["justify"] = "center"
        GLabel_910["text"] = "ساي بلس"
        GLabel_910.place(x=140,y=160,width=78,height=65)

        GLabel_101=tk.Label(root)
        GLabel_101["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_101["font"] = ft
        GLabel_101["fg"] = "#333333"
        GLabel_101["justify"] = "center"
        GLabel_101["text"] = "أوميغا صفر"
        GLabel_101.place(x=220,y=90,width=78,height=65)

        GLabel_592=tk.Label(root)
        GLabel_592["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_592["font"] = ft
        GLabel_592["fg"] = "#333333"
        GLabel_592["justify"] = "center"
        GLabel_592["text"] = "ساي ماينس"
        GLabel_592.place(x=390,y=160,width=78,height=65)

        GLabel_469=tk.Label(root)
        GLabel_469["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_469["font"] = ft
        GLabel_469["fg"] = "#333333"
        GLabel_469["justify"] = "center"
        GLabel_469["text"] = "فاي ماينس"
        GLabel_469.place(x=390,y=230,width=78,height=65)

        GLabel_282=tk.Label(root)
        GLabel_282["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_282["font"] = ft
        GLabel_282["fg"] = "#333333"
        GLabel_282["justify"] = "center"
        GLabel_282["text"] = "أوميغا اثنان"
        GLabel_282.place(x=220,y=300,width=78,height=65)

        GLabel_452=tk.Label(root)
        GLabel_452["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_452["font"] = ft
        GLabel_452["fg"] = "#333333"
        GLabel_452["justify"] = "center"
        GLabel_452["text"] = "أوميغا واحد"
        GLabel_452.place(x=310,y=90,width=78,height=65)

        GLabel_554=tk.Label(root)
        GLabel_554["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_554["font"] = ft
        GLabel_554["fg"] = "#333333"
        GLabel_554["justify"] = "center"
        GLabel_554["text"] = "أوميغا ثلاثة"
        GLabel_554.place(x=310,y=300,width=78,height=65)

        GLabel_372=tk.Label(root)
        GLabel_372["bg"] = "#c71585"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_372["font"] = ft
        GLabel_372["fg"] = "#333333"
        GLabel_372["justify"] = "center"
        GLabel_372["text"] = "صفر"
        GLabel_372.place(x=50,y=230,width=78,height=65)

        GLabel_219=tk.Label(root)
        GLabel_219["bg"] = "#c71585"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_219["font"] = ft
        GLabel_219["fg"] = "#333333"
        GLabel_219["justify"] = "center"
        GLabel_219["text"] = "واحد"
        GLabel_219.place(x=50,y=160,width=78,height=65)

        GLabel_978=tk.Label(root)
        GLabel_978["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_978["font"] = ft
        GLabel_978["fg"] = "#333333"
        GLabel_978["justify"] = "center"
        GLabel_978["text"] = "بلس"
        GLabel_978.place(x=220,y=370,width=78,height=65)

        GLabel_296=tk.Label(root)
        GLabel_296["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_296["font"] = ft
        GLabel_296["fg"] = "#333333"
        GLabel_296["justify"] = "center"
        GLabel_296["text"] = "ماينس"
        GLabel_296.place(x=310,y=370,width=78,height=65)

        GLabel_228=tk.Label(root)
        GLabel_228["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_228["font"] = ft
        GLabel_228["fg"] = "#333333"
        GLabel_228["justify"] = "center"
        GLabel_228["text"] = "معدل الكشف"
        GLabel_228.place(x=10,y=10,width=67,height=63)

        GLabel_968=tk.Label(root)
        GLabel_968["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_968["font"] = ft
        GLabel_968["fg"] = "#333333"
        GLabel_968["justify"] = "center"
        GLabel_968["text"] = ""
        GLabel_968.place(x=160,y=10,width=78,height=65)

        GLabel_722=tk.Label(root)
        GLabel_722["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_722["font"] = ft
        GLabel_722["fg"] = "#333333"
        GLabel_722["justify"] = "center"
        GLabel_722["text"] = ""
        GLabel_722.place(x=240,y=10,width=78,height=65)

        GLabel_962=tk.Label(root)
        GLabel_962["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_962["font"] = ft
        GLabel_962["fg"] = "#333333"
        GLabel_962["justify"] = "center"
        GLabel_962["text"] = ""
        GLabel_962.place(x=320,y=10,width=78,height=65)

        GLabel_363=tk.Label(root)
        GLabel_363["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_363["font"] = ft
        GLabel_363["fg"] = "#333333"
        GLabel_363["justify"] = "center"
        GLabel_363["text"] = ""
        GLabel_363.place(x=400,y=10,width=78,height=65)

        GLabel_132=tk.Label(root)
        GLabel_132["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_132["font"] = ft
        GLabel_132["fg"] = "#333333"
        GLabel_132["justify"] = "center"
        GLabel_132["text"] = ""
        GLabel_132.place(x=480,y=10,width=78,height=65)

        GLabel_770=tk.Label(root)
        GLabel_770["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_770["font"] = ft
        GLabel_770["fg"] = "#333333"
        GLabel_770["justify"] = "center"
        GLabel_770["text"] = ""
        GLabel_770.place(x=560,y=10,width=78,height=65)

        GLabel_129=tk.Label(root)
        GLabel_129["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_129["font"] = ft
        GLabel_129["fg"] = "#333333"
        GLabel_129["justify"] = "center"
        GLabel_129["text"] = ""
        GLabel_129.place(x=650,y=0,width=5,height=545)

        GLabel_445=tk.Label(root)
        GLabel_445["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_445["font"] = ft
        GLabel_445["fg"] = "#333333"
        GLabel_445["justify"] = "center"
        GLabel_445["text"] = ""
        GLabel_445.place(x=650,y=260,width=350,height=5)

        GLabel_419=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_419["font"] = ft
        GLabel_419["fg"] = "#333333"
        GLabel_419["justify"] = "center"
        GLabel_419["text"] = "اللاعب الاول"
        GLabel_419.place(x=790,y=0,width=70,height=25)

        GLabel_347=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_347["font"] = ft
        GLabel_347["fg"] = "#333333"
        GLabel_347["justify"] = "center"
        GLabel_347["text"] = "اللاعب الثاني"
        GLabel_347.place(x=790,y=270,width=70,height=25)

        GLabel_413=tk.Label(root)
        GLabel_413["bg"] = "#d3edc9"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_413["font"] = ft
        GLabel_413["fg"] = "#333333"
        GLabel_413["justify"] = "center"
        GLabel_413["text"] = ""
        GLabel_413.place(x=660,y=70,width=336,height=39)

        GLabel_391=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_391["font"] = ft
        GLabel_391["fg"] = "#333333"
        GLabel_391["justify"] = "center"
        GLabel_391["text"] = "الكروت"
        GLabel_391.place(x=790,y=50,width=70,height=25)

        GLabel_167=tk.Label(root)
        GLabel_167["bg"] = "#d3edc9"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_167["font"] = ft
        GLabel_167["fg"] = "#333333"
        GLabel_167["justify"] = "center"
        GLabel_167["text"] = ""
        GLabel_167.place(x=660,y=340,width=336,height=39)

        GLabel_706=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_706["font"] = ft
        GLabel_706["fg"] = "#333333"
        GLabel_706["justify"] = "center"
        GLabel_706["text"] = "الكروت"
        GLabel_706.place(x=790,y=320,width=70,height=25)

        GLabel_333=tk.Label(root)
        GLabel_333["bg"] = "#e6ceb1"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_333["font"] = ft
        GLabel_333["fg"] = "#333333"
        GLabel_333["justify"] = "center"
        GLabel_333["text"] = ""
        GLabel_333.place(x=0,y=440,width=650,height=58)

        GLabel_82=tk.Label(root)
        GLabel_82["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_82["font"] = ft
        GLabel_82["fg"] = "#333333"
        GLabel_82["justify"] = "center"
        GLabel_82["text"] = "فاي بلس"
        GLabel_82.place(x=140,y=230,width=78,height=65)

        GLineEdit_751=tk.Entry(root)
        GLineEdit_751["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_751["font"] = ft
        GLineEdit_751["fg"] = "#333333"
        GLineEdit_751["justify"] = "center"
        GLineEdit_751["text"] = "Entry"
        GLineEdit_751.place(x=0,y=500,width=249,height=30)

        GButton_732= tk.Button(root, text="Submit", command=lambda: print(GLineEdit_751.get()))
        GButton_732["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_732["font"] = ft
        GButton_732["fg"] = "#000000"
        GButton_732["justify"] = "center"
        GButton_732["text"] = "موافق"
        GButton_732.place(x=250,y=500,width=78,height=30)
    #     GButton_732["command"] = self.GButton_732_command

    # def GButton_732_command(self):

    #     #print GLineEdit_751.get()
    #     print(self.GLineEdit_751["text"])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()