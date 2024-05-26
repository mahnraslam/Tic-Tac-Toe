import tkinter as tk
from Game import Playing

class GameBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.obj = Playing(3, 3, 3)
        self.configure(bg='Cadet Blue')
        self.title("Tic Tac Toe")
        self.geometry("800x650")
        self.maxsize(850, 650)
        self.player = 1  # Initialize the player attribute
        self.board = [[None for _ in range(3)] for _ in range(3)]  # Initialize the board attribute
        self.main_board()
        self.winner_frame = None  # Initialize the winner frame attribute
        self.partner = 'Friend'
    def main_board(self):
        f1 = tk.Frame(self, bg='Cadet Blue')
        f1.grid(row=0, column=0, pady=15)
        tk.Label(f1, font=('arial', 20, 'bold'), text="Tic Tac Toe", fg="#000000", width=10, height=2, bg="light gray", padx=30).grid(row=0, column=0)

        # Upper Frame
        Upper_frame = tk.Frame(self, bg='Cadet Blue', padx=70, pady=10)
        Upper_frame.grid(row=1, column=0)

        i1 = tk.Label(Upper_frame, font=('arial', 14, 'bold'), text="Play With:", fg="#000000", width=10, height=2, bg="Sky Blue", padx=20)
        i1.grid(row=0, column=0, sticky='w')

        i2 = tk.Button(Upper_frame, font=('arial', 13, 'bold'), text="Friends", fg="#000000", width=7, height=2, bg="Sky Blue", bd=2,command = lambda : self.changePartner('Friend'))
        i2.grid(row=0, column=1, sticky='w')

        i3 = tk.Button(Upper_frame, font=('arial', 13, 'bold'), text="Computer", fg="#000000", width=8, height=2, bg="Sky Blue", bd=2,command=lambda: self.changePartner("Computer"))
        i3.grid(row=0, column=2, sticky='w')

        spacer = tk.Label(Upper_frame, width=2, bg="Cadet Blue")
        spacer.grid(row=0, column=3)

        i4 = tk.Label(Upper_frame, font=('arial', 15, 'bold'), text="Player 1: 'O'", fg="#000000", width=10, height=2, bg="Sky Blue", padx=20, bd=2)
        i4.grid(row=0, column=4, sticky='w')

        i5 = tk.Label(Upper_frame, font=('arial', 15, 'bold'), text="Player 2: 'X'", fg="#000000", width=9, height=2, bg="Sky Blue", bd=2)
        i5.grid(row=0, column=5, sticky='w')

        quit_frame = tk.Frame(self, bg='Cadet Blue', padx=70, pady=10)
        quit_frame.grid(row=3, column=0)

        quit_button = tk.Button(quit_frame, font=('arial', 14, 'bold'), text="Quit", fg="#000000", width=4, height=1, bg="light gray", padx=20, command=self.destroy)
        quit_button.grid(row=0, column=0, sticky='w')

        self.Lower_frame = tk.Frame(self, bg="Cadet Blue", pady=20)
        self.Lower_frame.grid(row=2, column=0)

        frame1 = tk.Frame(self.Lower_frame, bd=4, highlightthickness=4, bg="Cadet Blue", highlightbackground="light gray", highlightcolor="light gray")
        frame1.grid(row=0, column=0, sticky='nsew')
        self.create_buttons(frame1, "frame1")

        frame2 = tk.Frame(self.Lower_frame, bd=4, highlightthickness=4, bg="Cadet Blue", highlightbackground="light gray", highlightcolor="light gray")
        frame2.grid(row=1, column=1, sticky='nsew')
        self.create_buttons(frame2, "frame2")

        frame3 = tk.Frame(self.Lower_frame, bd=4, highlightthickness=4, bg="Cadet Blue", highlightbackground="light gray", highlightcolor="light gray")
        frame3.grid(row=2, column=2, sticky='nsew')
        self.create_buttons(frame3, "frame3")

    def create_buttons(self, frame, frame_name):
        for r in range(3):
            for c in range(3):
                button_name = f"{frame_name}_R{r}C{c}"
                button = tk.Button(frame, font=('arial', 13, 'bold'), bg="Sky Blue", fg="#000000", bd=2, justify='center', width=5, 
                                   command=lambda r=r, c=c, frame_name=frame_name: self.switch(frame_name, r, c), highlightbackground="light gray", highlightcolor="light gray")
                button.grid(row=r, column=c, sticky='nsew')
                setattr(self, button_name, button)

    def computerTurn(self):
        frame,row,col = self.obj.putAutomatically()
         
        if   frame!=-1 and row!= -1 and col!=-1 :
            if self.obj.array[frame][row][col]==0:
                self.obj.array[frame][row][col] = "X"
               
                self.player = 1      
                if frame == 0:
                    frame_name = "frame1"
                elif frame == 1:
                    frame_name = "frame2"
                elif frame == 2:
                    frame_name = "frame3"
        
                button_name = f"{frame_name}_R{row}C{col}"
                button = getattr(self, button_name, None)
                button.config(text="X", fg="#000133")  # Update the button text
            else: 
                print("Else condition calls", frame,row,col)
                print(self.obj.array) 
        z = self.obj.winning()
        if z != -1:
            self.display_winner("Computer")

        if self.obj.is_draw():    
            self.display_winner("None")
    def changePartner(self,other):
        self.partner =  other
       
    def reset_board(self):
        for frame in ["frame1", "frame2", "frame3"]:
            for r in range(3):
                for c in range(3):
                    button_name = f"{frame}_R{r}C{c}"
                    button = getattr(self, button_name, None)
                    if button:
                        button.config(text="", state="normal")  # Reset button text and enable it
        self.obj = Playing(3, 3, 3)
        self.player = 1  # Reset the player to Player 1
        if self.winner_frame:
            self.winner_frame.destroy()  # Destroy the winner frame

    def display_winner(self,p):
        # Disable all buttons
        for frame in ["frame1", "frame2", "frame3"]:
            for r in range(3):
                for c in range(3):
                    button_name = f"{frame}_R{r}C{c}"
                    button = getattr(self, button_name, None)
                    if button:
                        button.config(state="disabled")

        self.winner_frame = tk.Frame(self, bg='light gray')
        self.winner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        if p!=None : 
            winner_label = tk.Label(self.winner_frame, text=f"{p} wins!", font=('arial', 20, 'bold'), fg="#000000", bg='light gray', padx=20, pady=10)
            winner_label.pack(pady=10)
        elif p == None:
            winner_label = tk.Label(self.winner_frame, text=f"Game Draw!", font=('arial', 20, 'bold'), fg="#000000", bg='light gray', padx=20, pady=10)
            winner_label.pack(pady=10)
        restart_button = tk.Button(self.winner_frame, text="Restart", font=('arial', 14, 'bold'), fg="light gray", bg="#000000", command=self.reset_board)
        restart_button.pack(pady=10)
        
     
    def switch(self, frame_name, row, col):
        button_name = f"{frame_name}_R{row}C{col}"
        button = getattr(self, button_name, None)
        # Determine the frame number
        if frame_name == "frame1":
            frame = 0
        elif frame_name == "frame2":
            frame = 1
        elif frame_name == "frame3":
            frame = 2
        else:
            return

        if self.player == 1 and self.obj.array[frame][row][col] == 0:
            self.obj.array[frame][row][col] = "O"
            button.config(text="O", fg="red")
            self.player = 2
            z = self.obj.winning()
            if z != -1:
                self.display_winner("Player 1")
            elif self.obj.is_draw():
                self.display_winner("None")
            elif self.partner == "Computer":
                self.computerTurn()
        elif self.partner != "Computer" and self.player == 2 and self.obj.array[frame][row][col] == 0:
            self.obj.array[frame][row][col] = "X"
            button.config(text="X", fg="#000133")
            self.player = 1
            z = self.obj.winning()
            if z != -1:
                self.display_winner("Player 2")
            elif self.obj.is_draw():
                self.display_winner("None")
if __name__ == "__main__":
    game = GameBoard()
    game.mainloop()
