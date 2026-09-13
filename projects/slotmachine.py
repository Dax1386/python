import random

def spin_row():
    symbols = ["🍒", "🍋", "🍊", "🍉", "🍇"]
    row = [random.choice(symbols) for _ in range(3)]
    return row

def print_row(row):
    print(" | ".join(row))

def check_win(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 10
        elif row[0] == "🍋":
            return  bet * 20
        elif row[0] == "🍊":
            return bet * 40
        elif row[0] == "🍉":
            return  bet * 50
        elif row[0] == "🍇":
            return  bet * 60
        
    elif row[0] == row[1] :
        if row[0] and row[1] == "🍒":
            return  bet * 2
        elif row[0] and row[1] == "🍋":
            return bet * 4
        elif row[0] and row[1] == "🍊":
            return  bet * 6
        elif row[0] and row[1] == "🍉":
            return bet * 8
        elif row[0] and row[1] == "🍇":
            return  bet * 10
        
    elif row[0] == row[2] :
        if row[0] and row[2] == "🍒":
            return  bet * 2
        elif row[0] and row[2] == "🍋":
            return bet * 4
        elif row[0] and row[2] == "🍊":
            return  bet * 6
        elif row[0] and row[2] == "🍉":
            return bet * 8
        elif row[0] and row[2] == "🍇":
            return  bet * 10
        
    elif row[1] == row[2] :
            if row[1] and row[2] == "🍒":
                return  bet * 2
            elif row[1] and row[2] == "🍋":
                return bet * 4
            elif row[1] and row[2] == "🍊":
                return  bet * 6
            elif row[1] and row[2] == "🍉":
                return bet * 8
            elif row[1] and row[2] == "🍇":
                return  bet * 10
    return 0

def main():
    print("------------------------------")
    print("Welcome to the Slot Machine Game!")
    print("Symbols: 🍒 🍋 🍊 🍉 🍇")
    print("------------------------------")

    balance = input("Enter your balance: ")
    while not balance.isdigit():
        print("Invalid input. Please enter a valid number.")
        balance = input("Enter your balance: ")
    
    balance = int(balance)
    if balance <= 0:
        print("Invalid input. Please enter a positive number.")
        return

    while balance > 0:
        print(f"\nYour current balance is: {balance}")
        
        bet = input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Invalid bet amount. Please enter a valid number.")
            continue
        
        bet = int(bet)
        if bet <= 0:
            print("Invalid bet amount. Please enter a positive number.")
            continue
        if bet > balance:
            print("Invalid bet amount. Please enter an amount within your balance.")
            continue

        balance -= bet
        row = spin_row()
        print_row(row)

        payout = check_win(row, bet)
        if payout > 0:
            print(f"You win! Payout: {payout}")
        else:
            print("You lose.")

        balance += payout

        play_again = input("if you play again?").lower()
        if play_again != 'y':
            print("thank you for playing")
            break

main()