from typing import List, Optional
from searches import Node, astar, node_to_path

MAX_NUM = 4


def main():
    start: MCState = MCState(MAX_NUM, MAX_NUM, True)
    solution: Optional[Node[MCState]] = astar(
        start, goal_test, MCState.sucessors, get_manhattan_distance
    )
    if solution is None:
        print("No solution found")
    else:
        path: List[MCState] = node_to_path(solution)
        display_solution(path)


class MCState:
    def __init__(
        self, missionaries: int = 3, cannibals: int = 3, boat: bool = True
    ) -> None:
        self.wm = missionaries
        self.wc = cannibals
        self.em = MAX_NUM - self.wm
        self.ec = MAX_NUM - self.wc
        self.boat = boat

    def __str__(self) -> str:
        return (
            "On the west bank there are {} missionaries and {} cannibals.\n"
            "On the east bank there are {} missionaries and {} cannibals.\n"
            "The boat is on the {} bank.".format(
                self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east")
            )
        )

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def sucessors(this):
        sucessors: List[MCState] = []
        if this.boat:
            if this.wm > 1:
                sucessors.append(MCState(this.wm - 2, this.wc, not this.boat))
            if this.wm > 0:
                sucessors.append(MCState(this.wm - 1, this.wc, not this.boat))
            if this.wc > 1:
                sucessors.append(MCState(this.wm, this.wc - 2, not this.boat))
            if this.wc > 0:
                sucessors.append(MCState(this.wm, this.wc - 1, not this.boat))
            if this.wc > 0 and this.wm > 0:
                sucessors.append(MCState(this.wm - 1, this.wc - 1, not this.boat))
        else:
            if this.em > 1:
                sucessors.append(MCState(this.wm + 2, this.wc, not this.boat))
            if this.em > 0:
                sucessors.append(MCState(this.wm + 1, this.wc, not this.boat))
            if this.ec > 1:
                sucessors.append(MCState(this.wm, this.wc + 2, not this.boat))
            if this.ec > 0:
                sucessors.append(MCState(this.wm, this.wc + 1, not this.boat))
            if this.ec > 0 and this.em > 0:
                sucessors.append(MCState(this.wm + 1, this.wc + 1, not this.boat))

        return [x for x in sucessors if x.is_legal]


def goal_test(state: MCState) -> bool:
    return state.wm == 0 and state.wc == 0 and state.is_legal


def display_solution(path: List[MCState]):
    if len(path) == 0:
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(
                "{} missionaries and {} cannibals moved from the east bank to the west bank.\n".format(
                    old_state.em - current_state.em, old_state.ec - current_state.ec
                )
            )
        else:
            print(
                "{} missionaries and {} cannibals moved from the west bank to the east bank.\n".format(
                    old_state.wm - current_state.wm, old_state.wc - current_state.wc
                )
            )
        print(current_state)
        old_state = current_state


if __name__ == "__main__":
    main()
