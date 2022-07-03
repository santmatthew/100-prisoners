"""This module contains the PrisonersRiddle class"""

from random import shuffle
from typing import Callable, Tuple


class PrisonersRiddle:
    """
    Class representing the 100 Prisoners Riddle (number of prisoners can be specified).

    Attributes
    ----------
    n_prisoners : int
        Number of prisoners
    n_boxes_selected : int
        Number of boxes that a prisoner is allowed to open
    """

    def __init__(self, n_prisoners: int, n_boxes_selected: int) -> None:
        self.n_prisoners = n_prisoners
        self.n_boxes_selected = n_boxes_selected
        self.box_contents = list(range(0, self.n_prisoners))
        shuffle(self.box_contents)

    def attempt_solution(self, strategy: Callable[[int, list[int], int], Tuple[int, bool]]) -> bool:
        """Attempts to solve the riddle using a given strategy."""

        strategy_success = True
        for i in range(0, self.n_prisoners):
            _, prisoner_success = strategy(
                i, self.box_contents, self.n_boxes_selected)
            strategy_success = strategy_success and prisoner_success
            if strategy_success is False:
                break
        return strategy_success

    def get_setup_info(self):
        """Gives details on the riddle setup"""

        return f"Number of prisoners: {self.n_prisoners}\n" + \
               f"Number of boxes selected: {self.n_boxes_selected}\n" + \
               f"Box contents: {self.box_contents}"
