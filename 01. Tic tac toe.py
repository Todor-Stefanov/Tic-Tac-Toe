# Although the board could be created on only one line:
# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ,
# I decided to  make my life unnecessarily a bit more complex
def draw_board():
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

    # For-loop which will print the board accordingly
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()         # 1 2 3
                        # 4 5 6
                        # 7 8 9

draw_board()
