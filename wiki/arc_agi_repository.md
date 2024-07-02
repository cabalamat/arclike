# ARC-AGI repository

The [ARC-AGI repository](https://github.com/fchollet/ARC-AGI) contains some sample problems for the ARC, 
and a web-based viewer that lets you.

## Sample problems

There are some simpler problems stored under `data/training` and some harder problems stored under `data/evaluation`.
The idea is you train your AI program using the simpler problems and then run it on the evaluation problems. There is
also a secret series of evaluation problems used for the ARC Prize itself; these have to be secret otherwise
as very simple program could overfit to those problems.

Each problem is a JSON file, for example, `data/training/0520fde7.json` is (when pretty-printed):

```json
{"train": [
    {"input":  [[1, 0, 0, 5, 0, 1, 0], 
                [0, 1, 0, 5, 1, 1, 1], 
                [1, 0, 0, 5, 0, 0, 0]], 
     "output": [[0, 0, 0], 
                [0, 2, 0], 
                [0, 0, 0]]}, 
    {"input":  [[1, 1, 0, 5, 0, 1, 0], 
                [0, 0, 1, 5, 1, 1, 1], 
                [1, 1, 0, 5, 0, 1, 0]], 
     "output": [[0, 2, 0], [0, 0, 2], [0, 2, 0] ]}, 
    {"input":  [[0, 0, 1, 5, 0, 0, 0], 
                [1, 1, 0, 5, 1, 0, 1], 
                [0, 1, 1, 5, 1, 0, 1]], 
     "output": [[0, 0, 0], 
                [2, 0, 0],  
                [0, 0, 2]]}], 
 "test": [
    {"input":  [[1, 0, 1, 5, 1, 0, 1], 
                [0, 1, 0, 5, 1, 0, 1], 
                [1, 0, 1, 5, 0, 1, 0]], 
     "output": [[2, 0, 2], 
                [0, 0, 0], 
                [0, 0, 0]]}]}
```

On the web-based testing interface, this looks like:

![](arc_testing_interface.png)

## Web-based viewer

This is stored in `apps/testing_interface.html`. 
