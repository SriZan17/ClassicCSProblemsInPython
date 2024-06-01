from typing import List, Optional
from searches import bfs, node_to_path, astar


def main():
    seq: List[str] = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
    start: Puzzle_state = Puzzle_state(seq)
    solution: Optional[Puzzle_state] = astar(
        start, goal_test, Puzzle_state.get_sucessors, get_manhattan_distance
    )
    if solution is None:
        print("No solution found")
    else:
        path: List[Puzzle_state] = node_to_path(solution)
        for p in path:
            print(p)


class Puzzle_state:

    def __init__(self, sequence: List[str]) -> None:
        self.sequence = sequence

    def __str__(self) -> str:
        sequence = self.sequence
        a = ""
        for i in range(len(sequence)):
            a = a + sequence[i] + "\t"
            if (i + 1) % 3 == 0:
                a = a + "\n"
        return a

    def get_sucessors(self) -> List:
        sucssores: List[Puzzle_state] = []
        sequence = self.sequence
        i = sequence.index(" ")

        moves = [-1, 1, -3, 3]

        for m in moves:
            if 0 <= i + m < 9:
                if i % 3 == 0 and m == -1:
                    continue
                if i % 3 == 2 and m == 1:
                    continue
                new_sequence = swap_indexes(sequence, i, i + m)
                sucssores.append(Puzzle_state(new_sequence))

        return sucssores


def get_manhattan_distance(state: Puzzle_state) -> int:
    distance = 0
    for tile in range(1, 9):
        current_index = state.sequence.index(str(tile))
        target_index = tile - 1
        dx = abs(current_index % 3 - target_index % 3)
        dy = abs(current_index // 3 - target_index // 3)
        distance = distance + dx + dy
    return distance


def goal_test(state: Puzzle_state) -> bool:
    return state.sequence == ["1", "2", "3", "4", "5", "6", "7", "8", " "]


def swap_indexes(lst: List[str], index1: int, index2: int) -> List[str]:
    new_lst = lst.copy()
    new_lst[index1], new_lst[index2] = new_lst[index2], new_lst[index1]
    return new_lst


if __name__ == "__main__":
    main()
