import customtkinter
import tkinter as tk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.circles = []
        self.circle_states = []

        for i in range(7):
            circle = customtkinter.CTkLabel(self, text="", width=20, height=20, corner_radius=10, fg_color="green")
            circle.grid(row=0, column=i, padx=5, pady=20)
            circle.bind("<Button-1>", lambda e, idx=i: self.toggle_circle(idx))
            self.circles.append(circle)
            self.circle_states.append("o")

        self.save_button = customtkinter.CTkButton(self, text="Salvar Estados", command=self.save_states)
        self.save_button.grid(row=1, column=0, columnspan=7, pady=10)

        self.result_label = customtkinter.CTkLabel(self, text="")
        self.result_label.grid(row=2, column=0, columnspan=7, pady=10)

        self.start_blinking()

    def start_blinking(self):
        self.blink()

    def blink(self):
        for idx, circle in enumerate(self.circles):
            if self.circle_states[idx] == "B":
                current_color = circle.cget("fg_color")
                new_color = "transparent" if current_color == "green" else "green"
                circle.configure(fg_color=new_color)
            elif self.circle_states[idx] == "O":
                circle.configure(fg_color="green")
            elif self.circle_states[idx] == "o":
                circle.configure(fg_color="gray")

        self.after(500, self.blink)

    def toggle_circle(self, idx):
        if self.circle_states[idx] == "B":
            self.circle_states[idx] = "O"
        elif self.circle_states[idx] == "O":
            self.circle_states[idx] = "o"
        else:
            self.circle_states[idx] = "B"

    def save_states(self):
        states = list(self.circle_states)
        print("Estados salvos:", states)
        
        message = self.get_message_for_states(states)
        self.result_label.configure(text=message)

    def get_message_for_states(self, states):
        if states == ["B"] * 7:
            return "Todos os LEDs estão piscando!"
        elif states == ["O"] * 7:
            return "Todos os LEDs estão fixos em verde."
        elif "gray" in states:
            return "Alguns LEDs estão em cinza."
        else:
            return "Configuração personalizada dos LEDs."

app = App()
app.mainloop()