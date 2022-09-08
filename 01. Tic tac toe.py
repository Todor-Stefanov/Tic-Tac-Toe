def draw_board():
    positions_list = (x for x in range(1, 10))
    board = [[], [], []]

    for_loop_counter = 0
    board_index = 0

    for i in positions_list:
        if for_loop_counter % 3 == 0 and for_loop_counter != 0:
            board_index += 1
        board[board_index].append(i)
        for_loop_counter += 1


    print(board)

draw_board()
