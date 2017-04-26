# CS251 at CCUT Week 3: Arguments in Propositional Logic
4/26/17

![keyboard](keyboard.jpg)

Outline: <a id="index"></a>
  * [Arguments and Validity](#validity)
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

### Exercises:
Identify the conclusion of these arguments.

1. It is sunny. So I should take my sunglasses.

2. It must have been sunny. I did wear my sunglasses, after all.

3. No one but you has had their hands in the cookie-jar. And the scene of the crime is littered with cookie-crumbs. You’re the culprit!

4. Miss Scarlett and Professor Plum were in the study at the time of the murder. Reverend Green had the candlestick in the ballroom, and we know that there is no blood on his hands. Hence Colonel Mustard did it in the kitchen with the lead-piping. Recall, after all, that the gun had not been fired.

## Validity
We define validity to be a property of an argument.

> An argument is valid if and only if it is impossible for the premises to be true while the conclusion false.

We can put this another way: `An argument is valid if and only if the truth of the premises guarantees the truth of the conclusion.`

And a third way: `An argument is valid if and only if whenever the premises are true, the conclusion is also true.`

These three definitions say the same thing.

### Exercises
Which of the following arguments are valid? Which are invalid?

1.
  >1. Socrates is a man.
  >2. All men are carrots.
  >$\therefore$ Socrates is a carrot.

2.  
  >1. Abe Lincoln was either born in Illinois or he was once president.
  >2. Abe Lincoln was never president.
  >$\therefore$ Abe Lincoln was born in Illinois.

3.  
  >1. If I pull the trigger, Abe Lincoln will die.
  >2. I do not pull the trigger.
  >$\therefore$ Abe Lincoln will not die.

4.
  >1. Abe Lincoln was either from France or from Luxemborg.
  >2. Abe Lincoln was not from Luxemborg.
  >$\therefore$ Abe Lincoln was from France.

5.  
  >1. If the world were to end today, then I would not need to get up tomorrow morning.
  >2. I will need to get up tomorrow morning.
  >$\therefore$ The world will not end today.

6.
  >1. Joe is now 19 years old.
  >2. Joe is now 87 years old.
  >$\therefore$ Bob is now 20 years old.

[Back to the Top](#index)

# Methods <a id="methods"></a>
Recall that one main reason to study logic is to be more precise. So can we be more precise than reading English arguments and trying to decide whether they are valid or not?

Yes, formal logic attempts to provide precise methods for determining whether an argument is valid or not. In this section, we will look at two methods for determining validity. These methods can also be used to determine some other properties we are interested in.

The two methods fall into the categories of truth tables and natural deduction. There are other methods (axiomatic logic) but these two are easier to use and understand.

[Back to the Top](#index)

## Truth Tables <a id="truthtables"></a>

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
