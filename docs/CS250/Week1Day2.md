#CS250 at CCUT Week 2: Relations

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

#### Universal Set and Empty Set

* The universal set $U$ is the set containing everything currently under consideration.
  * Content depends on the context.
  * Sometimes explicitly stated, sometimes implicit.
* The empty set is the set with no elements.
Symbolized by $\varnothing$ or $\{\}$.

#### Things to remember
* Sets can be elements of other sets, e.g.,
$\{\{1, 2, 3\}, a, \{u\}, \{b, c\}\}$
* The empty set is different from the set containing the empty set $\varnothing \neq \{\varnothing\}$

#### Subsets and Set Equality
>Definition:
Set $A$ is a subset of set $B$ iff every element of $A$ is also an element of
$B$.

* Formally: $A \subseteq B \leftrightarrow \forall x(x \in A \rightarrow x \in B)$
* In particular, $\varnothing \subseteq S$ and $S \subseteq S$ for every set $S$.

>Definition:
Two sets A and B are equal iff they have the same elements.

* Formally: $A = B \leftrightarrow A \subseteq B \land B \subseteq A$.
* Example: {1, 5, 5, 5, 3, 3, 1} = {1, 3, 5} = {3, 5, 1}.

#### Proper Subsets
>Definition:
A is a proper subset of B iff A ⊆ B and A 6= B.

* This is denoted by $A \subset B$.
* $A \subset B$ can be expressed by
$\forall x(x \in A \rightarrow x \in B) \land \exists x(x \in B \land x \notin A)$

#### Set Cardinality
>Definition:
If there are exactly $n$ distinct elements in a set $S$, where $n$ is a nonnegative integer, we say that $S$ is finite. Otherwise it is infinite.

>Definition
The cardinality of a finite set $S$, denoted by $|S|$, is the number of
(distinct) elements of $S$.


Examples:
* $|\varnothing| = 0$
* Let S be the set of letters of the English alphabet. Then $|S| = 26$.
* $|\{1, 2, 3\}| = 3$
* $|\{\varnothing\}| = 1$
* The set of integers Z is infinite.

#### Power Sets

>Definition
The set of all subsets of a set $S$ is called the power set of $S$.

* It is denoted by $\wp (S)$.
* Formally: $\wp(S) = \{S' \mid S' \subseteq S\}$
* In particular, $S \in \wp(S)$ and $\varnothing \in \wp(S)$.
* Example: $\wp(\{a, b\}) = \{\varnothing, \{a\}, \{b\}, \{a, b\}\}$
* If $|S| = n$ then $|\wp(S)| = 2^n$

#### Tuples
* The ordered $n$-tuple $(a_1, a_2, ... , a_n)$ is the ordered collection of $n$ elements, where $a_1$ is the first, $a_2$ the second, etc., and an the $n$-th (i.e., the last).
* Two $n$-tuples are equal iff their corresponding elements are equal.
$(a_1, a_2, ... , a_n) = (b_1, b_2, ... , b_n) \leftrightarrow a_1 = b_1 \land a_2 = b_2 \land ...  \land a_n = b_n$
* 2-tuples are called ordered pairs

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
