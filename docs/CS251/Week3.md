# CS251 at CCUT Week 3: Arguments in Propositional Logic
4/26/17

![keyboard](keyboard.jpg)

Outline: <a id="index"></a>
  * [Arguments and Validity](#validity)
    * [Soundness](#sound)
  * [Methods](#methods)
    * [Truth Tables](#truthtables)
    * [Natural Deduction](#natural)
  * [Sentence Forms](#forms)
    * [Tautology](#taut)
    * [Contradiction](#contra)
    * [Contingency](#contingent)
  * [Equivalence](#equiv)
    * [Inequivalence](#inequiv)
  * [Sets of Sentences](#sets)
    * [Consistency](#consistent)
    * [Inconsistency](#inconsistent)
  * [Practice Problems](#practice)

Many examples and exercises on this page are sourced from [*forall x: Calgary Remix An Introduction to Formal Logic*](http://openlogicproject.org/2017/01/18/forall-x-calgary-remix/) by P. D. Magnus and Tim Button with additions by J. Robert Loftis and remixed and revised by Aaron Thomas-Bolduc and Richard Zach under a [Creative Commons Attribution-ShareAlike 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).




Argument Validity <a id="validity"></a>
===========
Logic is in the business of evaluating arguments. We study logic to discover (or build) methods for precisely sorting good from bad arguments. There are a number of other related concepts that will be useful to discuss as well. We will take these in turn.

An argument is a line of reasoning that takes us from some assumptions to a conclusion. Take for instance the following argument:

  > It is raining heavily.
  > If you do not take an umbrella, you will get soaked.
  > So, you should take an umbrella

More precisely, an argument is a set of sentences of which one is called the **conclusion** and the others are called the **premises**. The conclusion is often indicated by the words *therefore*, *so*, *hence*, and *thus* while premises are sometimes indicated by *since* and *because*

Often arguments in natural language omit some premises which are obvious or implied by context. The argument above omits the premise that you don't want to get soaked. We call these *enthymematic* arguments.

As an addition to our vocabulary of propositional logic, we use the symbol $\therefore$ to mean therefore.

### Test yourself:
Identify the conclusion of these arguments.

>1. It is sunny. So I should take my sunglasses.

>2. It must have been sunny. I did wear my sunglasses, after all.

>3. No one but you has had their hands in the cookie-jar. And the scene of the crime is littered with cookie-crumbs. You’re the culprit!

>4. Miss Scarlett and Professor Plum were in the study at the time of the murder. Reverend Green had the candlestick in the ballroom, and we know that there is no blood on his hands. Hence Colonel Mustard did it in the kitchen with the lead-piping. Recall, after all, that the gun had not been fired.

## Validity
We define validity to be a property of an argument.

> An argument is valid if and only if it is impossible for the premises to be true while the conclusion false.

We can put this another way: `An argument is valid if and only if the truth of the premises guarantees the truth of the conclusion.`

And a third way: `An argument is valid if and only if whenever the premises are true, the conclusion is also true.`

These three definitions say the same thing.



### Test yourself
Can you figure out which of the following arguments are valid? Which are invalid?

A.
  >1. Socrates is a man.
  >2. All men are carrots.
  >$\therefore$ Socrates is a carrot.

B.  
  >1. Abe Lincoln was either born in Illinois or he was once president.
  >2. Abe Lincoln was never president.
  >$\therefore$ Abe Lincoln was born in Illinois.

C.  
  >1. If I pull the trigger, Abe Lincoln will die.
  >2. I do not pull the trigger.
  >$\therefore$ Abe Lincoln will not die.

D.
  >1. Abe Lincoln was either from France or from Luxemborg.
  >2. Abe Lincoln was not from Luxemborg.
  >$\therefore$ Abe Lincoln was from France.

E.  
  >1. If the world were to end today, then I would not need to get up tomorrow morning.
  >2. I will need to get up tomorrow morning.
  >$\therefore$ The world will not end today.

F.
  >1. Joe is now 19 years old.
  >2. Joe is now 87 years old.
  >$\therefore$ Bob is now 20 years old.

<br>


## Soundness <a id="sound"></a>
We are often interested in more than whether an argument is valid. We also want to know whether we should believe the conclusion is true. If an argument is valid **and** the premises are true, then we say that the argument is **sound**

>An argument is sound if and only if it is valid and the premises are true.

It follows from the definition that the conclusion of a sound argument is true.

<br>
#### Could there be:

In each case: if so, give an example; if not, explain why not.

>1. A valid argument that has one false premise and one true
premise?

>2. A valid argument that has only false premises?

>3. A valid argument with only false premises and a false conclusion?

>4. A sound argument with a false conclusion?

>5. An invalid argument that can be made valid by the addition of a new premise?

>6. A valid argument that can be made invalid by the addition of a new premise?



[Back to the Top](#index)

# Methods <a id="methods"></a>
Recall that one main reason to study logic is to be more precise. So can we be more precise than reading English arguments and trying to decide whether they are valid or not?

Yes, formal logic attempts to provide precise methods for determining whether an argument is valid or not. In this section, we will look at two methods for determining validity. These methods can also be used to determine some other properties we are interested in.

The two methods fall into the categories of truth tables and natural deduction. There are other methods (axiomatic logic) but these two are easier to use and understand.

[Back to the Top](#index)

## Truth Tables <a id="truthtables"></a>
Every non-atomic sentence of PL is composed of atomic sentences with logical connectives. We call these **compound sentences**. The truth value of compound sentences depends *only* on the truth value of the atomic sentences that comprise it along with the semantics of the logical connectives.

For example, in order to know the truth value of $D \land E$, we need only to know the truth values of $D$ and $E$ as well as the meaning of the connective $\land$.

As we saw last week, we can use truth tables to show a mapping of the truth values.

For instance the truth value of the compound sentence $\neg p$ is summarized by the following truth table:
p | $\neg$ p
:-|:-
T | F
F | T

We can use this same truth table method to **decide** whether an argument is valid or invalid. To show that an argument is valid, we must show that it is impossible for the premises to be true while the conclusion false. Or, in other words, whenever the premises are true, the conclusion is also true.

To use this truth table method for showing validity of an argument, we need to draw the truth table, with columns including each premise and the conclusion. Then we look to see if there are any rows where the premises are true and the conclusion is false. If so, the argument is *invalid*; if not, the argument is *valid*.

Example:
$A \rightarrow B$
$A$
$\therefore B$

A  |B   | Premise 1         | Premise 2| Conclusion
:-|:- |:-                 |:- |:-
A | B | A $\rightarrow$ B | A | B
T | T | T                 | T | T
T | F | F                 | T | F
F | T | T                 | F | T
F | F | T                 | F | F

As we can see, there is only 1 row where the premises are true (row 1), and the conclusion at row 1 is also true. So, there does not exist any row where the premises are true and the conclusion is false. We can conclude that the argument is *valid*.

Truth tables can be used to decide any of the problems in this section, i.e. they can be used to decide whether an argument is valid or invalid; they can be used to decide whether a set of sentences is consistent or inconsistent; they can be used to decide whether a sentence is a tautology, contradiction, or contingency; and they can be used to decide whether two sentences are logically equivalent or inequivalent.

Another example:
H | I | (H $\land$ I) $\rightarrow$ H
:-|:--|:------------------------------
T | T | T  T  T  **T**  T
T | F | T  F  F  **T**  T
F | T | F  F  T  **T**  F
F | F | F  F  F  **T**  F

This sentence, (H $\land$ I) $\rightarrow$ H, is a tautology. We know this because the column for the sentence is true at every row. In other words, this sentence cannot be false.

The drawback of the truth table method is that as our sentences contain more atomic propositions, the number of rows in a truth table grows exponentially. A complete truth table has a line for every possible assignment of true and false to the relevant atomic sentences.

How many rows does our table need if there are 3 atomic proposition letters? What about for $n \in \mathbb{N}$ atomic proposition letters?

#### Practice problems


[Back to the Top](#index)

## Natural Deduction <a id="natural"></a>

[Back to the Top](#index)

# Sentence Forms <a id="sentence"></a>

[Back to the Top](#index)

## Tautology <a id="taut"></a>

[Back to the Top](#index)

## Contradiction <a id="contra"></a>

[Back to the Top](#index)

## Contingency <a id="contingent"></a>

[Back to the Top](#index)

# Equivalence <a id="equiv"></a>

[Back to the Top](#index)

## Inequivalence <a id="inequiv"></a>

[Back to the Top](#index)

# Sets of Sentences <a id="set"></a>

[Back to the Top](#index)

## Consistency <a id="consistent"></a>

[Back to the Top](#index)

## Inconsistency <a id="inconsistent"></a>

[Back to the Top](#index)

## Practice Problems <a id="practice"></a>
Practice exercises
##### A. Use either a derivation or a truth table for each of the following.
1. Show that $A \rightarrow (((B \land C) \lor D) \rightarrow A)$ is a tautology.

2. Show that $A \rightarrow (A \rightarrow B)$ is not a tautology
3. Show that the sentence $A \rightarrow \neg A$ is not a contradiction.
4. Show that the sentence $A \leftrightarrow \neg A$ is a contradiction.
5. Show that the sentence $\neg W \rightarrow (J \lor J))$ is contingent
6. Show that the sentence $\neg(X \lor (Y \lor Z)) \lor (X \lor (Y \lor Z))$ is not contingent
7. Show that the sentence $B \rightarrow \neg S$ is equivalent to the sentence $\neg \neg B \rightarrow \neg S$
8. Show that the sentence $\neg(X \lor O)$ is not equivalent to the
sentence $X \land O$
9. Show that the sentences $\neg(A \lor B)$, $C$, $C \rightarrow A$ are jointly inconsistent.
10. Show that the sentences $\neg(A \lor B)$, $\neg B$, $B \rightarrow A$ are jointly consistent
11. Show that $\neg(A \lor (B \lor C)) \therefore \neg C$ is valid.
12. Show that $\neg (A \land (B \lor C)) \therefore \neg C$ is invalid.

##### B. Use either a derivation or a truth table for each of the following.
1. Show that $A \rightarrow (B \rightarrow A)$ is a tautology
2. Show that $\neg (((N \leftrightarrow Q) \lor Q) \lor N)$  is not a tautology
3. Show that $Z \lor (\neg Z \leftrightarrow Z)$ is contingent
4. show that $(L \leftrightarrow ((N \rightarrow N) \rightarrow L)) \lor H$ is not contingent
5. Show that $(A \leftrightarrow A) \land (B \land \neg B)$ is a contradiction
6. Show that $(B \leftrightarrow (C \lor B))$ is not a contradiction.
7. Show that $((\neg X \leftrightarrow X) \lor X)$ is equivalent to $X$
8. Show that $F \land (K \land R)$ is not equivalent to $(F \leftrightarrow (K \leftrightarrow R))$
9. Show that the sentences $\neg (W \rightarrow W)$, $ (W \leftrightarrow W) \land W$, $E \lor (W \rightarrow \neg (E \land W))$ are inconsistent.
10. Show that the sentences :$\neg R \lor C$, $(C \land R) \rightarrow R$, $(\neg(R \lor R) \rightarrow R)$ are consistent.
11. Show that $\neg \neg (C \leftrightarrow \neg C)$, $((G \lor C) \lor G)$ $\therefore ((G \rightarrow C) \land G)$ is valid.
12. Show that $\neg \neg L$, $(C \rightarrow \neg L) \rightarrow C$ $\therefore \neg C$ is invalid.
