#CS250 at CCUT Week 2: Relations

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
