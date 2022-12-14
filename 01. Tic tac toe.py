# Although the board could be created on only one line:
# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ,
# I decided to  make my life unnecessarily a bit more complex
def create_board():
    # Firstly, I am creating a tuple which will contain the numbers
    # of which the players will have to choose where to place their crosses or circles.
    # I chose tuple because this value will not be changed later in the function and therefore
    # will play the role of a constant. On top of that tuples are a bit faster than the lists.
    positions_list = (x for x in range(1, 10))
    # The board will be a multidimensional list which again could be created like that:
    # board = [[], [], []]
    # or with list comprehension:
    board = [[] for x in range(3)]

    # The two values below will play the role of support values in the first for-loop
    for_loop_counter = 0
    board_index = 0

    # For-loop which will insert the values from the positions_list to the board
    for num in positions_list:
        if for_loop_counter % 3 == 0 and for_loop_counter != 0:
            board_index += 1
        board[board_index].append(num)
        for_loop_counter += 1

    return board


def draw_board(board):
    # For-loop which will print the board accordingly
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()          # 1 2 3
                         # 4 5 6
                         # 7 8 9


def first_choice(first_player_name, second_player_name):
    # In order to make the game as fair as possible, the player who will choose
    # between Heads or Tails will also be randomly picked.
    import random
    names = [first_player_name, second_player_name]
    random.shuffle(names)
    return random.choice(names)


def heads_or_tails():
    # A simple function which recreates the famous game Heads or Tails
    import random
    lst = ["Heads", "Tails"]
    random.shuffle(lst)
    return random.choice(lst)


def starting_player(first_player_name, second_player_name, chosen_player, first_choice):
    # Based on the result of the previous function, starting_player() will return the player
    # first the player who won Heads or Tails, the result, and the player who lost
    dict_choice = {chosen_player: first_choice}
    for name in [first_player_name, second_player_name]:
        if name not in dict_choice:
            if "Tails" in dict_choice.values():
                dict_choice[name] = "Heads"
            else:
                dict_choice[name] = "Tails"

    h_t_result = heads_or_tails()
    if dict_choice[first_player_name] == h_t_result:
        return first_player_name, h_t_result, second_player_name
    else:
        return second_player_name, h_t_result, first_player_name

    # When the next three functions are called, they are going to check the current status of the board
    # whether there is a winning match or not
def check_diagonals(board, symbol):
    left_diagonal = []
    for i in range(len(board)):
        left_diagonal.append(board[i][i])
    right_diagonal = []
    for j in range(-1, -4, -1):
        right_diagonal.append(board[abs(j + 1)][j])
    if (symbol in left_diagonal and left_diagonal.count(symbol) == 3) or (symbol in right_diagonal and right_diagonal.count(symbol) == 3):
        return True
    else:
        return False


def check_rows(board, symbol):
    upper_row = board[0]
    middle_row = board[1]
    bottom_row = board[2]
    if (symbol in upper_row and upper_row.count(symbol) == 3) or (symbol in middle_row and middle_row.count(symbol) == 3) or (symbol in bottom_row and bottom_row.count(symbol) == 3):
        return True
    else:
        return False


def check_columns(board, symbol):
    left_column = []
    middle_column = []
    right_column = []
    for i in range(len(board)):
        left_column.append(board[i][0])
        middle_column.append(board[i][1])
        right_column.append(board[i][2])

    if (symbol in left_column and left_column.count(symbol) == 3) or (
            symbol in middle_column and middle_column.count(symbol) == 3) or (
            symbol in right_column and right_column.count(symbol) == 3):
        return True
    else:
        return False


def check_board_for_space(board):
    # In case no one has won the game and there are no free positions on the board
    # this function will stop the game
    is_space = False
    for i in range(len(board)):
        for j in board[i]:
            if type(j) == int:
                is_space = True
    return is_space



def surrender_check(position, player, first_name, second_name):
    # In case someone has foreseen his loss,
    # this function will help that someone surrender
    if position == "S":
        print(f"{player} has surrendered!")
        if player == first_name:
            print(f"Congratulations {second_name}! You are awesome!")
        else:
            print(f"Congratulations {first_name}! You are awesome!")
        return True

    return False


def position_input(player):
    # Looks after a correct position input
    is_valid = False
    position = ''
    while not is_valid:
        position = input(f"{player} choose your position: ")
        if position == "S":
            break
        try:
            position = int(position)
        except:
            print("Incorrect input")
            continue
        if position >= 1 and position <= 9:
            if available_positions[position] in taken_positions:
                print(f"{player}, this position is taken!")
                continue
            else:
                is_valid = True
        else:
            print(f"{player}, enter a number between 1 and 9.")
    return position


def fill_available_pos_dict():
    # I created this function because for the previous one I needed to check somewhere,
    # whether a certain position has already been chosen or not.
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            counter += 1
            available_positions[counter] = (i, j)


player_one = input("Please enter player's one name: ")
player_two = input("Please enter player's two name: ")
print(f"Welcome {player_one} and {player_two}. Now your names will be shuffled.")


chosen_player = first_choice(player_one, player_two)
first_player_to_choose = input(f"{chosen_player} has been chosen to pick Heads or Tails: ")

first_name, result, second_name = starting_player(player_one, player_two, chosen_player, first_player_to_choose)
print(f"The result of the coin toss is: {result}. Therefore the player who is going to make the first move is: {first_name}.")
players_info_dict = {first_name: {"symbol": "X"}, second_name: {"symbol": "X"}}
print(f"{first_name}'s symbol is 'X', so {second_name} yours will be 'O'")
print('-'*13 + "The game begins!" + 13*"-")
board = create_board()
draw_board(board)
available_positions = dict()
fill_available_pos_dict()

game_over = False
taken_positions = set()
while not game_over:
    for player in players_info_dict.keys():
        position = position_input(player)
        if surrender_check(position, player, first_name, second_name):
            game_over = True
            break
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == position:
                    board[i][j] = players_info_dict[player]["symbol"]
                    taken_positions.add((i, j))
        draw_board(board)

        if check_diagonals(board, players_info_dict[player]["symbol"]) \
                or check_rows(board, players_info_dict[player]["symbol"]) \
                or check_columns(board, players_info_dict[player]["symbol"]):
            game_over = True
            print(f"Congratulations {player}! You are awesome!")
            break
        if not check_board_for_space(board):
            game_over = True
            print("Draw!")
            break

