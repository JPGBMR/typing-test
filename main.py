import tkinter as tk
import random
import time

# Sample passages for typing challenge
TEXT_PASSAGES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile programming language loved by developers.",
    "Artificial Intelligence is transforming industries worldwide.",
    "Typing speed can improve with consistent practice and focus.",
    "A journey of a thousand miles begins with a single step.",
    "Knowledge is power, and the application of knowledge is wisdom.",
    "Consistency is the key to mastering any skill.",
    "Great achievements come from small, consistent actions.",
    "Learning never exhausts the mind.",
    "Success is the result of preparation, hard work, and learning from failure.",
    "Challenges are what make life interesting; overcoming them is what makes life meaningful.",
    "Don't watch the clock; do what it does. Keep going.",
    "The only way to do great work is to love what you do.",
    "Opportunities don't happen; you create them.",
    "Start where you are. Use what you have. Do what you can.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "To handle yourself, use your head; to handle others, use your heart.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don't be afraid to give up the good to go for the great.",
    "I find that the harder I work, the more luck I seem to have.",
    "Motivation is what gets you started. Habit is what keeps you going.",
    "The way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today.",
    "You learn more from failure than from success. Don’t let it stop you.",
    "It’s not whether you get knocked down; it’s whether you get up.",
    "If you are working on something that you really care about, you don’t have to be pushed.",
    "People who are crazy enough to think they can change the world are the ones who do.",
    "Failure will never overtake me if my determination to succeed is strong enough.",
    "Knowing is not enough; we must apply. Wishing is not enough; we must do.",
    "We generate fears while we sit. We overcome them by action.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Whether you think you can or think you can’t, you’re right.",
    "Security is mostly a superstition. Life is either a daring adventure or nothing.",
    "The man who has confidence in himself gains the confidence of others.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Creativity is intelligence having fun.",
    "Do what you can with all you have, wherever you are.",
    "To see what is right and not do it is a lack of courage.",
    "Reading is to the mind what exercise is to the body.",
    "The successful warrior is the average man, with laser-like focus.",
    "Happiness is not something ready-made. It comes from your own actions.",
    "Small steps in the right direction can turn out to be the biggest step of your life.",
    "Don't limit your challenges; challenge your limits.",
    "Dream it. Wish it. Do it.",
    "Act as if what you do makes a difference. It does.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Do something today that your future self will thank you for.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Your life does not get better by chance; it gets better by change.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "The best way to predict the future is to create it.",
    "Learn as if you will live forever, live like you will die tomorrow.",
    "Strive not to be a success, but rather to be of value.",
    "The only person you are destined to become is the person you decide to be.",
    "Dream big and dare to fail.",
    "Life isn’t about finding yourself. It’s about creating yourself.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Success is getting what you want. Happiness is wanting what you get.",
    "The harder the conflict, the greater the triumph.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us."
]


class SpeedTyper:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedTyper")
        self.root.geometry("800x450")

        # Initialize variables
        self.timer = 30  # Adjust timer to 30 seconds
        self.current_text = ""
        self.start_time = None
        self.correct_words = 0
        self.total_words_typed = 0
        self.total_characters_typed = 0
        self.word_index = 0
        self.words = []

        # GUI elements
        self.create_ui()

    def create_ui(self):
        # Title
        self.title_label = tk.Label(self.root, text="SpeedTyper", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=10)

        # Instructions
        self.instructions_label = tk.Label(
            self.root, text="Type the text below as quickly and accurately as possible!", font=("Helvetica", 14)
        )
        self.instructions_label.pack(pady=5)

        # Display text
        self.text_display = tk.Text(
            self.root, font=("Courier", 16), wrap="word", height=4, width=80, state="disabled"
        )
        self.text_display.pack(pady=10)

        # Input box
        self.input_box = tk.Entry(self.root, font=("Courier", 14), width=50)
        self.input_box.pack(pady=10)
        self.input_box.bind("<space>", self.validate_word)

        # Timer and scores
        self.timer_label = tk.Label(self.root, text="Time: 30", font=("Helvetica", 16))
        self.timer_label.pack(pady=5)

        self.score_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.score_label.pack(pady=5)

        # Restart button
        self.restart_button = tk.Button(
            self.root, text="Start Game", font=("Helvetica", 14), command=self.start_game
        )
        self.restart_button.pack(pady=10)

        # Quit button
        self.quit_button = tk.Button(self.root, text="Quit", font=("Helvetica", 10), command=self.quit_app)
        self.quit_button.pack(pady=10)

    def start_game(self):
        # Reset variables
        self.timer = 30
        self.correct_words = 0
        self.total_words_typed = 0
        self.total_characters_typed = 0
        self.word_index = 0

        # Reset UI elements
        self.input_box.delete(0, tk.END)
        self.input_box.config(state="normal")
        self.timer_label.config(text=f"Time: {self.timer}")
        self.score_label.config(text="")
        self.restart_button.config(text="Restart Game")
        self.quit_button.config()

        # Select and display a random passage
        self.current_text = random.choice(TEXT_PASSAGES)
        self.words = self.current_text.split()
        self.display_text()

        # Start the timer
        self.start_time = time.time()
        self.update_timer()

    def display_text(self):
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", tk.END)

        for i, word in enumerate(self.words):
            color = "black"
            if i < self.word_index:
                color = "green" if self.words[i] == "CORRECT" else "red"
            self.text_display.insert(tk.END, word + " ", (color,))
        self.text_display.tag_configure("green", foreground="green")
        self.text_display.tag_configure("red", foreground="red")
        self.text_display.tag_configure("black", foreground="black")
        self.text_display.config(state="disabled")

    def validate_word(self, event):
        user_input = self.input_box.get().strip()

        if self.word_index < len(self.words):
            target_word = self.words[self.word_index]

            if user_input == target_word:
                self.words[self.word_index] = "CORRECT"
                self.correct_words += 1

            self.total_words_typed += 1
            self.total_characters_typed += len(user_input)

            self.word_index += 1
            self.input_box.delete(0, tk.END)
            self.display_text()

            if self.word_index == len(self.words):
                self.load_next_passage()

    def load_next_passage(self):
        self.current_text = random.choice(TEXT_PASSAGES)
        self.words = self.current_text.split()
        self.word_index = 0
        self.display_text()

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, self.timer - elapsed_time)
        self.timer_label.config(text=f"Time: {remaining_time}")

        if remaining_time > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        # Calculate scores
        wpm = (self.correct_words * 60) // self.timer  # Extrapolate to words per minute
        accuracy = (self.correct_words / self.total_words_typed * 100) if self.total_words_typed > 0 else 0

        # Lock input box
        self.input_box.config(state="disabled")

        # Display scores
        self.score_label.config(text=f"WPM: {wpm}, Accuracy: {accuracy:.2f}%")

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTyper(root)
    root.mainloop()