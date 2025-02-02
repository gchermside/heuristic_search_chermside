from tile_game import TileGameState



def admissible_heuristic(state: TileGameState) -> float:
    """
    Produces a number for the given tile game state representing
    an estimate of the cost to get to the goal state. Remember that this heuristic must be
    admissible, that is it should never overestimate the cost to reach the goal.
    This heuristic is the combined manhattan distance for each tile to its goal location
    divided by 2.

    Args:
        state - the tilegame state to evaluate. Consult handout for how the tilegame state is represented

    Returns: a float.
    """
    dimension = len(state.board)
    total_distance = 0
    for i in range(dimension):
        for j in range(dimension):
            num = state.board[i][j]
            row = (num-1) // dimension
            col = (num-1) % dimension
            total_distance += abs(row-i) + abs(col-j)
    return total_distance / 2


def inadmissible_heuristic(state: TileGameState) -> float:
    """
    Produces a number for the given tile game state representing
    an estimate of the cost to get to the goal state. This heuristic
    is inadmissible, meaning it can, at times, overestimate the cost-to-goal.
    This inadmissible heuristic uses the sum of all manhattan distances for 
    each tile to their goal location.

    Args:
        state - the tilegame state to evaluate. Consult handout for how the tilegame state is represented

    Returns: a float.
    """
    dimension = len(state.board)
    total_distance = 0
    for i in range(dimension):
        for j in range(dimension):
            num = state.board[i][j]
            row = (num-1) // dimension
            col = (num-1) % dimension
            total_distance += abs(row-i) + abs(col-j)
    return total_distance


def my_heuristic(state: TileGameState) -> float:
    """
    Your implementation of an inadmissible heuristic.
    Args:
        state - the tilegame state to evaluate. Consult handout for how the tilegame state is represented

    Returns: a float (the heuristic value of state).
    """
    heuristic_value = 0
    dimension = len(state.board)
    for i in range(dimension):
        for j in range(dimension):
            num = state.board[i][j]
            row = (num-1) // dimension
            col = (num-1) % dimension
            num = state.board[i][j]
            cur_location_goal = (i * dimension) + j
            if not num == cur_location_goal: #if the number is not where it belongs
                heuristic_value += (abs(row-i) ** 2 + abs(col-j) ** 2) ** 0.5
                # # try to swap it each way, and see how that changes
                # if i > 0: #if we are not is the top row, swap up and see what happens
                #     num_goal_up = (i - 1) * dimension + j
                #     if num == num_goal_up:
                #         other_num_up = state.board[i - 1][j]
                #         if other_num_up == cur_location_goal:
                #             heuristic_value += 0.5
                #             continue

                # if i < dimension - 1: #if we are not is the bottom row, swap down and see what happens
                #     num_goal_down = (i + 1) * dimension + j
                #     if num == num_goal_down:
                #         other_num_down = state.board[i + 1][j]
                #         if other_num_down == cur_location_goal:
                #             heuristic_value += 0.5
                #             continue

                # if j > 0: #if we are not is the left-most row, swap left and see what happens
                #     num_goal_left = (i * dimension) + (j - 1)
                #     if num == num_goal_left:
                #         other_num_left = state.board[i][j - 1]
                #         if other_num_left == cur_location_goal:
                #             heuristic_value += 0.5
                #             continue

                # if j < dimension - 1: #if we are not is the right-most row, swap right and see what happens
                #     num_goal_right = (i * dimension) + (j + 1)
                #     if num == num_goal_right:
                #         other_num_right = state.board[i][j + 1]
                #         if other_num_right == cur_location_goal:
                #             heuristic_value += 0.5
                #             continue
                # heuristic_value += abs(row-i) + abs(col-j)
    # print("heuristic ", heuristic_value, state)
    return heuristic_value
