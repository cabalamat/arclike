# solver.py

Documents the `solver.py` module of [[Arclike]], which puts together gridfuns to solve a task.

## class Solver

The `Solver` class will attempt to solve a task:

```py
tk = Task()
tk.loadFromFile("something.json")
solv = Solver(tk)
solv.expand() # expands 1 level from here
```

And then once you have expanded the Nodes, you can look at them with: 

```py
nodes: list[Node] = solv.nodes()
```

## class Node

From a node, you can look at it's loss on the training set:

```py
aNode = solv.nodes()[0]
lo: int = aNode.loss() # return loss, an integer
```

You can get its parent, which implies a Solver is a Node. (It's the root of a tree of nodes).

```py
parent: Node = aNode.parent()
```

As with a `Solver` you can `expand()` it to form all the nodes below it

## Unsolved issues

When we a looking at a task, do we expand the nodes on just one training pair at a time, or on all of them?