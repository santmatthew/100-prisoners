"""
Module containing strategy functions and a dictionary of the strategies.

All strategies should have the same signature:
    given_prisoner_number : int
        The number of the prisoner attempting to find his number.
    boxes : list[int]
        A list with the values [0, n_prisoners) shuffled.
    n_boxes_selected : int
        The number of boxes a prisoner can open in order to find their number.

    returns : Tuple[int, bool]
        The number of boxes opened, success/failure
"""

from random import shuffle
from typing import Callable, Tuple


def random(given_prisoner_number: int, boxes: list[int], n_boxes_selected: int) -> Tuple[int, bool]:
    """Naive strategy where the prisoners just choose n boxes randomly."""

    found = False
    permutation = list(range(0, len(boxes)))
    shuffle(permutation)
    permutation = permutation[0:n_boxes_selected]
    boxes_opened = 0
    for box_number in permutation:
        if boxes[box_number] == given_prisoner_number:
            found = True
            break
        boxes_opened = boxes_opened + 1
    return (boxes_opened, found)


def loop(given_prisoner_number: int, boxes: list[int], n_boxes_selected: int) -> Tuple[int, bool]:
    """
    Strategy that puts prisoner on a random loop:
        1. Select box whose label is the prisoner's number
        2. Select box whose label is the number contained in the last box.
        3. Repeat step 2 until the prisoner's number is found (loop closed) or attempts run out.
    """

    found = False
    boxes_opened = 0
    next_box = given_prisoner_number
    while not found and boxes_opened < n_boxes_selected:
        if boxes[next_box] == given_prisoner_number:
            found = True
        else:
            next_box = boxes[next_box]
        boxes_opened = boxes_opened + 1
    return (boxes_opened, found)


strategies: dict[str, Callable[[int, list[int], int], bool]] = {
    'random': random,
    'loop': loop
}
