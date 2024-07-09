# Arclike

Some notes on my program **Arclike**, Which is available on <i class='fab fa-github'></i> Github at <https://github.com/cabalamat/arclike>.

## Program Structure

## Road Map

Arclike will be developed in this order:

`Grid` class to hold a 2-dimensional grid of coloured squares. Some functions for prettyprinting grids and transfomations between
them on the console, e.g.:

![](gridxyansi.png)

Some grid functions (functions which act on Grids) in `gridfun.py`.

A `Problem` class that holds a problem, i.e. a set of inputs and their corresponding outputs, plus one or more inputs without outputs (called *questions*), where 
the task is to find the output for those inputs.

Reading problems from the JSON files in the [ARC-AGI repository](arc_agi_repository).

Then we can get to the important task of solving the ARC-AGI problem!

The simple solution will be to have various grid functions, and pattern recognisers that can suggest solutions, e.g. a grid function with some parameters
to determine how it works. The candidate solutions can them be compared to the actual result and perform the same task on the ones with the lowest *loss*,
until you get a candidate solution with zero loss, which is then applied to the question, forming the answer.

More intelligent ways of doing the above.

Ways of doing the above so the AI learns, i.e. if it has done a task and subsequently gets a similar task, it recognises it is similar, and can solve it more quickly. 

 
