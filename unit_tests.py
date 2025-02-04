import unittest

# from directed_graph import DirectedGraph
# from bfs_and_dfs import bfs, dfs
from tile_game import TileGame, TileGameState, HeuristicTileGame
from informed_search import astar
from blind_search import iterative_deepening_search
from heuristics import admissible_heuristic, inadmissible_heuristic


class IOTest(unittest.TestCase):
    """
    Tests IO for search implementations. Contains basic/trivial test cases.

    Each test function instantiates a search problem (TileGame) and tests if the three test case
    contains the solution, the start state is in the solution, the end state is in the
    solution and, if applicable, if the length of the solutions are the same.

    These tests are not exhaustive and do not check if your implementation follows the
    algorithm correctly. We encourage you to create your own tests as necessary.
    """

    def _check_tilegame(self, start_state, goal_state, length=None, heuristic=None):
        """
        Test algorithm on a TileGame
        algorithm: algorithm to test
        start_state: start state of the TileGame
        goal_state: goal state of the TileGame
        length: length that the path returned from algorithm should be. 
                Think about why this argument is optional, and when you should provide it.
        heuristic: heuristic to use for the TileGame (admissible or inadmissible)
        """

        def path_is_valid(cur_path):
            """"checks that the cur_path only takes valid moves
            Parameters: 
            current path (List<State>) takes in a path or states
            Returns:
            Boolean: returns true if the path is valid, false otherwise
            """
            while len(cur_path) > 1:
                cur_position = cur_path.pop(0)
                succsessors = game.get_successors(cur_position)
                if cur_path[0] not in succsessors:
                    return False
            return True

        # Ensure start_state and goal_state dimensions are n x n
        self.assertEqual(len(start_state.board), len(start_state.board[0]), "Dimensions must be n x n")
        dim = len(start_state.board)
        
        # Initialize the TileGame with the provided start and goal states, and the given heuristic
        game = HeuristicTileGame(dim, start_state=start_state, goal_state=goal_state, heuristic=heuristic)
        
        # Run the algorithm (e.g., A* or any other search algorithm) on the game
        path, stats = astar(game)
        
        # Check that the path starts and ends with the correct states
        self.assertEqual(path[0], start_state, "Path should start with the start state")
        self.assertEqual(path[-1], goal_state, "Path should end with the goal state")
        # If a path length is provided, verify the length matches the expected value
        if length:
            self.assertEqual(len(path), length, f"Path length should be {length}")
        
        #checks that each step in the path is one move from the previous step
        self.assertTrue(path_is_valid(path),
                        "Path should only take valid moves")

        #checks that there are no repeated states in the path
        self.assertEqual(len(path), len(set(path)),
                         "Path should not contain duplicate elements")
        
    def test_astar(self):
        start_state = TileGameState(((4, 1, 3), (7, 2, 6), (9, 5, 8)))
        goal_state = TileGameState(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self._check_tilegame(start_state, goal_state, length=7, heuristic=admissible_heuristic)
        self._check_tilegame(start_state, goal_state, heuristic=inadmissible_heuristic)

        #checks that astar works when the start state is the goal state
        self._check_tilegame(goal_state, goal_state, length=1, heuristic=admissible_heuristic)
        self._check_tilegame(goal_state, goal_state, length=1, heuristic=inadmissible_heuristic)

        #checks that astar works on a 1-by-1 board
        one_by_one_board = TileGameState(((1,),))
        self._check_tilegame(one_by_one_board, one_by_one_board, length=1, heuristic=admissible_heuristic)
        self._check_tilegame(one_by_one_board, one_by_one_board, length=1, heuristic=inadmissible_heuristic)

        #checks that astar finds the shortest path when only one swap is needed
        one_swap_board_start = TileGameState(((3, 2), (1, 4)))
        one_swap_board_goal = TileGameState(((1, 2), (3, 4)))
        self._check_tilegame(one_swap_board_start, one_swap_board_goal, length=2, heuristic=admissible_heuristic)
        self._check_tilegame(one_swap_board_start, one_swap_board_goal, length=2, heuristic=inadmissible_heuristic)

        #checks that the admissible_heuristic finds the shortest path when 
        # some swaps moves 2 tiles in the right direction
        two_swap_start_state = TileGameState(((5, 1, 3), (4, 2, 6), (7, 8, 9)))
        two_swap_goal_state = TileGameState(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self._check_tilegame(two_swap_start_state, two_swap_goal_state, length=3, heuristic=admissible_heuristic)
        self._check_tilegame(two_swap_start_state, two_swap_goal_state, heuristic=inadmissible_heuristic)

        #checks on a 2-by-2 board that admissible_heuristic finds a path of the right length
        four_swap_start_state = TileGameState(((4, 2), (3, 1)))
        four_swap_goal_state = TileGameState(((1, 2), (3, 4)))
        self._check_tilegame(four_swap_start_state, four_swap_goal_state, length=4, heuristic=admissible_heuristic)
        self._check_tilegame(four_swap_start_state, four_swap_goal_state, heuristic=inadmissible_heuristic)

        five_swap_start_state = TileGameState(((4, 3), (2, 1)))
        five_swap_goal_state = TileGameState(((1, 2), (3, 4)))
        self._check_tilegame(five_swap_start_state, five_swap_goal_state, length=5, heuristic=admissible_heuristic)
        self._check_tilegame(five_swap_start_state, five_swap_goal_state, heuristic=inadmissible_heuristic)

#FIXME: add stats testing

if __name__ == "__main__":
    unittest.main()
