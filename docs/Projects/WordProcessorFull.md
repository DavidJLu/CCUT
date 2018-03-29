CS300: Homework 5 - Word Processor
=============

![Typewriter](typewriter.jpg)

From Professor Herb Mayer's CS300 course. [External Link](http://web.cecs.pdx.edu/~herb/cs300s07/)

Word Processor Complete Implementation
------------
General Rules: Implement your Homework in C or C++, using any 32-bit or more powerful run-time system. Hand in the complete listing of all source files plus include files, if any, and all inputs with generated outputs. Write your group’s names, the HW number, completion date, and the current PSU term into the header of each source file. If you work in a group of 2 or more, keep in mind that fair work distribution is one important SW Engineering aspect. You need to practice fair work distribution, and group work. This aspect is important in your case, as all group members receive the identical credit for the delivered project.

>Abstract: Implement in C or C++ the Word Processor, specified in HW1. Show that all commands work by running the complete test suite specified in HW1. All previously functioning text processing commands must still work correctly.

Detail: The word processor you implement is an old-fashioned, simple text processing tool that reads unformatted ASCII text input with embedded commands, and outputs formatted text. The output has all commands removed, and is formatted as specified by the commands or by defaults. Characters should be monospaced.

Demonstrate via suitable input texts, that all text processing commands work. The `.ra` and `.co` commands had been implemented before and must still function properly. Hand in all inputs and their corresponding outputs, showing in each case that yet another formatting command works as specified.

Following the emitted output, your word processor dumps additional internal information. This information is for tracking purposes for the implementation team, not meant for the benefit of the user of your word processor. This tracking information includes the following:

\# | Internal Data to be Tracked
:--|:--
1  | Total number of input characters read
2  | Total number of input blanks read
3  | Total number of input cr/lf read
4  | Total number of input tabs read
5  | Total number of input lines read
6  | Total number of unprintable character read
7  | Total number of commands encountered
8  | Total number of distinct commands, i.e. the same command occurring more than once in the input is counted just one time
9  | Total number of words in the input; a word is a contiguous sequence of characters embedded in white space. White space includes blanks, new-lines, the start of file, and of file, and tabs. Also, any combination of these c outs as one white space
10  | Total number of white spaces output. White space is a combinations of blanks, tabs, and newlines, but at least one of those
