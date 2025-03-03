import random

class Game:
    def __init__(self):
        self.users = {}  # Store user data in a dictionary

    def new_user(self, name):
        if name in self.users:
            print("🔴 User already exists. Please log in as an existing user.")
            return
        self.users[name] = 500
        print(f"🎉 Welcome {name}! You have been given ₹500 to start the game. Let's play!")

    def existing_user(self, name):
        if name not in self.users:
            print("🔴 User not found. Please create a new account.")
            return False
        print(f"👋 Welcome back, {name}! Your current balance is ₹{self.users[name]}.")
        return True

    def play_game(self, name):
        if name not in self.users:
            print("🔴 User not found. Please create a new account or log in.")
            return

        while True:
            print(f"💰 Your current balance: ₹{self.users[name]}")
            try:
                bet_amount = int(input("💵 Enter your bet amount (10, 50, 100): "))
                if bet_amount not in [10, 50, 100]:
                    print("⚠️ Invalid bet amount. Please choose 10, 50, or 100.")
                    continue
                if self.users[name] < bet_amount:
                    print("⚠️ Insufficient balance. Please choose a lower bet amount.")
                    continue
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue

            random_number = random.randint(1, 10)
            print("🎲 A number between 1 and 10 has been chosen. Can you guess it?")

            # 3 attempts with decreasing rewards
            for attempt in range(1, 4):
                try:
                    guessed_number = int(input(f"🔢 Attempt {attempt}/3: Guess a number: "))
                    if guessed_number < 1 or guessed_number > 10:
                        print("⚠️ Invalid number. Please choose a number between 1 and 10.")
                        continue
                except ValueError:
                    print("⚠️ Please enter a valid number.")
                    continue

                if guessed_number == random_number:
                    multiplier = 2 if attempt == 1 else 1.5 if attempt == 2 else 1.2
                    winnings = int((bet_amount * multiplier)-bet_amount)
                    print(f"🎉 Congratulations! You guessed correctly on attempt {attempt}. You win ₹{winnings}.")
                    self.users[name] += winnings
                    break
                else:
                    if attempt < 3:
                        hint = "higher" if guessed_number < random_number else "lower"
                        print(f"❌ Wrong guess! Try guessing a {hint} number.")
                    else:
                        print("❌ Sorry, you used all your attempts. Better luck next time!")

            if guessed_number != random_number:
                print(f"💔 The correct number was {random_number}. You lose ₹{bet_amount}.")
                self.users[name] -= bet_amount

            if self.users[name] <= 0:
                print("💔 You have run out of balance. Game over!")
                break

            play_again = input("🔄 Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("🙌 Thank you for playing! See you next time!")
                break

    def start_game(self):
        while True:
            print("\n🎮 Welcome to the Three SHots of Luck Game! 🎲")
            user_type = input("🆕 Are you a new user or an existing user? (new/existing): ").lower()
            name = input("✏️ Enter your name: ")

            if user_type == "new":
                self.new_user(name)
            elif user_type == "existing":
                if not self.existing_user(name):
                    continue
            else:
                print("⚠️ Invalid option. Please choose 'new' or 'existing'.")
                continue

            self.play_game(name)

            exit_game = input("❓ Do you want to exit the game? (yes/no): ").lower()
            if exit_game == 'yes':
                print("👋 Goodbye! See you next time. 🎉")
                break

# Start the game
game = Game()
game.start_game()
