CS251 Week 1: Welcome!
=======

![Math Art](math.jpg)

<sub>(Converted from week 1 slides)

Instructor: David Lu
A good textbook: [forall x Calgary Remix](http://forallx.openlogicproject.org/)
Author: PD Magnus, Tim Button, J. Robert Loftis, Aaron Thomas-Bolduc, Richard Zach

#### About Your Instructor:
I'm glad to be back in Changchun and to see everyone here at CCUT again.

Some quick facts about me:
* Born and grew up in the US (mostly in New York)
* Went to college at the [University at Buffalo](https://www.buffalo.edu/), which is located in upstate NY, near Canada.
* Graduated with a BA in Philosophy
* Worked on a PhD in Philosophy at [Syracuse University](https://www.syracuse.edu/) (also located in upstate NY - central), specializing in metaphysics and philosophical methodology
* Taught philosophy courses over 6 years in ethics, metaphysics and epistemology, critical thinking, and formal logic at Syracuse University
* Currently teaching discrete math, introduction to C++, and ethics for computing at Portland State University
* 3rd year participating in the PSU/CCUT partnership program
* One younger brother and one younger sister


CS251 Guest Lectures at CCUT
-----

The central topic of CS251 is formal logic

In this course, we study a language which we can use to express and investigate valid inferences. Formal logic is the study of valid inferences in an abstract fashion, usually in terms of abstract rules. In many ways, it is similar to the study of formal mathematics, which you are familiar with. Logic, like mathematics, is an important field of study because sometimes we need very precise ways to prove that something is or is not the case.

In the preface of Daniel Velleman's excellent book, *How to Prove It: A Structured Approach* he writes:
>‘Students... often have trouble the ﬁrst time that they’re asked to work seriously with mathematical proofs, because they don’t know ‘the rules of the game’. What is expected of you if you are asked to prove something? What distinguishes a correct proof from an incorrect one?

This class is a step toward learning how correct proofs are constructed.


#### Arguments
Logic is in the business of evaluating arguments. We'd like to have a rigorous method for sorting the good arguments from the bad arguments.

An argument is a series of sentences, one of which is a conclusion and the others given as reasons to believe the conclusion. Here's an example:

1. It's raining heavily.
2. If you do not take an umbrella, you'll get soaked.
3. Therefore, you should take an umbrella.

1 and 2 are the premises of this argument and 3 is the conclusion.

We shall specify every argument has one conclusion and zero or more premises. Let's look at some more examples of arguments.

#### Logic and Computer Science
Logic and computer science are closely related in many areas.
* Research into logic that are guided by applications in computer science.
  * Example: Rewriting systems, Combinatory logic, and Abstract interpretation (used in static analysis, compile time optimization, and debugging);
* Fundamental concepts in computer science that are naturally expressible in logical form.
  * Example: Type theory (used in type systems), Formal semantics of programming languages, Hoare logic, and Logic programming;
* Applications of fundamental concepts derived from the theory of computation that cast light on questions of pure logic.
  * Example: Curry-Howard correspondence and Game semantics;
* Tools for logicians considered as applied computer science.
  * Example: Automated theorem proving and Model checking.


#### Exercises
Let's look at some of the exercises in the book and practice translating them into Chinese, identifying the premises and conclusions, and deciding whether they are good or bad arguments.
