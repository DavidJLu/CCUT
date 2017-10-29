#CS250 at CCUT Week 3: Relations

#### Representing binary relations
We can represent a binary relation graphically as follows:

if $a R b$ then draw and arrow from $a$ to $b$ to form the following graph.

$a \rightarrow b$

> Example:
> * Let $A = \{0, 1, 2\}$, $B = \{u, v\}$ and $R = \{(0, u), (0, v), (1, v), (2, u)\}$.
> * Is it true that $R \subseteq A \times B$?
> * Draw the graph.

We can also represent a binary relation $R$ by a *table* showing the ordered pairs of R.

Let $A = \{0, 1, 2\}$, $B = \{u, v\}$ and $R = \{(0, u), (0, v), (1, v), (2, u)\}$.

The table looks like this:

R   |u  |v
|---|---|---
0   | 1 | 1
1   | 0 | 1
2   | 1 | 0

Relations represent *one to many relationships* between elements in $A$ and $B$.

#### Theorem: The number of binary relations on a set A where $\mid A \mid = n$ is: $2^{n^2}$
> Proof:
>* If $\mid A \mid = n$ then the cardinality of the Cartesian product $\mid A \times A \mid = n^2$.
>* $R$ is a binary relation on $A$ if $R \subseteq A \times A$ (that is, $R$ is a subset of $A \times A$).
>* The number of subsets of a set with $k$ elements: $2^k$
>* The number of subsets of $A \times A$ is $2^{A \times A} = 2^{n^2}$

-------

### Types of Relations

Let's come up with examples for each.

* **Empty Relation**: A relation $R$ on a set $A$ is called Empty if the set $A$ is empty set.
* **Full Relation**: A binary relation $R$ on a set $A$ and $B$ is called full if $A \times B$.
* **Reflexive Relation**: A relation $R$ on a set $A$ is called reflexive if $(a, a) \in R$ holds for every element $a \in A$, e.g. if set $A = \{a, b\}$ then $R = \{(a, a), (b, b)\}$ is reflexive relation.
* **Irreflexive relation**: A relation $R$ on a set $A$ is called reflexive if no $(a, a) \in R$ holds for every element $a \in A$, e.g. if set $A = \{a, b\}$ then $R = \{(a, b), (b, a)\}$ is irreflexive relation.
* **Symmetric Relation**: A relation $R$ on a set $A$ is called symmetric if $(b, a) \in R$ holds when $(a, b) \in R$, e.g. The relation $R=\{(4, 5), (5, 4), (6, 5), (5, 6)\}$ on set $A=\{4, 5, 6\}$ is symmetric.
* **Anti-Symmetric Relation**: A relation $R$ on a set $A$ is called anti-symmetric if $(a, b) \in R$ and $(b, a) \in R$ then $a = b$ is called antisymmetric, e.g. The relation $R = \{(a, b) \rightarrow R \mid a \leq b\}$ is anti-symmetric since $a \leq b$ and $b \leq a$ implies $a = b$.
* **Transitive Relation**: A relation $R$ on a set $A$ is called transitive if $(a, b) \in R$ and $(b, c) \in R$ then $(a, c) \in R$ for all $a, b, c \in A$, e.g. Relation $R=\{(1, 2), (2, 3), (1, 3)\}$ on set $A=\{1, 2, 3\}$ is transitive.
* **Equivalence Relation**: A relation is an Equivalence Relation if it is reflexive, symmetric, and transitive. E.g. relation $R=\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)\}$ on set $A=\{1, 2, 3\}$ is equivalence relation as it is reflexive, symmetric, and transitive.
* **Asymmetric Relation**: Asymmetric relation is opposite of symmetric relation. A relation $R$ on a set $A$ is called asymmetric if no $(b, a) \in R$ when $(a,b) \in R$.

### Exercises:
Consider the following relations on the set A = {1, 2, 3, 4}:
1. $R1 = \{(1, 1), (1, 2), (2, 3), (1, 3), (4, 4)\}$
1. $R2 = \{(1, 1)(1, 2), (2, 1), (2, 2), (3, 3), (4, 4)\}$
1. $R3 = \{(1, 3), (2, 1)\}$
1. $R4 = \varnothing$, the empty relation
1. $R5 = A \times A$, the universal relation

Which of the relations are reflexive.

Which of these are symmetric?

------
Consider the following relations:
1. Relation $\leq$ (less than or equal) on the set $\mathbb{Z}$ of integers.
1. Set inclusion $\subseteq$ on a collection $C$ of sets.
1. Relation $\perp$ (perpendicular) on the set $L$ of lines in the plane.
1. Relation $\parallel$ (parallel) on the set $L$ of lines in the plane.
1. Relation $\mid$ of divisibility on the set $\mathbb{N}$ of positive integers. (Recall $x \mid y$ if there exists $z$ such that $xz = y$.)


Which of the relations are reflexive.

Which of these are symmetric?

Which are transitive and which not?
