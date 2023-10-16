import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Initialize the tableau
tableau = [[] for _ in range(7)]

# Initialize the foundation
foundation = {suit: [] for suit in suits}

# Initialize the stock and waste
stock = deck
waste = []

# Initialize the tableau with color IDs and revealed tags
for i in range(7):
    for j in range(i, 7):
        revealed = j == i  # Set to True for the first card, False for the rest
        card = stock.pop(0)
        color = 'Red' if card[1] in ['Hearts', 'Diamonds'] else 'Black'
        tableau[j].append((card + (color,), revealed))

# Function to display the current state of the game
def display_game():
    print("Stock:", len(stock), "cards")
    print("Waste:", waste[-1] if waste else "Empty")
    print("Foundation:")
    for suit in suits:
        print(suit + ":", foundation[suit])

    print("Tableau:")
    for i, pile in enumerate(tableau):
        if pile:
            print(f"{i + 1}:", end=" ")
            for j, (card, revealed) in enumerate(pile):
                if revealed:
                    print(card, end=" ")
                else:
                    print("*", end=" ")
            print()
        else:
            print(f"{i + 1}: *")

# Function to check if the move is valid
def is_valid_move(card, target_pile):
    if not tableau[target_pile]:
        return True
    last_card, _ = tableau[target_pile][-1]
    if ranks.index(last_card[0]) - 1 == ranks.index(card[0]) and last_card[2] != card[2]:
        if (last_card[2] == 'Red' and card[2] == 'Black') or (last_card[2] == 'Black' and card[2] == 'Red'):
            return True
        else:
            return False
    return False

# Function to move a card from one pile to another
def move_card(source_pile, target_pile):
    card, _ = tableau[source_pile].pop()
    tableau[target_pile].append((card, True))
    if tableau[source_pile]:
        next_card, revealed = tableau[source_pile][-1]
        if not revealed:
            tableau[source_pile][-1] = (next_card, True)

# Function to move a card to the foundation
def move_to_foundation(card):
    suit = card[1]
    rank = card[0]
    if foundation[suit]:
        last_rank = foundation[suit][-1][0]
        if ranks.index(rank) == ranks.index(last_rank) + 1:
            foundation[suit].append(card)
        else:
            print("Invalid move, try again.")
    elif rank == 'Ace':
        foundation[suit].append(card)
    else:
        print("Invalid move, try again.")

# Game loop
while True:
    display_game()
    user_input = input("Enter source pile number (1-7), 'w' for waste, or 0 for stock, q to quit: ")

    if user_input.isdigit():
        source_pile = int(user_input)
        if source_pile <= 7:
            if source_pile == 0:
                if stock:
                    card = stock.pop(0)
                    waste.append(card)
                else:
                    stock = waste[::-1]
                    waste = []
            else:
                source_pile -= 1
                if not tableau[source_pile]:
                    print("Invalid choice, try again.")
                    continue
                target_pile = input("Enter target pile number (1-7) or 'f' to move to foundation: ")
                if target_pile == 'f':
                    card, _ = tableau[source_pile][-1]
                    move_to_foundation(card)
                    if tableau[source_pile]:
                        tableau[source_pile].pop()
                    continue
                else:
                    target_pile = int(target_pile) - 1
                    if target_pile == -1:
                        if waste:
                            card, _ = waste.pop()
                            tableau[source_pile].append((card, True))
                        else:
                            print("Invalid choice, try again.")
                            continue
                    else:
                        if is_valid_move(tableau[source_pile][-1][0], target_pile):
                            move_card(source_pile, target_pile)
                        else:
                            print("Invalid move, try again.")
                            continue
        else:
            print("invalid input")
            continue

    elif user_input.lower() == 'w':
        if waste:
            print("Current waste card:", waste[-1])
            target_pile = input("Enter target pile number (1-7) or 'f' to move to foundation: ")
            if target_pile == 'f':
                card = waste[-1]
                move_to_foundation(card)
                waste.pop()
            else:
                target_pile = int(target_pile) - 1
                if waste:
                    waste_card = waste[-1] + (waste[-1][1],)  # Include the color information
                    if is_valid_move(waste_card, target_pile):
                        tableau[target_pile].append((waste.pop() + (waste_card[2],), True))  # Include the color information
                    else:
                        print("Invalid move, try again.")
                else:
                    print("Invalid move, try again.")
        
    elif user_input.lower() == 'q':
        print("goodbye")
        break
        
    for pile in tableau:
        if pile and not pile[-1][1]:  # Check if the top card is hidden
            pile[-1] = (pile[-1][0], True)
    if waste and len(waste[-1]) == 2:
        waste[-1] = waste[-1] + ('Red' if waste[-1][1] in ['Hearts', 'Diamonds'] else 'Black',)  # Include the color information

    # Check for win condition
    if all(len(foundation[suit]) == 13 for suit in suits):
        print("You win!")
        break
