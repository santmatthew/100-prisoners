100 Prisoners Riddle Simulator
====

Monte Carlo simulation of the [100 Prisoners Riddle](https://en.wikipedia.org/wiki/100_prisoners_problem) that shows 
the success rate for different strategies.

*Requires: Python 3.10.x or above*

## How to run

Just run `python3 main.py random` to try a random stratefy or `python3 main.py loop` to try the loop strategy.

## Command line options

The program accepts the following parameters in the following order:

```
strategy: can be 'loop' or 'random'.

number of attempts: how many times the simulation should run. Default 1000.

number of prisoners: number of prisoners looking for their number. Default 100.

number of boxes opened: how many boxes each prisoner is allowed to open in order to find their number. Default 50.

verbose: if set to true, additional information is shown in the output. Default False.
```

## Adding more strategies

To try your own custom strategy you need to 

1. Add a function to `strategies.py` with the following signature:
```
(given_prisoner_number: int, boxes: list[int], n_boxes_selected: int) -> Tuple[int, bool]

    given_prisoner_number : int
        The number of the prisoner attempting to find his number.
    boxes : list[int]
        A list with the values [0, n_prisoners) shuffled.
    n_boxes_selected : int
        The number of boxes a prisoner can open in order to find their number.

    returns : Tuple[int, bool]
        The number of boxes opened, success/failure
```
2. Add a suitable key and the function reference to the `strategies` dictionary at the end of the file.

You can then call the strategy from the main program as the 1st argument.