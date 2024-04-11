'''
This is my first attempt to make a tamagotchi integrated game using python and integrated tkinter library. 😊
'''
import tkinter as tk
import random

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.feeding = random.randint(60, 80)
        self.happiness = random.randint(60, 80)
        self.health = random.randint(60, 80)
        self.time_total = 0

    def feed(self):
        self.feeding += random.randint(0, 7)
        if self.feeding > 100:
            self.feeding = 100
        self.check_health()
        self.increment_time()

    def play(self):
        self.feeding -= random.randint(0, 7)
        if self.feeding < 25:
            self.health -= 9
        self.happiness += random.randint(1, 8)
        if self.happiness > 100:
            self.happiness = 100
        self.check_health()
        self.increment_time()

    def pass_time(self):
        self.time_total += 10
        self.feeding -= random.randint(0, 4)
        self.health -= random.randint(0, 3)
        self.happiness -= random.randint(0, 8)
        if self.happiness < 0:
            self.happiness = 0
        self.check_health()
        self.increment_time()

    def cure(self):
        self.health += random.randint(0, 19)
        if self.health > 100:
            self.health = 100
        self.happiness -= random.randint(0, 3)
        if self.happiness < 0:
            self.happiness = 0
        self.check_health()
        self.increment_time()

    def check_health(self):
        if self.feeding <= 0 or self.happiness <= 0 or self.health <= 0:
            return True
        return False

    def increment_time(self):
        self.time_total += 4

class TamagotchiApp:
    def __init__(self, master, tamagotchi):
        self.master = master
        self.master.title("Tamagotchi")
        self.tamagotchi = tamagotchi

        self.create_widgets()

    def create_widgets(self):
        self.feed_button = tk.Button(self.master, text="🍔 Feed", command=self.feed)
        self.feed_button.pack()

        self.play_button = tk.Button(self.master, text="🎮 Play", command=self.play)
        self.play_button.pack()

        self.time_button = tk.Button(self.master, text="⏰ Time", command=self.pass_time)
        self.time_button.pack()

        self.cure_button = tk.Button(self.master, text="💊 Cure", command=self.cure)
        self.cure_button.pack()

        self.feeding_label = tk.Label(self.master, text="Feeding:  ")
        self.feeding_label.pack()

        self.happiness_label = tk.Label(self.master, text="Happiness:  ")
        self.happiness_label.pack()

        self.health_label = tk.Label(self.master, text="Health:  ")
        self.health_label.pack()

        self.time_label = tk.Label(self.master, text="Time Total:  ")
        self.time_label.pack()

        self.message_label = tk.Label(self.master, text="", fg="red")
        self.message_label.pack()

        self.update_labels()

    def update_labels(self):
        self.feeding_label.config(text=f"Feeding: {self.tamagotchi.feeding}")
        self.happiness_label.config(text=f"Happiness: {self.tamagotchi.happiness}")
        self.health_label.config(text=f"Health: {self.tamagotchi.health}")
        self.time_label.config(text=f"Time Total: {self.tamagotchi.time_total} minutes")

    def feed(self):
        self.tamagotchi.feed()
        self.update_labels()
        if self.tamagotchi.check_health():
            self.message_label.config(text="Your Tamapet has passed away")
            self.disable_buttons()

    def play(self):
        self.tamagotchi.play()
        self.update_labels()
        if self.tamagotchi.check_health():
            self.message_label.config(text="Your Tamapet has passed away")
            self.disable_buttons()

    def pass_time(self):
        self.tamagotchi.pass_time()
        self.update_labels()
        if self.tamagotchi.check_health():
            self.message_label.config(text="Your Tamapet has passed away")
            self.disable_buttons()

    def cure(self):
        self.tamagotchi.cure()
        self.update_labels()
        if self.tamagotchi.check_health():
            self.message_label.config(text="Your Tamapet has passed away")
            self.disable_buttons()

    def disable_buttons(self):
        self.feed_button.config(state="disabled")
        self.play_button.config(state="disabled")
        self.time_button.config(state="disabled")
        self.cure_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    my_tamagotchi = Tamagotchi(name="Tama")
    app = TamagotchiApp(root, tamagotchi=my_tamagotchi)
    root.mainloop()
