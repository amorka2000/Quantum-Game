import asyncio
import os
import random
import tkinter as tk
import tkinter.font as tkFont

class EntanglionGame:
    #global GLabel_333
    global but_var
    def __init__(self, root):
        #GUI
        root.title("undefined")
        #setting window size
        width=1000
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLabel_910=tk.Label(root)
        self.GLabel_910["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_910["font"] = ft
        self.GLabel_910["fg"] = "#333333"
        self.GLabel_910["justify"] = "center"
        self.GLabel_910["text"] = "ساي بلس"
        self.GLabel_910.place(x=140,y=160,width=78,height=65)

        self.GLabel_101=tk.Label(root)
        self.GLabel_101["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_101["font"] = ft
        self.GLabel_101["fg"] = "#333333"
        self.GLabel_101["justify"] = "center"
        self.GLabel_101["text"] = "أوميغا صفر"
        self.GLabel_101.place(x=220,y=90,width=78,height=65)

        self.GLabel_592=tk.Label(root)
        self.GLabel_592["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_592["font"] = ft
        self.GLabel_592["fg"] = "#333333"
        self.GLabel_592["justify"] = "center"
        self.GLabel_592["text"] = "ساي ماينس"
        self.GLabel_592.place(x=390,y=160,width=78,height=65)

        self.GLabel_469=tk.Label(root)
        self.GLabel_469["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_469["font"] = ft
        self.GLabel_469["fg"] = "#333333"
        self.GLabel_469["justify"] = "center"
        self.GLabel_469["text"] = "فاي ماينس"
        self.GLabel_469.place(x=390,y=230,width=78,height=65)

        self.GLabel_282=tk.Label(root)
        self.GLabel_282["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_282["font"] = ft
        self.GLabel_282["fg"] = "#333333"
        self.GLabel_282["justify"] = "center"
        self.GLabel_282["text"] = "أوميغا اثنان"
        self.GLabel_282.place(x=220,y=300,width=78,height=65)

        self.GLabel_452=tk.Label(root)
        self.GLabel_452["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_452["font"] = ft
        self.GLabel_452["fg"] = "#333333"
        self.GLabel_452["justify"] = "center"
        self.GLabel_452["text"] = "أوميغا واحد"
        self.GLabel_452.place(x=310,y=90,width=78,height=65)

        self.GLabel_554=tk.Label(root)
        self.GLabel_554["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_554["font"] = ft
        self.GLabel_554["fg"] = "#333333"
        self.GLabel_554["justify"] = "center"
        self.GLabel_554["text"] = "أوميغا ثلاثة"
        self.GLabel_554.place(x=310,y=300,width=78,height=65)

        self.GLabel_372=tk.Label(root)
        self.GLabel_372["bg"] = "#c71585"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_372["font"] = ft
        self.GLabel_372["fg"] = "#333333"
        self.GLabel_372["justify"] = "center"
        self.GLabel_372["text"] = "صفر"
        self.GLabel_372.place(x=50,y=230,width=78,height=65)

        self.GLabel_219=tk.Label(root)
        self.GLabel_219["bg"] = "#c71585"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_219["font"] = ft
        self.GLabel_219["fg"] = "#333333"
        self.GLabel_219["justify"] = "center"
        self.GLabel_219["text"] = "واحد"
        self.GLabel_219.place(x=50,y=160,width=78,height=65)

        self.GLabel_978=tk.Label(root)
        self.GLabel_978["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_978["font"] = ft
        self.GLabel_978["fg"] = "#333333"
        self.GLabel_978["justify"] = "center"
        self.GLabel_978["text"] = "بلس"
        self.GLabel_978.place(x=220,y=370,width=78,height=65)

        self.GLabel_296=tk.Label(root)
        self.GLabel_296["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_296["font"] = ft
        self.GLabel_296["fg"] = "#333333"
        self.GLabel_296["justify"] = "center"
        self.GLabel_296["text"] = "ماينس"
        self.GLabel_296.place(x=310,y=370,width=78,height=65)

        self.GLabel_228=tk.Label(root)
        self.GLabel_228["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_228["font"] = ft
        self.GLabel_228["fg"] = "#333333"
        self.GLabel_228["justify"] = "center"
        self.GLabel_228["text"] = "معدل الكشف"
        self.GLabel_228.place(x=10,y=10,width=67,height=63)

        self.GLabel_129=tk.Label(root)
        self.GLabel_129["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_129["font"] = ft
        self.GLabel_129["fg"] = "#333333"
        self.GLabel_129["justify"] = "center"
        self.GLabel_129["text"] = ""
        self.GLabel_129.place(x=650,y=0,width=5,height=545)

        self.GLabel_445=tk.Label(root)
        self.GLabel_445["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_445["font"] = ft
        self.GLabel_445["fg"] = "#333333"
        self.GLabel_445["justify"] = "center"
        self.GLabel_445["text"] = ""
        self.GLabel_445.place(x=650,y=260,width=350,height=5)

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

        self.GLabel_413=tk.Label(root)
        self.GLabel_413["bg"] = "#d3edc9"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_413["font"] = ft
        self.GLabel_413["fg"] = "#333333"
        self.GLabel_413["justify"] = "center"
        self.GLabel_413["text"] = ""
        self.GLabel_413.place(x=660,y=70,width=336,height=39)

        self.GLabel_391=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_391["font"] = ft
        self.GLabel_391["fg"] = "#333333"
        self.GLabel_391["justify"] = "center"
        self.GLabel_391["text"] = "الكروت"
        self.GLabel_391.place(x=790,y=50,width=70,height=25)

        self.GLabel_167=tk.Label(root)
        self.GLabel_167["bg"] = "#d3edc9"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_167["font"] = ft
        self.GLabel_167["fg"] = "#333333"
        self.GLabel_167["justify"] = "center"
        self.GLabel_167["text"] = ""
        self.GLabel_167.place(x=660,y=340,width=336,height=39)

        self.GLabel_706=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_706["font"] = ft
        self.GLabel_706["fg"] = "#333333"
        self.GLabel_706["justify"] = "center"
        self.GLabel_706["text"] = "الكروت"
        self.GLabel_706.place(x=790,y=320,width=70,height=25)

        self.GLabel_333=tk.Label(root)
        self.GLabel_333["bg"] = "#e6ceb1"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_333["font"] = ft
        self.GLabel_333["fg"] = "#333333"
        self.GLabel_333["justify"] = "center"
        self.GLabel_333["text"] = ""
        self.GLabel_333.place(x=0,y=440,width=650,height=58)

        self.GLabel_82=tk.Label(root)
        self.GLabel_82["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_82["font"] = ft
        self.GLabel_82["fg"] = "#333333"
        self.GLabel_82["justify"] = "center"
        self.GLabel_82["text"] = "فاي بلس"
        self.GLabel_82.place(x=140,y=230,width=78,height=65)

        self.GLineEdit_751=tk.Entry(root)
        self.GLineEdit_751["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_751["font"] = ft
        self.GLineEdit_751["fg"] = "#333333"
        self.GLineEdit_751["justify"] = "center"
        self.GLineEdit_751["text"] = "Entry"
        self.GLineEdit_751.place(x=0,y=500,width=249,height=30)

        self.GButton_732= tk.Button(root, text="Submit", command=lambda: but_var.set(1))
        self.GButton_732["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_732["font"] = ft
        self.GButton_732["fg"] = "#000000"
        self.GButton_732["justify"] = "center"
        self.GButton_732["text"] = "موافق"
        self.GButton_732.place(x=250,y=500,width=78,height=30)
        #self.GButton_732["command"] = self.GButton_732_command

        self.GLabel_104=tk.Label(root)
        self.GLabel_104["bg"] = "#bf9090"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_104["font"] = ft
        self.GLabel_104["fg"] = "#333333"
        self.GLabel_104["justify"] = "center"
        self.GLabel_104["text"] = ""
        self.GLabel_104.config(wraplength=336)
        self.GLabel_104.place(x=660,y=130,width=336,height=53)

        self.GLabel_131=tk.Label(root)
        self.GLabel_131["bg"] = "#bf9090"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_131["font"] = ft
        self.GLabel_131["fg"] = "#333333"
        self.GLabel_131["justify"] = "center"
        self.GLabel_131["text"] = ""
        self.GLabel_131.config(wraplength=336)
        self.GLabel_131.place(x=660,y=400,width=336,height=53)

        GLabel_92=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_92["font"] = ft
        GLabel_92["fg"] = "#333333"
        GLabel_92["justify"] = "center"
        GLabel_92["text"] = "المكونات الكمية"
        GLabel_92.place(x=790,y=110,width=70,height=25)

        GLabel_535=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_535["font"] = ft
        GLabel_535["fg"] = "#333333"
        GLabel_535["justify"] = "center"
        GLabel_535["text"] = "المكونات الكمية"
        GLabel_535.place(x=790,y=380,width=70,height=25)

        self.GLabel_441=tk.Label(root)
        self.GLabel_441["bg"] = "#bcbc7c"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_441["font"] = ft
        self.GLabel_441["fg"] = "#333333"
        self.GLabel_441["justify"] = "center"
        self.GLabel_441["text"] = ""
        self.GLabel_441.config(wraplength=336)
        self.GLabel_441.place(x=660,y=200,width=336,height=53)

        self.GLabel_557=tk.Label(root)
        self.GLabel_557["bg"] = "#bcbc7c"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_557["font"] = ft
        self.GLabel_557["fg"] = "#333333"
        self.GLabel_557["justify"] = "center"
        self.GLabel_557["text"] = ""
        self.GLabel_557.config(wraplength=336)
        self.GLabel_557.place(x=660,y=480,width=336,height=53)

        GLabel_740=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_740["font"] = ft
        GLabel_740["fg"] = "#333333"
        GLabel_740["justify"] = "center"
        GLabel_740["text"] = "الاحداث الكمية"
        GLabel_740.place(x=790,y=180,width=70,height=25)

        GLabel_534=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_534["font"] = ft
        GLabel_534["fg"] = "#333333"
        GLabel_534["justify"] = "center"
        GLabel_534["text"] = "الاحداث الكمية"
        GLabel_534.place(x=790,y=460,width=70,height=25)

        self.quantum_components = ["Quantum Error Correction", "Physical Qubits", "Quantum Gates", "Magnetic Shielding",
                                   "Qubit Interconnect", "Quantum Programming", "Dilution Refrigerator", "Control Infrastructure"]
        self.detection_rate = 1
        self.ship_locations = {}
        self.engine_deck = ["X", "H", "SWAP", "CNOT", "PROBE"]
        self.quantum_event_deck = ["Bit Flip Error", "Wave Function Collapse", "Schrödinger","Quantum Shuffle"]
        self.engine_control = {"Player1": [], "Player2": []}
        self.engine_discard = []
        self.current_player = ""
        self.engine_card_pile = []
        self.initialize_ship_locations()
        self.create_engine_card_pile()
        self.distribute_engine_cards()

    # def GButton_732_command(self):
    #     print("command")
        
    def initialize_ship_locations(self):
        #flag = await asyncio.wait_for(GButton_732_command(), 2)
        self.GLabel_333["text"] = "Player 1: Press Enter to roll the Centarious dice..."
        self.GButton_732.wait_variable(but_var)
        self.ship_locations["Player1"] = {"Galaxy": "Centarious", "Planet": "ZERO" if self.roll_dice1() == 0 else "ONE"}
        self.GLabel_333["text"] = "Player 2: Press Enter to roll the Centarious dice..."
        self.GButton_732.wait_variable(but_var)
        self.ship_locations["Player2"] = {"Galaxy": "Centarious", "Planet": "ZERO" if self.roll_dice2() == 0 else "ONE"}
        
    def roll_dice1(self):
        #input("Player 1: Press Enter to roll the Centarious dice...")
        #os.wait(tk.Button(self.root, text="Submit", command=lambda: print(self.GLineEdit_751.get())))
        dice_roll = random.randint(0, 1)
        self.GLabel_333["text"] = "Dice roll:" + str(dice_roll)
        self.GButton_732.wait_variable(but_var)
        return dice_roll
    
    def roll_dice2(self):
        #input("Player 2: Press Enter to roll the Centarious dice...")
        dice_roll = random.randint(0, 1)
        self.GLabel_333["text"] = "Dice roll:" + str(dice_roll)
        self.GButton_732.wait_variable(but_var)
        return dice_roll

    def create_engine_card_pile(self):
        engine_cards = ["H"] * 8 + ["CNOT"] * 7 + ["X"] * 5 + ["SWAP"] * 3 + ["PROBE"]
        self.engine_card_pile = engine_cards * 2  # 24 engine cards in total
        random.shuffle(self.engine_card_pile)

    def distribute_engine_cards(self):
        for player in self.engine_control:
            self.engine_control[player] = self.draw_engine_cards(player, 3)

    def draw_engine_cards(self, player, num_cards):
        cards = []
        for _ in range(num_cards):
            if self.engine_card_pile:
                card = self.engine_card_pile.pop()
                cards.append(card)
            else:
                #print("No more engine cards left in the pile.")
                self.GLabel_333["text"] = "No more engine cards left in the pile."
                self.GButton_732.wait_variable(but_var)
                break
        return cards


    def setup_game(self):
        temp_str = "=== Entanglion Game ===\n"
        self.current_player = random.choice(["Player1", "Player2"])
        temp_str+= "Starting Player:" + self.current_player
        self.GLabel_333["text"] = temp_str


    def draw_event_card(self):
        if len(self.quantum_event_deck) > 0:
            card = random.choice(self.quantum_event_deck)
            self.quantum_event_deck.remove(card)
            self.perform_event_card(card)
            return card
        else:
            #print("No event cards left.")
            self.GLabel_333["text"] = "No event cards left."
            self.GButton_732.wait_variable(but_var)
            return None
        
    def perform_event_card(self, card):
        #print(f"Event card drawn: {card}")
        self.GLabel_333["text"] = "Event card drawn:" + card
        self.GButton_732.wait_variable(but_var)
        if card == "Bit Flip Error":
            if self.detection_rate > 4:
                self.detection_rate = 4
            #print("Detection rate reset to 4.")
            self.GLabel_333["text"] = "Detection rate reset to 4."
            self.GButton_732.wait_variable(but_var)
        elif card == "Wave Function Collapse":
            if self.detection_rate > 2:
                self.detection_rate -= 2
                #print("Detection rate decreased by 2.")
                self.GLabel_333["text"] = "Detection rate decreased by 2."
                self.GButton_732.wait_variable(but_var)
            else:
                self.detection_rate = 1
        elif card == "Schrödinger":
            self.detection_rate += 1
            #print("Detection rate increased by 1.")
            self.GLabel_333["text"] = "Detection rate increased by 1."
            self.GButton_732.wait_variable(but_var)
        elif card == "Quantum Shuffle":
            random.shuffle(self.quantum_event_deck)
            #print("Event card shuffled.")
            self.GLabel_333["text"] = "Event card shuffled."
            self.GButton_732.wait_variable(but_var)
            new_card = self.draw_event_card()
            if new_card:
                #print(f"Additional event card drawn: {new_card}")
                self.GLabel_333["text"] = "Additional event card drawn:" + new_card
                self.GButton_732.wait_variable(but_var)
        else:
            #print(f"Invalid event card: {card}")
            self.GLabel_333["text"] = "Invalid event card:" + card
            self.GButton_732.wait_variable(but_var)
        #print()

    def perform_retrieval_mission(self, player):
        #print(f"Player {player}, performing retrieval mission...")
        self.GLabel_333["text"] = "Player " + player + ", performing retrieval mission..."
        self.GButton_732.wait_variable(but_var)
        outcome = self.roll_dice()  # Simulate rolling the Entanglion die
        #print("Outcome of the retrieval mission:", outcome)
        self.GLabel_333["text"] = "Outcome of the retrieval mission:" + str(outcome)
        self.GButton_732.wait_variable(but_var)
        if outcome > self.detection_rate:
            component = random.choice(self.quantum_components)
            self.quantum_components.remove(component)
            #print("Component retrieved:", component)
            #print("Placing component on spaceship board...")
            self.GLabel_333["text"] = "Component retrieved:" + component + "\nPlacing component on spaceship board..."
            self.GButton_732.wait_variable(but_var)
        else:
            #print("Away team was detected by ground defenses!")
            self.GLabel_333["text"] = "Away team was detected by ground defenses!"
            self.GButton_732.wait_variable(but_var)
            self.detection_rate += 1
            #print("Detection rate increased to:", self.detection_rate)
            self.GLabel_333["text"] = "Detection rate increased to:" + str(self.detection_rate)
            self.GButton_732.wait_variable(but_var)
            
    def roll_dice(self):
        #input("Press Enter to roll the Entanglion dice...")
        self.GLabel_333["text"] = "Press Enter to roll the Entanglion dice..."
        self.GButton_732.wait_variable(but_var)
        dice_roll = random.randint(1, 8)
        #print("Dice roll:", dice_roll)
        self.GLabel_333["text"] = "Dice roll:" + str(dice_roll)
        self.GButton_732.wait_variable(but_var)
        return dice_roll

    def play_game(self):
        self.setup_game()
        while True:
            #print()
            #print("Current Player:", self.current_player)
            self.GLabel_333["text"] = "Current Player:" + self.current_player
            self.GButton_732.wait_variable(but_var)
            self.show_game_status()
            #action = input("Choose an action (navigate/exchange/retrieve/event): ")
            self.GLabel_333["text"] = "Choose an action (navigate/exchange/retrieve/event): "
            self.GButton_732.wait_variable(but_var)
            action = self.GLineEdit_751.get()
            self.GLineEdit_751.delete(0, 'end')
            if action == "navigate":
                self.navigate()
            elif action == "exchange":
                self.exchange()
            elif action == "retrieve":
                if self.are_players_in_entanglion():
                    self.retrieve()
                else:
                    #print("Cannot retrieve outside Entanglion.")
                    self.GLabel_333["text"] = "Cannot retrieve outside Entanglion."
                    self.GButton_732.wait_variable(but_var)
                                  
            elif action == "event":
                self.draw_event_card()
            else:
                #print("Invalid action. Please try again.")
                self.GLabel_333["text"] = "Invalid action. Please try again."
                self.GButton_732.wait_variable(but_var)
            # Check win condition
            if self.check_win_condition():
                #print("Congratulations! You have collected all the quantum components and won the game!")
                self.GLabel_333["text"] = "Congratulations! You have collected all the quantum components and won the game!"
                self.GButton_732.wait_variable(but_var)
                break
            # Check loss condition
            if self.detection_rate >= 10:
                #print("The detection rate has reached the maximum level. The game ends in a loss!")
                self.GLabel_333["text"] = "The detection rate has reached the maximum level. The game ends in a loss!"
                self.GButton_732.wait_variable(but_var)
                break
            # Switch to the other player
            self.switch_player()

    def navigate(self):
        player = self.current_player
        #print(f"Player {player}, navigating...")
        self.GLabel_333["text"] = "Player " + player + ", navigating..."
        self.GButton_732.wait_variable(but_var)
        #card = input("Choose an engine card from your hand: ")
        self.GLabel_333["text"] = "Choose an engine card from your hand: "
        self.GButton_732.wait_variable(but_var)
        card = self.GLineEdit_751.get()
        self.GLineEdit_751.delete(0, 'end')
        if card in self.engine_control[player]:
            self.engine_control[player].remove(card)
            self.engine_discard.append(card)
            #print("Engine card played:", card)
            self.GLabel_333["text"] = "Engine card played:" + card
            self.GButton_732.wait_variable(but_var)

            if card == "X":
                if self.ship_locations[player]["Galaxy"] == "Centarious" and self.ship_locations[player]["Planet"] in ["ZERO", "ONE"]:
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Superious" and self.ship_locations[other_player]["Planet"] == "PLUS":
                        self.update_ship_location(player, "Centarious", self.ship_locations[player]["Planet"], "Entanglion", "PHI_PLUS")
                        self.update_ship_location(other_player, "Superious", "PLUS", "Entanglion", "PHI_PLUS")
                    elif self.ship_locations[other_player]["Galaxy"] == "Superious" and self.ship_locations[other_player]["Planet"] == "MINUS":
                        self.update_ship_location(player, "Centarious", self.ship_locations[player]["Planet"], "Entanglion", "PHI_MINUS")
                        self.update_ship_location(other_player, "Superious", "MINUS", "Entanglion", "PHI_MINUS")
                    else:
                        #print(f"Player {player} cannot navigate with the X card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the X card at the moment."
                        self.GButton_732.wait_variable(but_var)
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] in ["PHI_PLUS", "PHI_MINUS"]:
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Entanglion" and self.ship_locations[other_player]["Planet"] in ["PHI_PLUS", "PHI_MINUS"]:
                        self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "OMEGA_TWO")
                        self.update_ship_location(other_player, "Entanglion", self.ship_locations[other_player]["Planet"], "Entanglion", "OMEGA_TWO")
                    else:
                        #print(f"Player {player} cannot navigate with the X card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the X card at the moment."
                        self.GButton_732.wait_variable(but_var)
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] == "OMEGA_TWO":
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Entanglion" and self.ship_locations[other_player]["Planet"] == "OMEGA_TWO":
                        self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "OMEGA_THREE")
                        self.update_ship_location(other_player, "Entanglion", self.ship_locations[other_player]["Planet"], "Entanglion", "OMEGA_THREE")
                    else:
                        #print(f"Player {player} cannot navigate with the X card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the X card at the moment."
                        self.GButton_732.wait_variable(but_var)
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] == "OMEGA_THREE":
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Entanglion" and self.ship_locations[other_player]["Planet"] == "OMEGA_THREE":
                        self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "OMEGA_ZERO")
                        self.update_ship_location(other_player, "Entanglion", self.ship_locations[other_player]["Planet"], "Entanglion", "OMEGA_ZERO")
                    else:
                        #print(f"Player {player} cannot navigate with the X card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the X card at the moment."
                        self.GButton_732.wait_variable(but_var)
                else:
                    #print(f"Player {player} cannot navigate with the X card at the moment.")
                    self.GLabel_333["text"] = "Player " + player + " cannot navigate with the X card at the moment."
                    self.GButton_732.wait_variable(but_var)
            elif card == "H":
                if self.ship_locations[player]["Galaxy"] == "Superious" and self.ship_locations[player]["Planet"] in ["PLUS", "MINUS"]:
                    self.update_ship_location(player, "Superious", self.ship_locations[player]["Planet"], "Centarious", "ZERO")
                elif self.ship_locations[player]["Galaxy"] == "Centarious" and self.ship_locations[player]["Planet"] == "ZERO":
                    self.update_ship_location(player, "Centarious", "ZERO", "Superious", "PLUS")
                elif self.ship_locations[player]["Galaxy"] == "Centarious" and self.ship_locations[player]["Planet"] == "ONE":
                    self.update_ship_location(player, "Centarious", "ONE", "Superious", "MINUS")
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] in ["PHI_PLUS", "PHI_MINUS"]:
                    self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "OMEGA_TWO")
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] == "OMEGA_TWO":
                    self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "PHI_PLUS")
                else:
                    #print(f"Player {player} cannot navigate with the H card at the moment.")
                    self.GLabel_333["text"] = "Player " + player + " cannot navigate with the H card at the moment."
                    self.GButton_732.wait_variable(but_var)
            elif card == "CNOT":
                if self.ship_locations[player]["Galaxy"] == "Centarious" and self.ship_locations[player]["Planet"] == "ZERO":
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Centarious" and self.ship_locations[other_player]["Planet"] == "ONE":
                        self.update_ship_location(player, "Centarious", "ZERO", "Centarious", "ONE")
                        self.update_ship_location(other_player, "Centarious", "ONE", "Centarious", "ZERO")
                    elif self.ship_locations[other_player]["Galaxy"] == "Superious" and self.ship_locations[other_player]["Planet"] == "PLUS":
                        self.update_ship_location(player, "Centarious", "ZERO", "Entanglion", "PHI_PLUS")
                        self.update_ship_location(other_player, "Superious", "PLUS", "Entanglion", "PHI_PLUS")
                    elif self.ship_locations[other_player]["Galaxy"] == "Superious" and self.ship_locations[other_player]["Planet"] == "MINUS":
                        self.update_ship_location(player, "Centarious", "ZERO", "Entanglion", "PHI_MINUS")
                        self.update_ship_location(other_player, "Superious", "MINUS", "Entanglion", "PHI_MINUS")
                    else:
                        #print(f"Player {player} cannot navigate with the CNOT card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the CNOT card at the moment."
                        self.GButton_732.wait_variable(but_var)
                elif self.ship_locations[player]["Galaxy"] == "Centarious" and self.ship_locations[player]["Planet"] == "ONE":
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Centarious" and self.ship_locations[other_player]["Planet"] == "ZERO":
                        self.update_ship_location(player, "Centarious", "ONE", "Centarious", "ZERO")
                        self.update_ship_location(other_player, "Centarious", "ZERO", "Centarious", "ONE")      
                    elif self.ship_locations[other_player]["Galaxy"] == "Superious" and self.ship_locations[other_player]["Planet"] == "PLUS":
                        self.update_ship_location(player, "Centarious", "ONE", "Entanglion", "PSI_PLUS")
                        self.update_ship_location(other_player, "Superious", "PLUS", "Entanglion", "PSI_PLUS")
                    elif self.ship_locations[other_player]["Galaxy"] == "Superious" and self.ship_locations[other_player]["Planet"] == "MINUS":
                        self.update_ship_location(player, "Centarious", "ONE", "Entanglion", "PSI_MINUS")
                        self.update_ship_location(other_player, "Superious", "MINUS", "Entanglion", "PSI_MINUS")
                    else:
                        #print(f"Player {player} cannot navigate with the CNOT card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the CNOT card at the moment."
                        self.GButton_732.wait_variable(but_var)
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] in ["PHI_PLUS", "PHI_MINUS"]:
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Entanglion" and self.ship_locations[other_player]["Planet"] in ["PHI_PLUS", "PHI_MINUS"]:
                        self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "PHI_PLUS" if self.ship_locations[player]["Planet"] == "PHI_MINUS" else "PHI_MINUS")
                        self.update_ship_location(other_player, "Entanglion", self.ship_locations[other_player]["Planet"], "Entanglion", "PHI_PLUS" if self.ship_locations[other_player]["Planet"] == "PHI_MINUS" else "PHI_MINUS")
                    else:
                        #print(f"Player {player} cannot navigate with the CNOT card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the CNOT card at the moment."
                        self.GButton_732.wait_variable(but_var)
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] == "OMEGA_THREE":
                    other_player = self.get_other_player(player)
                    if self.ship_locations[other_player]["Galaxy"] == "Entanglion" and self.ship_locations[other_player]["Planet"] == "OMEGA_THREE":
                        self.update_ship_location(player, "Entanglion", self.ship_locations[player]["Planet"], "Entanglion", "OMEGA_ZERO")
                        self.update_ship_location(other_player, "Entanglion", self.ship_locations[other_player]["Planet"], "Entanglion", "OMEGA_ZERO")
                    else:
                       # print(f"Player {player} cannot navigate with the CNOT card at the moment.")
                        self.GLabel_333["text"] = "Player " + player + " cannot navigate with the CNOT card at the moment."
                        self.GButton_732.wait_variable(but_var)
                else:
                   # print(f"Player {player} cannot navigate with the CNOT card at the moment.")
                    self.GLabel_333["text"] = "Player " + player + " cannot navigate with the CNOT card at the moment."
                    self.GButton_732.wait_variable(but_var)
            elif card == "SWAP":
                if self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] == "OMEGA_THREE":
                    self.update_ship_location(player, "Entanglion", "OMEGA_THREE", "Entanglion", "OMEGA_ZERO")
                elif self.ship_locations[player]["Galaxy"] == "Entanglion" and self.ship_locations[player]["Planet"] == "OMEGA_ZERO":
                    self.update_ship_location(player, "Entanglion", "OMEGA_ZERO", "Entanglion", "OMEGA_THREE")
                else:
                    #print(f"Player {player} cannot navigate with the SWAP card at the moment.")
                    self.GLabel_333["text"] = "Player " + player + " cannot navigate with the SWAP card at the moment."
                    self.GButton_732.wait_variable(but_var)
            else:
                #print(f"Invalid engine card: {card}")
                self.GLabel_333["text"] = "Invalid engine card: " + card
                self.GButton_732.wait_variable(but_var)
            #print()
        # Draw a replacement card
        new_card = self.draw_engine_cards(player, 1)
        if new_card:
            self.engine_control[player].append(new_card[0])
            #print("New card drawn:", new_card[0])
            self.GLabel_333["text"] = "New card drawn: " + new_card[0]
            self.GButton_732.wait_variable(but_var)


    def update_ship_location(self, player, from_galaxy, from_planet, to_galaxy, to_planet):
        self.ship_locations[player]["Galaxy"] = to_galaxy
        self.ship_locations[player]["Planet"] = to_planet
        #print(f"Player {player}'s ship moved from {from_galaxy} {from_planet} to {to_galaxy} {to_planet}.")
        self.GLabel_333["text"] = "Player " + player + "'s ship moved from " + from_galaxy + " " + from_planet + " to " + to_galaxy + " " + to_planet + "."
        self.GButton_732.wait_variable(but_var)

    def swap_ships(self):
        player1 = "Player1"
        player2 = "Player2"
        self.ship_locations[player1], self.ship_locations[player2] = self.ship_locations[player2], self.ship_locations[player1]
        #print("Ships swapped.")
        self.GLabel_333["text"] = "Ships swapped."
        self.GButton_732.wait_variable(but_var)

    def exchange(self):
        player = self.current_player
        #print(f"Player {player}, exchanging...")
        self.GLabel_333["text"] = "Player " + player + ", exchanging..."
        self.GButton_732.wait_variable(but_var)
        #card = input("Choose an engine card from your hand to discard: ")
        self.GLabel_333["text"] = "Choose an engine card from your hand to discard: "
        self.GButton_732.wait_variable(but_var)
        card = self.GLineEdit_751.get()
        self.GLineEdit_751.delete(0, 'end')
        if card in self.engine_control[player]:
            self.engine_control[player].remove(card)
            self.engine_discard.append(card)
            #print("Engine card discarded:", card)
            self.GLabel_333["text"] = "Engine card discarded: " + card
            self.GButton_732.wait_variable(but_var)
            new_card = self.draw_engine_cards(player, 1)
            if new_card:
                self.engine_control[player].append(new_card[0])
                #print("New card drawn:", new_card[0])
                self.GLabel_333["text"] = "New card drawn: " + new_card[0]
                self.GButton_732.wait_variable(but_var)

    def retrieve(self):
        player = self.current_player
        self.perform_retrieval_mission(player)

    def switch_player(self):
        if self.current_player == "Player1":
            self.current_player = "Player2"
        else:
            self.current_player = "Player1"
            
    def get_other_player(self, player):
        return "Player2" if player == "Player1" else "Player1"
    
    def are_players_in_entanglion(self):
        player1 = "Player1"
        player2 = "Player2"
        return self.ship_locations[player1]["Galaxy"] == "Entanglion" and self.ship_locations[player2]["Galaxy"] == "Entanglion"

    def show_game_status(self):
        self.GLabel_910["text"] = "ساي بلس"
        self.GLabel_101["text"] = "أوميغا صفر"
        self.GLabel_592["text"] = "ساي ماينس"
        self.GLabel_469["text"] = "فاي ماينس"
        self.GLabel_282["text"] = "أوميغا اثنان"
        self.GLabel_452["text"] = "أوميغا واحد"
        self.GLabel_554["text"] = "أوميغا ثلاثة"
        self.GLabel_372["text"] = "صفر"
        self.GLabel_219["text"] = "واحد"
        self.GLabel_978["text"] = "بلس"
        self.GLabel_296["text"] = "ماينس"
        self.GLabel_228["text"] = "معدل الكشف"
        
        #print("Quantum Components Available:", self.quantum_components)
        self.GLabel_104["text"] = str(self.quantum_components)
        self.GLabel_131["text"] = str(self.quantum_components)
        #print("Quantum Event Cards Available:", self.quantum_event_deck)
        self.GLabel_441["text"] = str(self.quantum_event_deck)
        self.GLabel_557["text"] = str(self.quantum_event_deck)
        #print("Detection Rate:", self.detection_rate)
        self.GLabel_228["text"] = "معدل الكشف\n" + str(self.detection_rate)

        for player, location in self.ship_locations.items():
            #print(f"Location {player}: Galaxy - {location['Galaxy']}, Planet - {location['Planet']}")
            temp_player = ""
            if(player == "Player1"):
                temp_player = "اللاعب الأول"
            else:
                temp_player = "اللاعب الثاني"
            if(location['Planet'] == "OMEGA_ZERO"):
                self.GLabel_101["text"] += "\n" + temp_player
            elif(location['Planet'] == "OMEGA_ONE"):
                self.GLabel_452["text"] +=  "\n" + temp_player
            elif(location['Planet'] == "OMEGA_TWO"):
                self.GLabel_282["text"] += "\n" + temp_player
            elif(location['Planet'] == "OMEGA_THREE"):
                self.GLabel_554["text"] +=  "\n" + temp_player
            elif(location['Planet'] == "PSI_PLUS"):
                self.GLabel_910["text"] += "\n" + temp_player
            elif(location['Planet'] == "PSI_MINUS"):
                self.GLabel_592["text"] += "\n" + temp_player
            elif(location['Planet'] == "PHI_PLUS"):
                self.GLabel_469["text"] += "\n" + temp_player
            elif(location['Planet'] == "PHI_MINUS"):
                self.GLabel_372["text"] +="\n" + temp_player
            elif(location['Planet'] == "ZERO"):
                self.GLabel_219["text"] +="\n" + temp_player
            elif(location['Planet'] == "PLUS"):
                self.GLabel_978["text"] += "\n" + temp_player
            elif(location['Planet'] == "MINUS"):
                self.GLabel_296["text"] +="\n" + temp_player
            elif(location['Planet'] == "ONE"):
                self.GLabel_413["text"] += "\n" + temp_player



        for player, cards in self.engine_control.items():
            #print(f"Cards {player}: {cards}")
            if(player == "Player1"):
                self.GLabel_413["text"] = str(cards)
            else:
                self.GLabel_167["text"] = str(cards)

       # print("==================")
        #print()

    def check_win_condition(self):
        return len(self.quantum_components) == 0

# game = EntanglionGame()
# game.play_game()

if __name__ == "__main__":
    root = tk.Tk()
    but_var = tk.IntVar()
    app = EntanglionGame(root)
    app.play_game()
    root.mainloop()