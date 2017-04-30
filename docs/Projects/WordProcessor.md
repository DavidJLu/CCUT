CS300: Homework 1 - Word Processor Specifications
============
![Fountain Pen](pen.jpg)

From Professor Herb Mayer's CS300 course. [External Link](http://web.cecs.pdx.edu/~herb/cs300s07/)

Word Processor Requirements Specification & Test Specification
------------

>**Abstract:** Compose 2 documents, each consisting of a Title Page, a Table of Contents, a Summary Section, and various content Chapters. The first document is a functional specification of all requirements for a word processor you will design, and which you later will implement. The second document is a complete list of tests that you will subject your project to, which will demonstrate that all features work as advertised. You will write all these test cases yourself and run your tool against each of them various times. A specification is a piece of technical writing; it should be short, factual, and to the point. Tables are encouraged, non-necessary prose is discouraged.

#### Detail:
The word processor you design is an old-fashioned, simple, non-proportional text processing tool that reads unformatted ASCII text input with embedded commands, and outputs formatted text. The output has all commands removed and is formatted as specified by the commands or by defaults. The spacing per character is not proportional as a modern word processor would be. Instead, each ASCII character consumes the identical amount of horizontal space of courier typewriter font.

#### Commands:
Word processor commands are embedded in the input text, each introduced by a leading period (AKA dot .) in column 1 of an input line, then followed by a dual-letter command followed sometimes by further parameters that refine the command. No other text is allowed on a command line. If found, trailing text on the command line is ignored silently.

#### Word Processor Required Functions:
1. It has **defaults**. If no formatting command is given, default output format is created.

1. It has notion of a **page**, with min and max line length and min and max lines per page. You need to specify all minima and maxima and default actions for all commands. For page sizes, start with the default of 50 lines per page, and 80 characters per line.

1. It has notion of **column numbers** for a line. Columns span positions 1 though 80, unless modified by explicit command.

1. It formats its output in **left-justified** fashion; i.e. all leftmost characters in each line start in the same column unless modified by explicit command.

1. It formats output by filling each output line with words from the input as far as possible but by default without **right-justification**; i.e. without adding blanks that would place the rightmost character into the last (rightmost) column.

1. It has a command that forces right-justification in addition to the default left-justification of text; right adjustment is not the default

1. It has commands to print **page numbers**, position the page number (left, middle, right) and to start with a specified page number.

1. It has concept of a **paragraph**. A paragraph starts at the beginning of the input text, after any empty line found in the input, or after any formatting command for empty space or a new page. The last line of a paragraph is never right-justified, even when the right-justified command is given.

1. It allows **empty spaces**; i.e. there may be empty lines between the end of one paragraph and the start of the next paragraph.

1. It allows **indentation**: the default position of the left-most column can be changed via a command; it is valid until overridden explicitly; the default is column 1.

1. It allows **temporary indentation** for the first line of a paragraph only.

1. Allows **multiple column output**. The default number of columns is 1.

#### Automation:
For the test specification, include the design requirement that you’ll design a test automaton TA. TA reads input files, produces outputs, and compares these outputs with pre-exiting files that are expected outputs. If a difference is detected, the TA lists this as an error with clear indication where the discrepancy occurred.

Command       | Meaning and Function
:--       |:--
.co #     | Number of columns. Implies .. default .. < >
.in #     | Indent: number of chars next line is indented before first character, may not exceed line length
.la [+/-] | Left adjustment:
.ll #     | Line length: total number of characters on a line, must be > 2, and < 80
.pl #     | Page length: total number of lines on a page, numeric argument needed
.ra [+/-] | Right adjustment:
.sp #     | Spaces: number of empty lines after previous line. May rollover to next page, in which case next page has leading empty lines. If # exceeds page length, a single empty page is printed

#### Input:
Input to the word processor is a stream of ASCII text. In a Unix environment, this is a file named `stdin`. On other operating systems use a text file explicitly named `stdin`. The input file contains the actual text to be formatted as well as embedded commands.

You create a table (Central Table) with all formatting commands, similar to the one shown above. Instead of a central table you can also use a list of paragraphs, explaining each command. This table needs to be short, sorting all commands in alphabetical order. The detailed explanation of defaults, min and max values of each command does not need to be included in the Central Table.

Input:
Here is a sample input snippet, from file `stdin`:

```
.ll 50 –- defines line length to be 50 characters
.pl 50 -- defines page length to be 50 lines
.ra    -- specifies right adjustment, in additional to default left adjustment
This is a sample input text file that will be formatted by right-adjusting, left-adjusting, and by removing all commands from the input. The output file shows paragraphs, such as this one.
.sp    -- defines empty space, default is 1 empty line
.in 5  -- specifies indent but temporary, 1 line, adding 5 character positions
It also allows temporary indentation, which is the same as additional indentation for the first line of a paragraph. All other lines, if any, in such a paragraph start on the leftmost column, which is column # 1 by default.
```

Output:
Here is a sample output snippet, to file `stdout`:

```
  This  is  a  sample  input text  file that will be
  formatted  by right-adjusting, left-adjusting, and
  by  removing  all  commands  from  the  input. The
  output file shows paragraphs, such as this one.

       It  also  allows temporary indentation, which
  is  the  same  as  additional  indentation for the
  first  line  of  a  paragraph. All other lines, if
  any,  in  such  a  paragraph start on the leftmost
  column, which is column # 1 by default.
```

Your Requirements Specification must define for each command, what is the default (i.e. what happens if no command is given), the minimum (which value cannot be reduced), the maximum (which value cannot be exceeded), and the action. Some command turn an action on or off, that is to be communicated via + and – arguments. Note that a line length of 1 is not meaningful, but decide, whether or not you allow it. If you do, the complete output will be a single character on each line. Note that a line longer than what fits horizontally onto a page is also not meaningful. Decide what to do, if that logic is violated. Your test Specification needs to state for each command, how its proper functioning is validated, which input, and which resulting output is measured.

\# | What has to be specified by you for each formatting command
:--|:--
1  | Name of command, e.g. `.sp` for space
2  | Action = semantics, if no argument is given
3  | Action if argument is given, e.g. `.sp 10`
4  | Format for all arguments: e.g. empty, +, -, a number, other
5  | Min value of argument
6  | Document what happens, if min value is violated. E.g. `.sp -5`
7  | Max value of argument. E.g. `.sp 99999999` -- probably invalid value
8  | What happens, if max value is violated

The detailed explanation of each command should proceed in the same order as the commands specified in the central table.

Note that all information in the Requirements Specification and the User Manual is logically equivalent. However, the target audience for the Spec is the implementer of the word processor, while the target audience for the User Manual is the user of the implemented tool.
