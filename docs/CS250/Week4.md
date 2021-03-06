---
presentation:
  # The "normal" size of the presentation, aspect ratio will be preserved
  # when the presentation is scaled to fit different resolutions. Can be
  # specified using percentage units.
  width: 960
  height: 700
  transition: 'slide'
---

<!-- slide data-transition='zoom'-->
# CS250 at CCUT Week 4: Relations and Ordering

<!-- slide -->
Recall we left off last week beginning to look at the properties of binary relations.

Let's continue.

<!-- slide -->
## Reflexivity

<!-- slide -->
A relation $R$ on a set $S$ is called **reflexive** if and only if $(a, a) \in R$ for every element $a$ of $S$.

<!-- slide vertical=true -->

In other words, a relation is reflexive if every element of the relation is related to itself.

<!-- slide vertical=true -->
Example:
The relation $\leq$ on the set of integers $\{1, 2, 3\}$ is:

$\{(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)\}$

<!-- slide vertical=true-->
### Is it reflexive?

* This relation is reflexive since it contains $(1, 1), (2, 2), (3, 3)$. <!-- .element: class="fragment" data-fragment-index="1" -->

* **In fact $\leq$ on any set of numbers is reflexive!** <!-- .element: class="fragment" data-fragment-index="2" -->

<!-- slide -->
#### Irreflexivity

A relation $R$ on a set $S$ is called **irreflexive** if $(a, a) \notin R$ for every $a \in S$.

<!-- slide vertical=true -->
Example:
Let $S = \{a, b\}$ and $R = \{(a, b), (b, a)\}$ be a relation on $A$.

$R$ is an irreflexive relation.

<!-- slide data-transition='zoom' -->
## Symmetry

<!-- slide -->
A relation $R$ on a set $S$ is called **symmetric** if and only if for any $a$ and $b \in S$, whenever $(a, b) \in R$, $(b, a) \in R$

<!-- slide -->
Example:
The relation $=$ on the set of integers $\{1, 2, 3\}$ is $\{(1, 1) , (2, 2), (3, 3)\}$ and it is *symmetric*.

<!-- slide -->
Question:
Is the relation $\leq$ on the set of integers $\{1, 2, 3\}$ *symmetric*?

* No.  <!-- .element: class="fragment" data-fragment-index="1" -->
* Why not? <!-- .element: class="fragment" data-fragment-index="2" -->
* Because $(1, 3)$ is in the relation but $(3, 1)$ is not <!-- .element: class="fragment" data-fragment-index="3" -->

<!-- slide -->
The relation *being the same height as* on a set of people is a symmetric relation.

The relation *being taller than* on a set of people is not.

<!-- slide -->
### Antisymmetry

<!-- slide -->
$R$ on a set $S$ is **anti-symmetric** if there is no pair of *distinct* elements of $X$ each of which is related by $R$ to the other.

<!-- slide data-transition="fade" -->
More formally, $R$ is anti-symmetric if for all $a$ and $b \in X$, if $Rab$ and $Rba$, then $a = b$

* Put another way: if $(a, b) \in R$ and $a \neq b$, then $(b, a) \notin R$ must not hold. <!-- .element: class="fragment" data-fragment-index="1" -->

<!-- slide -->
Most formally:
$\forall a, b \in S, (Rab \land Rba) \Rightarrow a = b$

Or equivalently:
$\forall a, b \in S, (Rab \land a \neq b) \Rightarrow \neg Rba$

<!-- slide -->
Example:
The subset order $\subseteq$ on the subsets of any given set is anti-symmetric.

<!-- slide vertical=true -->
Given two sets $A$ and $B$, if every element in $A$ is also in $B$ and every element in $B$ is also in $A$, then $A$ and $B$ must contain all the same elements and therefore be equal:

$A \subseteq B \land B \subseteq A \Rightarrow A = B$

<!-- slide -->
Example 2:
The $\leq$ relation on $\mathbb{R}$ is anti-symmetric.

<!-- slide -->
If for two real numbers $x$ and $y$ both inequalities $x \leq y$ and $y \leq x$ are true then $x$ and $y$ must be equal.

<!-- slide -->
Strange Note:
It's possible for a relation to be both symmetric and anti-symmetric!

Can you think of an example?

* How about equality? <!-- .element: class="fragment" data-fragment-index="1" -->

<!-- slide data-transition="zoom" -->
## Transitivity

<!-- slide -->
A binary relation $R$ over a set $S$ is **transitive** if whenever an element $a$ is related to an element $b$ and $b$ is related to an element $c$ then $a$ is also related to $c$.

<!-- slide -->
Formally:

$\forall a, b, c \in S, (Rab \land Rbc) \Rightarrow Rac$

<!-- slide -->
Example:

The relation *greater than* on the set of integers is a transitive relation.

I.e. Whenever $x > y$ and $y > z$ it holds that $x > z$.

<!-- slide -->

On the other hand, *mother of* is not transitive.

If Alice is the mother of Barbara, and Barbara is the mother of Clara, it cannot be the case that Alice is the mother of Barbara.

<!-- slide -->

Example:
Is the relation *sister of* transitive?

<!-- slide -->

<!-- slide data-transition="fade" -->
## Partial Order Relations

<!-- slide -->
Partial Order Relation: A binary relation $R$ on a set $A$ is a *partial order* if and only if it is:
* Reflexive
* Antisymmetric
* Transitive

<!-- slide data-background-video="../Duke.mp4" data-background-video-loop=true -->
