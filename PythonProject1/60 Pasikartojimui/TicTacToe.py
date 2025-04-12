# 1. Sukuriame tuščią žaidimo lentą – 3x3 matrica
board = [" " for _ in range(9)]

# 2. Atvaizduojame lentą vartotojui
def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()

# 3. Patikriname, ar žaidėjas laimėjo
def check_winner(player):
    # Laimėjimo kombinacijos: eilutės, stulpeliai, įstrižainės
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # eilutės
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # stulpeliai
        [0, 4, 8], [2, 4, 6]              # įstrižainės
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# 4. Patikriname, ar lenta pilna (lygiosios)
def is_draw():
    return all(cell != " " for cell in board)

# 5. Paleidžiame žaidimo ciklą
def play_game():
    current_player = "X"

    while True:
        print_board()
        try:
            move = int(input(f"Žaidėjas {current_player}, pasirink langelį (1-9): ")) - 1
        except ValueError:
            print("Netinkamas įvestis. Bandyk dar kartą.")
            continue

        if move < 0 or move > 8:
            print("Langelis turi būti nuo 1 iki 9.")
            continue
        if board[move] != " ":
            print("Šis langelis jau užimtas!")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Žaidėjas {current_player} laimėjo!")
            break

        if is_draw():
            print_board()
            print("🤝 Lygiosios!")
            break

        # Keičiam žaidėją
        current_player = "O" if current_player == "X" else "X"

# 6. Pradedam žaidimą
play_game()
