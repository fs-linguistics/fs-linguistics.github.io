 
# Haskell 



Prereqs: Install GHC

Make sure you can run ghci in your terminal. 


# Writing basic porgrams in haskell. 

We are not starting with hello world because i'm afraid it will slightly confuse youbecause you have to understand the monad and that might make you cry. 


But, that will not be a proble because we have the ghci.


So type in your ghci

```
  1 + 1 
```


Hooray, it should know how to do basic math

Use ghci as an alteranitve to print statements until we learn about how to print


You can also define your functions in there, but it might be easier to just open a separate file and type your definitions there


# Our first function

```haskell
sumOfTwo :: Int -> Int -> Int
sumOfTwo x y = x + y 
```


Now type in ghci

```
  sumOfTwo 5 9
```

Or any two numbers you like

Congrats you made your first program


Small exercise: make similar function for multiplications
make another one for string concatenation (hint change the type signature), and string concat is `++`
  
# What is a functional language

Variable are not allowed to change. Everything you write can bee though of as an equation.

For instance, the usual thing you see in imperative languages like `x = x + 1` is bad, because we can 
cancel those xs and we get `0 = 1` and our head exploads. 

You might be wondering how it's even possible write like anything? Surely you can't make a programming language where you can only set a variable once. And how do you even do loops?

If you are familiar with some basic theory of computation, you should be familiar with the idea of a turing machine. 

The details arent' important, but basically a turing machine is "every computer". (almost) any programming language is essentially a turing machine, but with slightly different syntax.
But there is something very important about turing machines, and anyother programming language, is that they can loop. This is like a while True in python without any break.

if haskell is truly a programming language, then it should be loop infinitely. How do we do that?

The answer is recursion.

# Basic recursion functions

Well, I guesss we are starting with everyone's favorite recrusion thing.


```
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2) 
```


wow that looks just like math. This is because the people that invented haskell were nerds, and wanted things to look verymath like. 
This is our first example of pattern matching. Basically, you can sort of view it as a bunch of if statements. It first checks the base cases. 
Then when it is unable to find a matching case, it will go into the last case, which binds the `n` variable to a 





