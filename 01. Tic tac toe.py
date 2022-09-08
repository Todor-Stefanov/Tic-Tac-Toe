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
            print(str(board[i][j]), end=" ")
        print()          # 1 2 3
                         # 4 5 6
                         # 7 8 9


def first_choice(first_player_name, second_player_name):
    import random
    names = [first_player_name, second_player_name]
    random.shuffle(names)
    return random.choice(names)


def heads_or_tails():
    import random
    lst = ["Heads", "Tails"]
    random.shuffle(lst)
    return random.choice(lst)


def starting_player(first_player_name, second_player_name, chosen_player, first_choice):
    dict_choice = {chosen_player: first_choice}
    for name in [first_player_name, second_player_name]:
        if name not in dict_choice:
            if "Tails" in dict_choice.values():
                dict_choice[second_player_name] = "Heads"
            else:
                dict_choice[second_player_name] = "Tails"

    result = heads_or_tails()
    if dict_choice[first_player_name] == result:
        return first_player_name, result, second_player_name
    else:
        return second_player_name, result, first_player_name


player_one = input("Please enter player's one name: ")
player_two = input("Please enter player's two name: ")
print(f"Welcome {player_one} and {player_two}. Now your names will be shuffled.")


chosen_player = first_choice(player_one, player_two)
first_player_to_choose = input(f"{chosen_player} has been chosen to pick Heads or Tails: ")
first_name, result, second_name = starting_player(player_one, player_two, chosen_player, first_player_to_choose)
print(f"The result of the coin toss is: {result}. Therefore the player who is going to make the first move is: {name}.")

board = create_board()
draw_board(board)

