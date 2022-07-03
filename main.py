"""Main module for running riddle simulation."""

import sys

from typing import Callable, Tuple

from prisoners_riddle import PrisonersRiddle
from strategies import strategies


def simulate(n_prisoners: int, n_boxes_selected: int,
             strategy: Callable[[list[int], int], Tuple[int, bool]],
             n_attempts: int, verbose: bool) -> float:
    """Runs a simulation of the riddle n times for a given setup using a given strategy."""

    success_count = 0
    for i in range(0, n_attempts):
        riddle = PrisonersRiddle(n_prisoners, n_boxes_selected)
        success = riddle.attempt_solution(strategy)
        if verbose:
            print(f"Attempt {i + 1}:")
            print(riddle.get_setup_info())
        if success:
            success_count = success_count + 1
    return success_count / n_attempts


if __name__ == '__main__':
    DEFAULT_N_ATTEMPTS = 1000
    DEFAULT_N_PRISONERS = 100
    DEFAULT_N_BOXES_SELECTED = 50
    DEFAULT_VERBOSITY = False

    args = sys.argv[1:]
    if len(args) < 1:
        print(f"Usage: {sys.argv[0]} strategy [n_attempts (default {DEFAULT_N_ATTEMPTS})] " + \
              f"[n_prisoners (default {DEFAULT_N_PRISONERS})] [n_boxes_selected (default " + \
              f"{DEFAULT_N_BOXES_SELECTED})] [verbose (default False)]")
        print(f"Where strategy can be one of {list(strategies.keys())}")
        sys.exit(1)
    strategy_key = args[0].strip().lower()
    if strategy_key not in strategies:
        print(
            f"Strategy '{strategy_key}' not found. Please use one of {list(strategies.keys())}")
        sys.exit(2)

    STRATEGY = strategies[strategy_key]
    N_ATTEMPTS = int(args[1]) if len(args) > 1 else DEFAULT_N_ATTEMPTS
    if N_ATTEMPTS < 1:
        print("n_attempts needs to be greater than 0")
        sys.exit(2)
    N_PRISONERS = int(args[2]) if len(args) > 2 else DEFAULT_N_PRISONERS
    if N_PRISONERS < 1:
        print("n_prisoners needs to be greater than 0")
        sys.exit(2)
    N_BOXES_SELECTED = int(args[3]) if len(
        args) > 3 else DEFAULT_N_BOXES_SELECTED
    if N_BOXES_SELECTED < 1:
        print("n_boxes_selected needs to be greater than 0")
        sys.exit(2)
    VERBOSE = bool(args[4]) if len(args) > 4 else DEFAULT_VERBOSITY

    print(f"Attempting solution {N_ATTEMPTS} times...")
    SUCCESS_RATE = simulate(
        N_PRISONERS, N_BOXES_SELECTED, STRATEGY, N_ATTEMPTS, VERBOSE)

    print(
        f"Success rate using {strategy_key} strategy for {N_PRISONERS} prisoners selecting " + \
        f"{N_BOXES_SELECTED} boxes: {SUCCESS_RATE}")
