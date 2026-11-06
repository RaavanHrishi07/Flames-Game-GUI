
import tkinter as tk
from tkinter import messagebox


class FlamesGame:
    def __init__(self, root):
        self.root = root
        self.root.title("FLAMES - Relationship Calculator")
        self.root.geometry("600x760")
        self.root.minsize(500, 700)
        self.root.configure(bg="#FFF0F5")

        self.colors = {
            "background": "#FFF0F5",
            "card": "#FFFFFF",
            "primary": "#D94680",
            "secondary": "#8B5CF6",
            "text": "#35243A",
            "muted": "#8B7B91",
            "input": "#FFF7FB"
        }

        self.setup_ui()
        self.root.bind("<Return>", lambda event: self.calculate_flames())

    def setup_ui(self):
        header = tk.Frame(self.root, bg=self.colors["background"])
        header.pack(fill="x", pady=(30, 15))

        tk.Label(
            header,
            text="💕 FLAMES GAME",
            font=("Segoe UI", 27, "bold"),
            bg=self.colors["background"],
            fg=self.colors["primary"]
        ).pack()

        tk.Label(
            header,
            text="Discover your relationship compatibility",
            font=("Segoe UI", 11),
            bg=self.colors["background"],
            fg=self.colors["muted"]
        ).pack(pady=(7, 0))

        card = tk.Frame(
            self.root,
            bg=self.colors["card"],
            padx=35,
            pady=30,
            highlightthickness=1,
            highlightbackground="#F3D6E4"
        )
        card.pack(fill="both", expand=True, padx=35, pady=15)

        tk.Label(
            card,
            text="Enter Your Names",
            font=("Segoe UI", 17, "bold"),
            bg="white",
            fg=self.colors["text"]
        ).pack(pady=(0, 22))

        self.player1 = self.create_input(card, "Player 1")
        self.player2 = self.create_input(card, "Player 2")

        button_frame = tk.Frame(card, bg="white")
        button_frame.pack(fill="x", pady=(25, 20))

        tk.Button(
            button_frame,
            text="💗  Calculate FLAMES",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors["primary"],
            fg="white",
            activebackground="#BE185D",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=12,
            command=self.calculate_flames
        ).pack(fill="x", pady=(0, 10))

        tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 10, "bold"),
            bg="#F3E8FF",
            fg=self.colors["secondary"],
            activebackground="#E9D5FF",
            relief="flat",
            cursor="hand2",
            pady=9,
            command=self.clear_all
        ).pack(fill="x")

        self.result_card = tk.Frame(
            card,
            bg="#FFF0F5",
            padx=15,
            pady=20
        )
        self.result_card.pack(fill="x", pady=(10, 0))

        tk.Label(
            self.result_card,
            text="YOUR RESULT",
            font=("Segoe UI", 9, "bold"),
            bg="#FFF0F5",
            fg=self.colors["muted"]
        ).pack()

        self.result_label = tk.Label(
            self.result_card,
            text="✨",
            font=("Segoe UI", 25, "bold"),
            bg="#FFF0F5",
            fg=self.colors["primary"]
        )
        self.result_label.pack(pady=(8, 3))

        self.description_label = tk.Label(
            self.result_card,
            text="Enter two names to discover the result!",
            font=("Segoe UI", 10),
            bg="#FFF0F5",
            fg=self.colors["muted"],
            wraplength=400
        )
        self.description_label.pack()

        tk.Label(
            self.root,
            text="Just for fun! Not a real compatibility test 💕",
            font=("Segoe UI", 9),
            bg=self.colors["background"],
            fg=self.colors["muted"]
        ).pack(pady=(0, 18))

        self.player1.focus_set()

    def create_input(self, parent, label_text):
        frame = tk.Frame(parent, bg="white")
        frame.pack(fill="x", pady=9)

        tk.Label(
            frame,
            text=label_text,
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg=self.colors["text"]
        ).pack(anchor="w", pady=(0, 7))

        entry = tk.Entry(
            frame,
            font=("Segoe UI", 13),
            bg=self.colors["input"],
            fg=self.colors["text"],
            insertbackground=self.colors["primary"],
            relief="flat",
            highlightthickness=1,
            highlightbackground="#F3D6E4",
            highlightcolor=self.colors["primary"]
        )
        entry.pack(fill="x", ipady=11, padx=2)

        return entry

    @staticmethod
    def calculate_remaining_count(name1, name2):
        first = list(name1.lower())
        second = list(name2.lower())

        first = [char for char in first if char.isalpha()]
        second = [char for char in second if char.isalpha()]

        for char in first[:]:
            if char in second:
                first.remove(char)
                second.remove(char)

        return len(first) + len(second)

    @staticmethod
    def get_flames_result(count):
        results = [
            "Friends",
            "Love",
            "Affection",
            "Marriage",
            "Enemy",
            "Siblings"
        ]

        index = 0

        while len(results) > 1:
            index = (index + count - 1) % len(results)
            results.pop(index)

        return results[0]

    def calculate_flames(self):
        name1 = self.player1.get().strip()
        name2 = self.player2.get().strip()

        if not name1 or not name2:
            messagebox.showwarning(
                "Missing Names",
                "Please enter both names before calculating."
            )
            return

        if not any(char.isalpha() for char in name1):
            messagebox.showwarning(
                "Invalid Name",
                "Player 1 must contain at least one letter."
            )
            return

        if not any(char.isalpha() for char in name2):
            messagebox.showwarning(
                "Invalid Name",
                "Player 2 must contain at least one letter."
            )
            return

        count = self.calculate_remaining_count(name1, name2)
        result = self.get_flames_result(count)

        self.result_label.configure(
            text=self.get_emoji(result)
        )

        self.description_label.configure(
            text=f"{name1.title()} + {name2.title()}\n\n{result.upper()}",
            fg=self.colors["primary"],
            font=("Segoe UI", 12, "bold")
        )

    @staticmethod
    def get_emoji(result):
        emojis = {
            "Friends": "🤝",
            "Love": "❤️",
            "Affection": "🥰",
            "Marriage": "💍",
            "Enemy": "⚡",
            "Siblings": "👫"
        }
        return emojis.get(result, "💕")

    def clear_all(self):
        self.player1.delete(0, tk.END)
        self.player2.delete(0, tk.END)

        self.result_label.configure(text="✨")
        self.description_label.configure(
            text="Enter two names to discover the result!",
            fg=self.colors["muted"],
            font=("Segoe UI", 10)
        )

        self.player1.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = FlamesGame(root)
    root.mainloop()
