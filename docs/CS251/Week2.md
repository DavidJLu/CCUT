# CS251 at CCUT Week 2: Propositional Logic
4/24/17

![Open Logic Text](openlogic.png)

<sub>Image from ["AN ACTUAL TEXTBOOK, AND: PHOTOS!"](http://openlogicproject.org/2016/03/12/an-actual-textbook-and-photos/) by [Richard Zach](http://openlogicproject.org/author/rzach/) is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)

*Sets, Logic, Computation* is an open source textbook which you can download at the [Open Logic Project](http://openlogicproject.org/download/)

--------

Last week we briefly reviewed the vocabulary and syntax of propositional logic (PL), and we discussed some motivations for studying it.

This week, we will think about the semantics (or meanings) of the PL, and practice a bit of translation between English and PL.

The study of logic really comes down to the study of valid arguments. So we will also begin to look at what an argument is and what makes an argument valid this week.

Outline: <a id="index"></a>
  * [Semantics](#semantics)
  * [Atomic Sentences](#atom)
  * [Compound Sentences](#compound)
    * [Not](#not)
    * [And](#and)
    * [Or](#or)
    * [Conditional](#conditional)
  * [Exercises](#exercises)


### Semantics and Principle of Bivalence <a id="semantics"></a>
In studying languages, we often distinguish the syntax from the semantics of the language.

Recall the syntax refers to the rules that allow us to form sentences of the language.
Recall that the syntax for PL is as follows:

  1. Any atomic sentence P is well-formed
  1. For any well-formed sentence $p$, $\neg p$ is well-formed
  1. For any well-formed sentences $p$ and $q$, $p \land q$, $p \lor q$, $p \rightarrow q$, and $p \equiv q$ are all well-formed.

So the formula $A \rightarrow (B \lor C)$ is well-formed.

On the other hand, the semantics of a language refers to the meanings.

In the propositional logic, the meaning of a sentence is its truth conditions. For this class, we will consider just two truth values: true and false. And we will assume the principle of bivalance

>Principle of Bivalence: Each sentence of our language must be either true or false, not both, not neither.

So we will assume that each sentence is either true or false.

[Back to Top](#index)

## Atomic Sentences <a id="atom"></a>

CCUT is in Changchun.

This can be represented by P.

### Compound Sentences <a id="compound"></a>
Here are the truth tables for our logical connectives:

|p |q |p $\land$ q| p $\lor$ q| $\neg$p | p $\rightarrow$ q |
|:-|:-|:--|:--|:--|:-- |
|T |T |T |T |F |T |
|T |F |F |T |F |F |
|F |T |F |T |T |T |
|F |F |F |F |T |T |

These truth tables give the semantics for the logical connectives. Notice that these are lower case $p$ and $q$, indicating that these are sentence schema (or sentence variables).

#### Pattern Matching
So the compound sentence $A \rightarrow (B \lor C)$ has the form $p \rightarrow q$.

This type of pattern matching is important to understand.

[Back to Top](#index)

## "Not" <a id="not"></a>
**Not** or *negation* is a *unary* connective. This means that it "connects" only to one sentence.

If $p$ is a well-formed sentence, then we can attach **not** to it: $\neg p$

The semantics for **not** are given by the following truth table:

|p | $\neg p$|
| :--|:--|
|T | F |
|F | T|

As we can see, negation gives us the opposite truth value of the original sentence.

>"The Earth is not the center of the universe"

How do we translate this and what is the truth value?


<br>

Let R mean "The widget is replaceable."
1. The widget can be replaced.
1. The widget is irreplaceable.
1. The widget is not irreplaceable.

How should we translate these?

But be careful!
  1. Jane is happy.
  1. Jane is unhappy.

  We might translate 1 to $H$, but 2 shouldn't be translated as $\neg H$. It may be that Jane is neither happy nor unhappy. The point here is that "Jane is not happy" does not necessarily mean the same thing as "Jane is unhappy."

[Back to Top](#index)

## "And" and "Conjunction" <a id="and"></a>
>I went to the party and I had fun.

|p |q |p $\land$ q|
|:-|:-|:--|
|T |T |T |
|T |F |F |
|F |T |F |
|F |F |F |

Examples
  1. Barbara is athletic and energetic.
  1. Barbara and Adam are both athletic.
  1. Although Barbara is energetic, she is not athletic.
  1. Adam is athletic, but Barbara is more athletic than him.

[Back to Top](#index)

## "Or" and "Disjunction" <a id="or"></a>
>I go to the party or I study.

|p |q |p $\lor$ q|
|:-|:-|:--|
|T |T |T |
|T |F |T |
|F |T |T |
|F |F |F |

Or is *inclusive*.

Examples
  1. Either Faye will play videogames, or she will watch
  movies.
  1. Either Faye or Ali will play videogames with me.
  1. Either you will not have soup, or you will not have salad.
  1. You will have neither soup nor salad.
  1. You get either soup or salad, but not both.

[Back to Top](#index)

## "If... then..." <a id="conditional"></a>
>If I goto the party, then I will not study.

|p |q |p $\rightarrow$ q|
|:-|:-|:--|
|T |T |T |
|T |F |F |
|F |T |T |
|F |F |T |

Examples
  1. If Jean is in Paris, then Jean is in France.

  1. Jean is in France only if Jean is in Paris.

  1. For Jean to be in Paris, it is necessary that Jean be in France.

  1. It is a necessary condition on Jean’s being in Paris that she
  be in France.

  1. For Jean to be in France, it is sufficient that Jean be in Paris.

  1. It is a sufficient condition on Jean’s being in France that she be in Paris


### Do you understand the conditional?
**Puzzle**: Each card has a letter (consonant or vowel) on one side, and a number (odd or even) on the other.

**Rule**: If there's a vowel on one side of the card, there is always an odd number on the other.

**Challenge**: How many of the pictured cards must you turn over to see if any break this rule?
![cards](cards.jpg)

[Back to Top](#index)
<br>

----------------------------
# Exercises <a id="exercises"></a>
Translations:
  1. Mary is in Barcelona.
  1. Those fruits are apples or they are not.
  1. Those fruits are neither apples nor oranges.
  1. If Professor Plum was murdered, then either Colonel Mustard or Mrs. White did it.
  1. If you didn’t grow up speaking English it is difficult to understand many jokes made in English but, if you watch enough television, you can learn many of those jokes.

[Answers](#answers)
[Back to Top](#index)

<br>
-------------



&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;

# Answers

[Back to Exercises](#exercises)
<a class="anchor" id="answers"></a>

  1. $M$
    $M$ is the atomic proposition "Mary is in Barcelona."
  --------  
  2. $A \lor \neg A$
    $A$ - "Those fruits are apples."
-----
  3. $\neg (A \lor O)$
    $A$ - "Those fruits are apples."
    $O$ - "Those fruits are oranges."
---------

  4. $P \rightarrow (M \lor W)$
  $P$ - "Professor Plum was murdered."
  $M$ - "Colonel Mustard did it."
  $W$ - "Mrs. White did it."
  ---------

  5. $(\neg G \rightarrow J) \land (W \rightarrow L)$
  $G$ - "You grew up speaking English."
  $J$ - "It is difficult to understand many jokes made in English."
  $W$ - "You watched enough TV."
  $L$ - "You can learn many English jokes."
