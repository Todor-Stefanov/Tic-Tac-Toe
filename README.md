
# Tic Tac Toe
This simple project could be done on less than 50 lines. But my main goal is to use as many of the basic python components as possiible:
- For/While loops
- Data Types
- Comprehensions
- Functios
- Namespaces


<p align="right">
  <img src="![cereal-tic-tac-toe](https://user-images.githubusercontent.com/112066009/189300790-dbf30d31-bf58-4dc5-8478-8b7c0560b5df.gif)" alt="Tic Tac Toe"/>
</p>


## Demo

https://user-images.githubusercontent.com/112066009/189302708-243a7cc4-516d-478a-bf91-bbe199297efe.mp4


## How to play my Tic Tac Toe

**At first, both players will be asked to write their names.  
```python
player_one = input("Please enter player's one name: ")
player_two = input("Please enter player's two name: ")
```

After that, they will be greeted and their names will be shuffled.
```python
def first_choice(first_player_name, second_player_name):
    # In order to make the game as fair as possible, the player who will choose
    # between Heads or Tails will also be randomly picked.
    import random
    names = [first_player_name, second_player_name]
    random.shuffle(names)
    return random.choice(names)

print(f"Welcome {player_one} and {player_two}. Now your names will be shuffled.")
chosen_player = first_choice(player_one, player_two)
```

The name which has been picked after the shuffle will be the one who will have to choose between Heads or Tails.
```python
first_player_to_choose = input(f"{chosen_player} has been chosen to pick Heads or Tails: ")
```  
Then the coin will be tossed and the winner will be the first to make his move. 
```python
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

first_name, result, second_name = starting_player(player_one, player_two, chosen_player, first_player_to_choose)
print(f"The result of the coin toss is: {result}. Therefore the player who is going to make the first move is: {first_name}.")
```
It is essential to know that the winner from the Head or Tails will always start with the cross sign "X".  
```python
players_info_dict = {first_name: {"symbol": "X"}, second_name: {"symbol": "O"}}
print(f"{first_name}'s symbol is 'X', so {second_name} yours will be 'O'")
```
To choose their move the players are expected to type a number from 1 to 9 inclusive. As you can see from the code below until a player enters a valid available position, the code will not move to the next. 
```python
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

    
```
### There are three outcomes: 
- One of the players wins  
```python
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

if check_diagonals(board, players_info_dict[player]["symbol"]) \
        or check_rows(board, players_info_dict[player]["symbol"]) \
        or check_columns(board, players_info_dict[player]["symbol"]):
    game_over = True
    print(f"Congratulations {player}! You are awesome!")
    break
```
- The game is a draw(My next goal is to make the game predict whether or not the game will end a draw)
```python
def check_board_for_space(board):
    # In case no one has won the game and there are no free positions on the board
    # this function will stop the game
    is_space = False
    for i in range(len(board)):
        for j in board[i]:
            if type(j) == int:
                is_space = True
    return is_space

if not check_board_for_space(board):
    game_over = True
    print("Draw!")
    break

```
- A player surrenders 
```python
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

if surrender_check(position, player, first_name, second_name):
    game_over = True
    break
```
![giphy](https://user-images.githubusercontent.com/112066009/189303513-63ee66af-8bd7-472a-9cee-42733fc57d34.gif)

## Get better at Tic Tac Toe

https://www.wikihow.com/Win-at-Tic-Tac-Toe
