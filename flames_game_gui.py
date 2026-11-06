
import tkinter as tk
from tkinter import messagebox


class FlamesGame:
    def __init__(self, root):
        self.root = root
        self.root.title("FLAMES Game")
        self.root.geometry("600x760")
        self.root.minsize(500, 700)
        self.root.configure(bg="#FFF7FB")

        self.colors = {
            "background": "#FFF7FB",
            "card": "#FFFFFF",
            "primary": "#DB2777",
            "secondary": "#9333EA",
            "text": "#3F3F46",
            "muted": "#71717A",
            "border": "#FBCFE8",
        }

        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(
            self.root,
            bg=self.colors["background"],
            padx=30,
            pady=20
        )
        main_frame.pack(fill="both", expand=True)

        # Header
        tk.Label(
            main_frame,
            text="FLAMES",
            font=("Segoe UI", 30, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        ).pack(pady=(5, 0))

        tk.Label(
            main_frame,
            text="Discover your relationship destiny!",
            font=("Segoe UI", 11),
            fg=self.colors["muted"],
            bg=self.colors["background"]
        ).pack(pady=(0, 20))

        # Input card
        input_card = tk.Frame(
            main_frame,
            bg=self.colors["card"],
            padx=25,
            pady=20,
            highlightthickness=1,
            highlightbackground=self.colors["border"]
        )
        input_card.pack(fill="x", pady=5)

        tk.Label(
            input_card,
            text="PLAYER 1",
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["secondary"],
            bg=self.colors["card"]
        ).pack(anchor="w")

        self.player1 = tk.Entry(
            input_card,
            font=("Segoe UI", 14),
            relief="flat",
            bg="#FDF2F8",
            fg=self.colors["text"],
            insertbackground=self.colors["primary"]
        )
        self.player1.pack(fill="x", ipady=10, pady=(7, 15))

        tk.Label(
            input_card,
            text="PLAYER 2",
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["secondary"],
            bg=self.colors["card"]
        ).pack(anchor="w")

        self.player2 = tk.Entry(
            input_card,
            font=("Segoe UI", 14),
            relief="flat",
            bg="#FDF2F8",
            fg=self.colors["text"],
            insertbackground=self.colors["primary"]
        )
        self.player2.pack(fill="x", ipady=10, pady=(7, 5))

        # Buttons
        button_frame = tk.Frame(
            main_frame,
            bg=self.colors["background"]
        )
        button_frame.pack(fill="x", pady=15)

        tk.Button(
            button_frame,
            text="✨  Calculate FLAMES",
            command=self.calculate_flames,
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["primary"],
            fg="white",
            activebackground="#BE185D",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=12
        ).pack(fill="x", pady=(0, 10))

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_all,
            font=("Segoe UI", 11, "bold"),
            bg="#F3E8FF",
            fg=self.colors["secondary"],
            activebackground="#E9D5FF",
            activeforeground=self.colors["secondary"],
            relief="flat",
            cursor="hand2",
            pady=10
        ).pack(fill="x")

        # Result card
        self.result_card = tk.Frame(
            main_frame,
            bg="#FFF0F5",
            height=190,
            highlightthickness=1,
            highlightbackground="#F9A8D4"
        )
        self.result_card.pack(fill="x", pady=(5, 0))
        self.result_card.pack_propagate(False)

        tk.Label(
            self.result_card,
            text="YOUR RESULT",
            font=("Segoe UI", 11, "bold"),
            fg=self.colors["secondary"],
            bg="#FFF0F5"
        ).pack(pady=(15, 5))

        # One label for the complete result
        self.result_label = tk.Label(
            self.result_card,
            text="✨\n\nEnter two names to discover the result!",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors["muted"],
            bg="#FFF0F5",
            justify="center"
        )
        self.result_label.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # Enter key support
        self.player1.bind(
            "<Return>",
            lambda event: self.player2.focus_set()
        )
        self.player2.bind(
            "<Return>",
            lambda event: self.calculate_flames()
        )

        self.player1.focus_set()

    def calculate_remaining_count(self, name1, name2):
        name1 = "".join(
            char.lower() for char in name1 if char.isalpha()
        )
        name2 = "".join(
            char.lower() for char in name2 if char.isalpha()
        )

        list1 = list(name1)
        list2 = list(name2)

        for char in list1[:]:
            if char in list2:
                list1.remove(char)
                list2.remove(char)

        return len(list1) + len(list2)

    def get_flames_result(self, count):
        flames = [
            "Friends",
            "Love",
            "Affection",
            "Marriage",
            "Enemy",
            "Siblings"
        ]

        if count == 0:
            return "Friends"

        index = 0

        while len(flames) > 1:
            index = (index + count - 1) % len(flames)
            flames.pop(index)

        return flames[0]

    def get_emoji(self, result):
        emojis = {
            "Friends": "🤝",
            "Love": "❤️",
            "Affection": "🥰",
            "Marriage": "💍",
            "Enemy": "⚡",
            "Siblings": "👫"
        }

        return emojis.get(result, "✨")

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
        emoji = self.get_emoji(result)

        result_text = (
            f"{emoji}\n\n"
            f"{name1.title()} + {name2.title()}\n"
            f"{result.upper()}"
        )

        self.result_label.configure(
            text=result_text,
            font=("Segoe UI", 15, "bold"),
            fg=self.colors["primary"],
            bg="#FCE7F3"
        )

        self.result_card.configure(
            bg="#FCE7F3",
            highlightbackground="#F9A8D4"
        )

    def clear_all(self):
        self.player1.delete(0, tk.END)
        self.player2.delete(0, tk.END)

        self.result_label.configure(
            text="✨\n\nEnter two names to discover the result!",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors["muted"],
            bg="#FFF0F5"
        )

        self.result_card.configure(
            bg="#FFF0F5",
            highlightbackground="#F9A8D4"
        )

        self.player1.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = FlamesGame(root)
    root.mainloop()
