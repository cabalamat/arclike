# List of solutions

Some previous solutions to the ARC challenge

[[ARC-solution]] by Johan Sokrates Wind was the winning solution to the 2020 ARC Challenge.

[[Dreamcoder]] is a system for neurally guided discrete program search that starts with a small DSL with some basic functions and gradually expands it by finding useful combinations of these functions and adding them to the library.

**Sebastien Ferre**'s approach described in a paper <https://arxiv.org/abs/2311.00545>, [pdf here](https://arxiv.org/pdf/2311.00545) 

## Program Synthesis Starter Notebook

[Program Synthesis Starter Notebook](https://www.kaggle.com/code/michaelhodel/program-synthesis-starter-notebook/notebook) shows a really primitive soloution in which there are 5 grid-transformation functions (called *primitives*). These are:

* `compress` = removes top/bottom rows and leftmost/rightmost columns that're all black (0) until can't do it any more (I think)
* `hmirror` = flip over on horizontal axis
* `tophalf` = return top half of grid
* `rot90` = rotate clockwise 90 degrees
* `trim` = removes top/bottom rows and leftmost/rightmost columns, regardless of what's in them

Note that none of these functions takes any parameters. Notre that the purpose of my patrec module is to produce functions *with* parameters.