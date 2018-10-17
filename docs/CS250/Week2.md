#CS250 at CCUT Week 2: Relations

### Introduction to Relations and Functions

Let $A = \{a_1, a_2, ..., a_k\}$ and $B = \{b_1, b_2, ..., b_m\}$

Recall that a **Cartesian product** $A \times B$ is defined by a set of pairs $\{(a_1, b_1), (a_1, b_2), ..., (a_1, b_m), ..., (a_k, b_m)\}$.

A **Cartesian product** defines a product set, or a set of all ordered arrangements of elements in sets in the Cartesian product.

### Binary relations:

If $A = \{1, 2\}$ and $B = \{a, b, c\}$, then:

$A \times B = \{\langle 1, a \rangle, \langle 1, b \rangle, \langle 1, c \rangle, \langle 2, a \rangle, \langle 2, b \rangle, \langle 2, c \rangle\}$
<br>

>A *binary relation* $R$ from $A$ to $B$ is a subset of $A \times B$
If $\langle a, b \rangle \in R$, then we can write $Rab$ or $aRb$.
The former is typically preferred, since it allows us an easy convention for notating relationships with >2 relata, e.g. $Rabc$, and to notate the negation $\neg Rab$, using our logical vocabulary.

>The *inverse relation* $R^{-1}$ is the relation from $B$ to $A$ which consists of the ordered pairs, which, when reversed, belong to $R$. In symbolic notation: $R^{-1} = \{\langle b, a \rangle | \langle a, b \rangle \in R\}$

<br>

1. Relations can be depicted by graphs. Draw a graph for the following relation $R$.
$R = \{\langle 1, 2 \rangle, \langle 2, 2 \rangle, \langle 2, 4 \rangle, \langle 3, 2 \rangle, \langle 3, 4 \rangle, \langle 4, 1\rangle, \langle 4, 3 \rangle \}$
<!-- -->
<br>

2. What does the inverse $R^{-1}$ look like?
<!-- -->
<br>

3. Relations can also be represented as a table or two dimensional array. What would that look like? Construct one for $R$.
<!---- --->
<br>

>Relation Composition or product:
Suppose that we have three sets $A$, $B$, and $C$, a relation $R$ defined from $A$ to $B$, and a relation $S$ defined from $B$ to $C$. We can define a composition of $R$ and $S$, written $(R | S)$ (but sometimes $S \circ R$), as follows. If $a$ is an element of $A$ and $c$ is an element of $C$, then $(R | S)ac$ iff there exists some element $b$ in $B$ such that $Rab$ and $Sbc$. So we have a relation $R|S$ from $a$ to $c$ iff $a$ is $R$ related to $b$ and $b$ is $S$ related to $c$.

4. Let $A$ = {1, 2, 3, 4}, $R$ = {(1, 2), (1, 2), (2, 4), (3, 2)}  ----- using () as angle brackets
and $S$ = {(1, 4), (1, 3), (2, 3), (3, 1), (4, 1)}
Find $R|S$.

<!--- $S \circ R$ = {(1, 3), (1, 4), (1, 1), (2, 1), (3, 3)} -->
<br>

>Relations have many interesting properties. Some that we're interested in include: reflexivity, symmetry, antisymmetry, transitivity, equivalence, and partial and total order.

-------

### Relationship Properties

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
-----

5. Construct or name an example for each property.
<br>

6. Consider the following relations on the set $A$ = {1, 2, 3}.
$R$ = {(1, 1), (1, 2), (1, 3), (3, 3)}
$S$ = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
$T$ = {(1, 1), (1, 2), (2, 2), (2, 3)}
$\emptyset$ = empty relation
$A \times A$ = universal relation on $A$

Determine whether or not each of the relations is (a) reflexive, (b) symmetric, (c) transitive, and (d) antisymmetric.

7. Consider the following relations:

	1. Relation $\leq$ (less than or equal) on the set $\mathbb{Z}$ of integers.
	1. Set inclusion $\subseteq$ on a collection $C$ of sets.
	1. Relation $\perp$ (perpendicular) on the set $L$ of lines in the plane.
	1. Relation $\parallel$ (parallel) on the set $L$ of lines in the plane.
	1. Relation $\mid$ of divisibility on the set $\mathbb{N}$ of positive integers. (Recall $x \mid y$ if there exists $z$ such that $xz = y$.)


Which of the relations are reflexive.

Which of these are symmetric?

Which are transitive and which not?

8. Consider the following relations on the set A = {1, 2, 3, 4}:
	1. $R1 = \{(1, 1), (1, 2), (2, 3), (1, 3), (4, 4)\}$
	1. $R2 = \{(1, 1)(1, 2), (2, 1), (2, 2), (3, 3), (4, 4)\}$
	1. $R3 = \{(1, 3), (2, 1)\}$
	1. $R4 = \varnothing$, the empty relation
	1. $R5 = A \times A$, the universal relation

Which of the relations are reflexive.

Which of these are symmetric?

-------
## Functions Examples and Exercises

Some definitions first.

Functions are ordinarily denoted by symbols. Suppose that for each element of a set $A$, the **domain**, we assign a unique element of a set $B$, the **codomain**. The collection of these assignments is called a function from $A$ to $B$. Let $f$ denote that function. We write:

$f: A \to B$

We can also say that $f$ **maps** $A$ to $B$.

Functions are often expressed by means of a mathematical formula. For example, consider the function which maps each real number to its square. We can denote this function by writing

* $f(x) = x^2$
* $x \mapsto x^2$
* $y = x^2$

In the first notation, $x$ is called a *variable* or *argument* and the letter $f$ denotes the function.
In the second, the barred arrow $\mapsto$ is read "goes to" or "maps to". (The LaTeX command is \mapsto).
In the last, $x$ is called the *independent variable* and $y$ is called the *dependent variable* since the value of $y$ depends on the value of $x$.

Exercises:
Find the domain $D$ of each of the following real-valued functions of a real variable:

(a) $f(x) = \frac{1}{x-2}$
<!--- f is not defined for x-2=0, so D = {Reals \ 2} -->

(b) $f(x) = x^2 - 3x - 4$
<!--- f is defined for every real number, so D = {R}  --->

(c) $f(x) = \sqrt{25-x^2}$
<!--- f is not defined when 25-x^2 is negative, so D = [-5, 5] = {x | -5 <= x <= 5}  ---->


#### Functions as Relations
Every function $f: A \to B$ defines a relation from $A$ to $B$ called the *graph of $f$*

Graph of $f = \{\langle a, b \rangle | a \in A,f(a) = b \in B\}$

Two functions $f: A \to B$ and $g: A \to B$ are *equal* if for every $a \in A$, $f(a) = g(a)$, i.e. they have the same graph.

Exercise: Map the function $f(x) = x^2 - 2x - 3$

#### Classes of Functions
A function is injective (one-to-one) if each element of the codomain is mapped to by *at most* one element of the domain.
That is, for all $x, x' \in A$, $f(x) = f(x') \to x = x'$

A function is surjective (onto) if each element of the codomain is mapped to by *at least* one element of the domain.
That is, for all $y \in B$, there exists an $x \in A$ such that $f(x) = y$

A function is bijective (one-to-one and onto or one-to-one correspondence) if each element of the codomain is mapped to by *exactly* one element of the domain.

### Exercises:
1. Consider functions $f: A \to B$ and $g: B \to C$.

Prove the following:
(a) if $f$ and $g$ are injective (one-to-one), then the composition function $g \circ f$ is injective (one-to-one)$.

<!---  Suppose $(g \circ f)(x) = (g \circ f)(y), then $g(f(x)) = g(f(y)). So $f(x) = f(y)$ because g is injective. Further, x = y since $f$ is injective. Thus, $g \circ f$ is injective. --->

(b) if $f$ and $g$ are surjective (onto) functions, then $g \circ f$ is an surjective (onto) function.
<!---  Let $c$ be an arbitrary element of $C$. Since $g$ is surjective, there exists a $b \in B$ such that $g(b) = c$. Since $f$ is surjective, there exists an $a \in A$ such that $f(a) = b$. But also $(g \circ f)(a) = g(f(a)) = g(b) = c$. Hence, each $c \in C$ is the mapping of some element $a \in A$. Therefore, $g \circ f$ is a surjective function.  -->

2. Determine if each function is injective (one-to-one):
(c) To each person on the earth, assign the number which corresponds to her or his age.
(d) To each country in the world, assign the latitude and longitude of its capital.
(e) To each book written by only one author, assign the author.
(f) To each country in the world which has a prime minister, assign its prime minister.
 <!-- no, yes, no, yes -->



3. Problem: Show that if $f$ is bijective, an inverse $g$ of $f$ exists. (define such a $g$ show that it is a function, and show that it is an inverse of $f$.)

<details><summary>Proof:</summary>

 Let $f: A \to B$ be bijective. We'll define a function $g: A \to B$ = $f^{-1}$ as follows. Let $b \in B$. since $f$ is surjective, there exists $a \in A$ such that $f(a) = b$. Let $g(b) = a$. Since $f$ is injective, this $a$ is unique, so $g$ is a well-defined function.

 Next, we show that $g$ is the inverse of $f$. First, we show that $g \circ f = id_A$.
 First, let $a \in A$. Let $b = f(a)$. Then by definition $g(b) = a$. then $g \circ f(a) = g(f(a)) = g(b) = a$.
 Second, show that $f \circ g = id_B$. Let $b \in B$ and $f^{-1}(b) = g(b) = a$. By definition, $f(a) = b$. It follows that $f \circ g(b) = f(g(b)) = f(a) = b$.
 </details>
