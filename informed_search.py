from queue import LifoQueue, PriorityQueue, Queue
from typing import List, Dict, Optional

from search_problem import State
from heuristic_search_problem import HeuristicSearchProblem
from tile_game import HeuristicTileGame, TileGame
from heuristics import admissible_heuristic, inadmissible_heuristic


def astar(problem: HeuristicSearchProblem) -> tuple[Optional[List[State]], Dict[str, any]]:
    """
    A* search.

    Args:
        problem - the problem on which the search is conducted, a HeuristicSearchProblem
        heuristic - the heuristic function to use

    Output: a list of states representing the path of the solution
            and a dictionary with stats about the search
    """
    stats = {
                "path_length": 0,
                "states_expanded": 0,
                "total_cost": 0, # TODO: I don't know what total_cost is supposed to be
                "max_frontier_size": 0
            }
    open_set = PriorityQueue()
    start_state = problem.get_start_state()
    open_set.put((problem.heuristic(start_state), [start_state]))
    has_been_added = [start_state]
    counter = 0
    while not open_set.empty():
        counter = counter + 1
        if counter % 500 == 0:
            print("states expanded ", counter, stats["states_expanded"])
        _ , cur_path = open_set.get()
        if problem.is_goal_state(cur_path[-1]): #if the end of the current path is the goal
            stats["path_length"] = len(cur_path)
            stats["total_cost"] = len(cur_path) - 1
            return cur_path, stats
        successors = problem.get_successors(cur_path[-1])
        for successor in successors:
            if successor not in has_been_added:
                new_path = cur_path + [successor]
                priority = problem.heuristic(successor) + len(new_path)
                # priority = problem.heuristic(successor)
                open_set.put((priority, new_path))
                has_been_added.append(successor)
        stats["states_expanded"] = stats["states_expanded"] + 1
        stats["max_frontier_size"] = max(stats["max_frontier_size"], open_set.qsize())
    return None, stats


def main():
    dim = 3
    tg = TileGame(dim)

    admissible_tile_game = HeuristicTileGame(
        dim, start_state=tg.get_start_state(), heuristic=admissible_heuristic)
    path_admissible, stats_admissible = astar(admissible_tile_game)
    print("path (admissible):")
    tg.print_pretty_path(path_admissible)
    print("stats (admissible):", stats_admissible)
    print('-'*110)

    inadmissible_tile_game = HeuristicTileGame(
        dim, start_state=tg.get_start_state(), heuristic=inadmissible_heuristic)
    path_inadmissible, stats_inadmissible = astar(inadmissible_tile_game)
    print("path (inadmissible):")
    tg.print_pretty_path(path_inadmissible)
    print("stats (inadmissible):", stats_inadmissible)
    print('-'*110)



if __name__ == "__main__":
    main()