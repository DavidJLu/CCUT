#CS250 at CCUT Week 1 Day 2: Relations

You should have had an introduction to set theory by now. Let's do a quick recap and take a look at the next topic: relations.

#### Sets
* A set is an unordered collection of objects, e.g., students in this class; air molecules in this room.
* The objects in a set are called the elements, or members of the set. A set is said to contain its elements.
* The notation $x \in S$ denotes that $x$ is an element of the set $S$.
* If $x$ is not a member of $S$, write $x \notin S$.

#### Describing sets
* $S = \{a, b, c, d\}$.
* Order not important $S = \{a, b, c, d\} = \{b, c, a, d\}$.
* Each distinct object is either a member or not; listing more than once does not change the set. $S = \{a, b, c, d\} = \{a, b, c, b, c, d\}$.
* Dots “. . . ” may be used to describe a set without listing all of the members when the pattern is clear. $S = \{a, b, c, d, . . . , z\}$ or $S = \{5, 6, 7, . . . , 20\}$.
* Try not to overuse this. Patters are not always as clear as the writer thinks

#### Important sets
$\mathbb{B}$ = Boolean values = $\{true, false\}$
$\mathbb{N}$ = natural numbers = $\{0, 1, 2, 3, . . . \}$
$\mathbb{Z}$ = integers = $\{. . . , -3, -2, -1, 0, 1, 2, 3, . . . \}$
$\mathbb{Z}+$ = $\mathbb{Z}\geq 1$ = positive integers = $\{1, 2, 3, . . . \}$
$\mathbb{R}$ = set of real numbers
$\mathbb{R}+$ = $\mathbb{R} > 0$ = set of positive real numbers
$\mathbb{C}$ = set of complex numbers
$\mathbb{Q}$ = set of rational numbers

#### Set Builder Notation
Another way of describing a set is to specify the property (or properties) that all members of the set must satisfy. We use a pipe, '$\mid$', to read "such that."

* $S = \{x \mid$ x is a positive integer less than 100 $\}$
* $S = \{x \mid x \in \mathbb{Z}+$ and $x < 100\}$
* $S = \{x \in \mathbb{Z}+ \mid x < 100\}$
* A predicate can be used, e.g., $S = \{x \mid P(x)\}$ where $P(x)$ is true iff $x$ is a prime number.
* Positive rational numbers $\mathbb{Q}+ = \{x \in \mathbb{R} \mid \exists p, q \in \mathbb{Z}+ x = p/q\}$

#### Interval Notation
We can use interval notation to describe subsets of sets upon which an order is defined, e.g., numbers.
* $[a, b] = \{x \mid a \leq x \leq b\}$
* $[a, b) = \{x \mid a \leq x < b\}$
* $(a, b] = \{x \mid a < x \leq b\}$
* $(a, b) = \{x \mid a < x < b\}$
* closed interval $[a, b]$
* open interval $(a, b)$
* half-open intervals $[a, b)$ and $(a, b]$
------
### Introduction to Relations

Let $A = \{a_1, a_2, ..., a_k\}$ and $B = \{b_1, b_2, ..., b_m\}$

Recall that a **Cartesian product** $A \times B$ is defined by a set of pairs $\{(a_1, b_1), (a_1, b_2), ..., (a_1, b_m), ..., (a_k, b_m)\}$.

A **Cartesian product** defines a product set, or a set of all ordered arrangements of elements in sets in the Cartesian product.

#### Binary relations
Definition: Let $A$ and $B$ be two sets. A binary relation from $A$ to $B$ is a subset of a Cartesian product $A \times B$.

* Let $R \subseteq A \times B$ mean $R$ is a set of ordered pairs of the form $(a, b)$ where $a \in A$ and $b \in B$.
* We use the notation $aRb$ or sometimes $Rab$ to denote $(a, b) \in R$.
* If $aRb$, we say that $a$ is related to $b$ by $R$.

>Example: Let $A=\{a, b, c\}$ and $B = \{1, 2, 3\}$.
> * Is $R = \{(a, 1), (b, 2), (c, 2)\}$ a relation from $A$ to $B$?
> * Is $Q = \{(1, a), (2, b)\}$ a relation from $A$ to $B$?
> * Is $P = \{(a, a), (b, c), (b, a)\}$ a relation from $A$ to $A$?

> Exercise: List all of the binary relations on the set $\{0, 1\}$

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

-------
