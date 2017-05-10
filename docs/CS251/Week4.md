CS251 at CCUT Week 4: The Predicate Calculus
=======
David Lu
5/8/17


![Matrix](matrix.jpg)

What Propositional Logic Can't Do
------

There are many arguments whose formal validity cannot be shown using just the propositional logic. Consider the following argument:

1. All humans are mortal.
2. Socrates is a human.
3. Therefore, Socrates is mortal.

Propositional logic takes each of these statements as atomic propositions and thus logically unrelated. We might translate this to the propositional logic like so:

1. H
2. S
3. M

But as we can see from the following truth assignment, the arugment is invalid:

H | S | M
:--:|:-:|:-:
T | T | F

This row of the truth table shows that it is possible for the premises to be true while the conclusion false, as construed in the propositional logic.

However, intuitively this argument *is* formally valid. Propositional logic does not represent the *internal* structure of an atomic sentence. And it is by virtue of logical features of the structure of these atomic sentences that this argument is formally valid. So we need a more detailed formal language to represent this kind of argument.

The Language of Predicate Calculus: Vocabulary and Syntax
-----

**Vocabulary**

* Logical Connectives: $\neg$, $\land$, $\lor$, $\rightarrow$, $\equiv$.

* Individual Constants: lower case letters of the alphabet toward the beginning ($a, b, c,$ ...)

* Predicates: upper case letters ($A, B, C, ..., Z$)

* Individual Variables: $x, y, z$

* Quantifiers: $\forall$ (universal quantifier); $\exists$ (existential quantifier)

The language of predicate calculus retains all of the logical vocabulary of propositional logic but replaces atomic sentences with predicate and individual constants and variables, and quantifiers.

#### Individual Constants
*Individual constants* name individuals: persons, places, things

#### Predicates
*Predicates* ascribe properties and relations to individuals. One place predicates, called monadic predicates, assign properties to single individuals. For instance, being human. Two place predicates, called dyadic predicates, assign relations to pairs of individuals. For instance, being taller than. $N$-place *polyadic* predicates assign relations between $N$-individuals. The argument place matters for polyadic predicates. Examples:

PC | English |
:-----|:------------------|
$Hs$  | Socrates is human.
$Ms$  | Socrates is mortal.
$Tsp$ | Socrates is taller than Plato.
$Tps$ | Plato is taller than Socrates.
$Bcp$ | Changchun is bigger than Portland.
$Babc$| $a$ is between $b$ and $c$.

#### Singular Sentences
These statements, which assign properties to named individuals are called *singular sentences*, similar to propositional logic's atomic sentences. Every singular sentence is well-formed.

#### Compound Sentences
Just like in propositional logic, we can translate compound sentences by using the logical connectives. These have the same syntax and semantics we studied previously. Compound sentences are well-formed.

PC | English
:---| :-----
$Gs \land Ps$ | Socrates was a Greek philosopher.
$Hs \rightarrow Ms$ | If Socrates is human then Socrates is mortal.

#### Variables and Quantifiers
Recall the argument we began with. It contains the premise `All humans are mortal`. How should we translate this into a sentence of propositional calculus? Here is where we need to use variables, since the sentence states that all individuals which are humans are mortals. Notice here that the quantifier `all` is employed. We should translate this sentence as:

$\forall x (Hx \rightarrow Mx)$

That is, `for all x if x is a human, then x is mortal`.

Similarly, the existential quantifier is used in the following example:

$\exists x Hx$

That is, `there exists an x such that x is a human`.

$\neg \exists x Ux$

`Unicorns do not exist.`

A quantifier must always be paired with a variable. We say that a quantifier `binds` a variable when it is paired in this way.

Sentences may also have multiple quantifiers binding different variables.

$\forall x \exists y ((Bx \land Wy) \rightarrow Exy)$

`Every bird eats some worm.`

Quantifiers have scope.

$\exists x Hx \land \exists x Bx$

`Some human exists and some bird exists.`

Notice each existential quantifier here binds an $x$. However, the scope of the first existential quantifier ends before the $\land$. So there is no ambiguity about which $x$ is being bound by which quantifier.

The following is an example of quantifier scope ambiguity.

$\forall x(Px \rightarrow \exists x (Qx \land Rx))$

It is ambiguous which quantifier binds the $x$es in the $Qx$ and $Rx$. In such cases choose another variable letter to disambiguate.

#### Free variables
Notice that the sentence $Hx$ is not a complete sentence. What could this say? When would it be true and when would it be false?

If a variable is not bound by a quantifier in a sentence, then we call it a `free variable`. The sentence is then not a complete sentence, i.e. it does not have a truth value since it does not have any truth conditions.



Predicate Calculus Translation Practice
======
1. Mary loves everyone
1. Mary loves everyone
1. No one talks
1. Everyone loves themself
1. Everyone loves everyone
1. Everyone loves everyone except themself
1. Every student smiles
1. Every student except George smiles
1. Everyone walks or talks
1. Every student walks or talks
1. Every student who walks talks
1. Every student who loves Mary is happy
1. Every boy who loves Mary hates every boy who Mary loves:
1. Every boy who loves Mary hates every other boy who Mary loves:


Answers
------

1. Mary loves everyone: $\forall x Lmx$
1. Mary loves everyone: $\forall x (Hx \rightarrow Lmx)$ (Assuming domain contains non-humans)
1. No one talks: $\neg \exists x Tx$
1. Everyone loves themself: $\forall x Lxx$
1. Everyone loves everyone: $\forall x \forall y Lxy$
1. Everyone loves everyone except themself: $\forall x \forall y (x \ne y \leftrightarrow Lxy)$
1. Every student smiles: $\forall x (Sx \rightarrow Mx)$
1. Every student except George smiles: $\forall x((Sx \land x \ne g) \rightarrow Mx)$
This allows the possibility that George smiles too; if we want to exclude that we might want something like this: $\forall x(Sx \rightarrow (x \ne g \leftrightarrow Mx))$. \textit{All students are such that they smile if and only if they are not identical to George.}
1. Everyone walks or talks: $\forall x (Wx \lor Tx)$
1. Every student walks or talks: $\forall x (Sx \rightarrow (Wx \lor Tx))$
1. Every student who walks talks: $\forall x((Sx \land Wx) \rightarrow Tx)$
1. Every student who loves Mary is happy: $\forall x((Sx \land Lxm) \rightarrow Hx)$
1. Every boy who loves Mary hates every boy who Mary loves:
$\forall x[(Bx \land Lxm) \rightarrow (\forall y(By \land Lmy) \rightarrow Hxy)]$ or by Exportation
$\forall x\forall y[((Bx \land Lxm) \land (By \land Lmy)) \rightarrow Hxy]$
1. Every boy who loves Mary hates every other boy who Mary loves:
$\forall x\{[(Bx \land Lxm) \rightarrow \forall y((By \land Lmy) \land y \ne x)] \rightarrow Hxy)\}$ or
$\forall x\forall y \{[(Bx \land Lxm) \land ((By \land Lmy) \land x \ne y)] \rightarrow Hxy\}$
If John loves Mary and Mary loves John, 13 says that John hates himself, but 14 does not.


Natural Deduction with Quantifiers
======

There are four quantifier rules that we need for extending our natural deduction system to predicate calculus. We need introduction and elimination rules for each of the two quantifiers. You can find an explanation of these rules at the following pdf:

[Quantifier Rules](QuantifierRules.pdf)

> All humans are mortal. Socrates is a human. Therefore, Socrates is mortal.
>$\forall x (Hx \rightarrow Mx), Hs$ $\vdash Ms$

$Proof$:

| |
|-
|1| $\forall x (Hx \rightarrow Mx)$ | | Premise|
|2| $Hs$ | | Premise |
|3| $Hs \rightarrow Ms$| 1 | UI|
|4| $Ms$ | 2, 3| MP|

Showing Invalidity
=======
In the propositional logic, we could show that an argument is `invalid` by finding a row of the truth table where the premises are true and the conclusion false. That would show that it is possible for the truth of the premises to fail to guarantee the truth of the conclusion. This works because the truth table contains every possible combination of truth values for the atomic sentences.

However, predicate calculus sentences may contain variables which range over some domain. That domain may contain an infinite number of items. For instance the set of natural numbers $\mathbb{N}$ is a set with countably infinite cardinality. We could not produce a truth table for a sentence that said something about the natural numbers.

Consider every natural number is even or odd:

$\forall x (Ex \lor Ox)$ where $x \in \mathbb{N}$

So we cannot show the invalidity of a predicate calculus argument by truth table. We need another method.

#### Models

A model is a domain of individuals and a specification of all properties and relations of those individuals. For instance, we might imagine a universe with two individuals, $a$ and $b$, and $a$ has the property $P$ while $b$ does not, and nothing else about the universe is true. This is a model and we could represent it using a table.

| | $P$ |
|:-|-   |
|$a$| T |
|$b$| F |

To show that an argument is invalid, we need to be able to create a model where the premises are true and the conclusion is false.

Predicate Calculus Argument Exercises
-------

1. $\forall x(Fx \rightarrow Gx)$, $\exists x(Hx \land \neg Gx))$ $\vdash \exists x(Hx \land \neg Fx)$

2. $\vdash \exists x (Fx \lor Gx)) \leftrightarrow (\exists x Fx \lor \exists x G)$

3. $\vdash (\forall x(Px \rightarrow Qx) \land \exists x Px) \rightarrow \exists x Qx$

4. $\vdash \forall x(Px \rightarrow Qx) \rightarrow (\exists x Px \rightarrow \exists x Qx)$
