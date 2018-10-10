#CS250 at CCUT Week 2: Relations

### Introduction to Relations

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

5. Construct or name an example for each property.
<br>

6. Consider the following relations on the set $A$ = {1, 2, 3}.
$R$ = {(1, 1), (1, 2), (1, 3), (3, 3)}
$S$ = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
$T$ = {(1, 1), (1, 2), (2, 2), (2, 3)}
$\emptyset$ = empty relation
$A \times A$ = universal relation on $A$

Determine whether or not each of the relations is (a) reflexive, (b) symmetric, (c) transitive, and (d) antisymmetric.## Relations

Some examples:
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

5. Construct or name an example for each property.
<br>

6. Consider the following relations on the set $A$ = {1, 2, 3}.
$R$ = {(1, 1), (1, 2), (1, 3), (3, 3)}
$S$ = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
$T$ = {(1, 1), (1, 2), (2, 2), (2, 3)}
$\emptyset$ = empty relation
$A \times A$ = universal relation on $A$

Determine whether or not each of the relations is (a) reflexive, (b) symmetric, (c) transitive, and (d) antisymmetric.
