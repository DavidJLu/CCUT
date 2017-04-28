CS201: Homework #3 - Decryption
=======

![Encrypted](encrypted.jpg)

Decryption Algorithm
--------

For each student we have encrypted a file containing a secret message. Your task is to create a program to decrypt the file and discover the secret message.

We are using a different encryption algorithm for each student so each student will create a unique decryption program. The encryption / decryption algorithm is based on the first 3 letters of your last name.

The Decryption Algorithm
In this assignment, you are to implement the decryption algorithm associated with your username. The key to your decryption algorithm is the first three letters of your last name. We are getting your name from the PSU registration system. [ Vu, Hanh $\rightarrow$ vuh ]

There are 3 stages to the decryption scheme. The first letter of your key determines the first stage. The second letter of your key determines the second stage. The third letter of your key determines the third stage.

###### First stage

For every 4 bytes of the file `<c0,c1,c2,c3>`, implement the following based on the first letter of your key:
'a' to ‘d’: Swap bytes `c0` and `c3`.
‘e’ to ‘h’: Swap bytes `c1` and `c2`.
‘i’ to ‘l’: Swap bytes `c0` and `c2`.
‘m’ to ‘p’: Swap bytes `c1` and `c3`.
‘q’ to ‘t’: Swap bytes `c2` and `c3`.
‘u’ to ‘z’: Swap bytes `c0` and `c1`.

###### Second stage
For every byte of the file with bits `<b7,b6,b5,b4,b3,b2,b1,b0>`, implement the following based on the second letter
of your key:
‘a’ to ‘d’: Swap bits `b7` and `b1`, Swap bits `b6` and `b0`.
‘e’ to ‘h’: Swap bits `b5` and `b3`, Swap bits `b4` and `b2`.
‘i’ to ‘l’: Swap bits `b7` and `b3`, Swap bits `b6` and `b2`.
‘m’ to ‘p’: Swap bits `b5` and `b1`, Swap bits `b4` and `b0`.
‘q’ to ‘t’: Swap bits `b7` and `b5`, Swap bits `b6` and `b4`.
‘u’ to ‘z’: Swap bits `b3` and `b1`, Swap bits `b2` and `b0`.

###### Third stage
For every 4 bytes of the file <c0,c1,c2,c3>, implement the following based on the third letter of your key, <k3>:
‘a’ to ‘d’: `XOR` bytes `c0` and `c3` with `k3`.
‘e’ to ‘h’: `XOR` bytes `c1` and `c2` with `k3`.
‘i’ to ‘l’: `XOR` bytes `c0` and `c2` with `k3`.
‘m’ to ‘p’: `XOR` bytes `c1` and `c3` with `k3`.
‘q’ to ‘t’: `XOR` bytes `c2` and `c3` with `k3`.
‘u’ to ‘z’: `XOR` bytes `c1` and `c0` with `k3`.
