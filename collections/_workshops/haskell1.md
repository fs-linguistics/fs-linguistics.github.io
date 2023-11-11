 
# Haskell 



Prereqs: Install GHC

Make sure you can run ghci in your terminal. 


# Writing basic porgrams in haskell. 

We are not starting with hello world because i'm afraid it will slightly confuse youbecause you have to understand the monad and that might make you cry. 


But, that will not be a proble because we have the ghci.


So type in your ghci

```haskell
  1 + 1 
```


Hooray, it should know how to do basic math

Use ghci as an alteranitve to print statements until we learn about how to print


You can also define your functions in there, but it might be easier to just open a separate file and type your definitions there, which is what we will now do

# Our first function

```haskell
sumOfTwo :: Int -> Int -> Int
sumOfTwo x y = x + y 
```

Save this to a file, like `myhaskellfile.hs` 


Now when you open ghci, do `ghci myhaskellfile.hs`

and type in
```haskell
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


```haskell
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2) 
``` 

wow that looks just like math. This is because the people that invented haskell were nerds, and wanted things to look verymath like. 
This is our first example of pattern matching. Basically, you can sort of view it as a bunch of if statements. It first checks the base cases. 
Then when it is unable to find a matching case, it will go into the last case, which binds the `n` variable to a variale, and then we go into the recursive case


This is already enough to write some basic programs in haskell

Exercise: write sum up to n (though I guess you could cheat and use the formuula) and product up to n. 

**Harder Question**: define a function called `plusOne` that just adds one to your number (you can use `+` and ou don't need recurseion)). Can you make a function `myPlus` that adds two numbers using your `plusOne` (you need a minus for recursion) Now make `myTimes` using this `myPlus`. How about exponentation?

# Working with lists

Because we are smart or something, we are going to jump directly into lists, which are our version of arrays.

Review: what is a linked list? You might remember it as a slower version of arrays that nobody uses. That's why Haskell only uses linked lists by default, screw you imperative normies.


Anyway, the real reason is because linked lists can be define mathemetically using induction. 


A linked list is either:


- empty 
- something in the first element, and a different list after that


You can kind of view empty as a null pointer, however it's better not to think about pointers as they belong to the evil world of C++.
 
For now, we will ignore polymorphism, and just do numbers

The syntax is more or less how you expect. 


```haskell
  []
```

The empty list

```haskell
  [1, 2, 3]
```


Somestuff in it


```haskell
  [1, 2, 3] ++ [5, 6, 7]
```

This is concatenation
 
Note the recursive method of definiton, this is because the array notation mentioned above is the note the "real" notation, its just synactic sugar that gets compileed to the recursive natation



```haskell
  1 : 2 : 3 : []
```

Type that into ghci

Try figuring out where the parenthesis go (hint, it's right associative, if you can figure out what that means)
 
```haskell
lengthOfList :: [Int] -> Int
lengthOfList [] = 0
lengthOfList (_:xs) = 1 + lengthOfList xs 
``` 

Just like how we previously matched our base cases using the number 0 and 1, we want to match it with the structure of a list. 

Note that since we have our recrusive structure, we can use "induction" by covering our two cases, either it being nothing, or a something plus another list. 


also note that the underscore is a black hole of death, which means that it's a variable that we don't care about 


# Thinking about recursion

Sometimes, if you don't know how to write a recursive function, you should write a bunch of base cases. 

For example, let's make a function that adds 1 to everything in the list

The first base case is easy


```haskell
add1 :: [Int] -> [Int]
lengthOfList [] = []
``` 


Ok, now the next case is the recursive case. But what if recursion is hard and I can't think of the solution?
One techinque is to just write a bunch of base cases until the answer comes to you 

```haskell
add1 :: [Int] -> [Int]
add1 [] = []
add1 (x1:[]) = (x + 1) : [] -- aka [x + 1]
add1 (x2:x1:[]) = (x2 + 1) : (x1 + 1) : [] -- aka [x2 + 1, x1 + 1]
add1 (x3:x2:x1:[]) = (x3 + 1) : (x2 + 1) : (x1 + 1) :  [] -- aka [x1 + 1, x2 + 1]
``` 

wow wow, you realize there is some part that uses an older part. Maybe that could be part of the recursion. 


```haskell
add1 :: [Int] -> [Int]
add1 [] = []
add1 (x1:[]) = (x1 + 1) : add1 [] -- aka [x1 + 1]
add1 (x2:x1:[]) = (x2 + 1) : add1 (x1 : []) -- aka [x2 + 1, x1 + 1]
add1 (x3:x2:x1:[]) = (x3 + 1) : add1 (x2 : x1 : []) -- aka [x3 + 1, x2 + 1, x1 + 1]
``` 

Ok, now we see that we have terms that match on both sides. This means everytime we copy and past something on the left onto the right in each case. For example, in the line right after the base case, we take x1, and copy it to the right before the `+ 1`. Then in the next line, we take `x2` and copy it to basically the same position right before the `+ 1` and then we do it with `x3` with basically the same thing, it's before the `+ 1`.  Then we notice the other *term* is done the same, `[]` is copied right after the `add1` on te first line, then we have `x1:[]` which gets copy and pasted right after `add1` onto, and then we finally have `x2:x1:[]` which gets copy and pasted right after the `add1`. 

That means we can replace them with variables!


```haskell
add1 :: [Int] -> [Int]
add1 [] = []
add1 (x:rest) = (x + 1) : add1 rest 
``` 


Exercise: make function that sums up all the values of a list, then make something that multiplise all the values together


**Exercise:** make a function `drop` that takes an an int `n` and a list that removes the firt `n` elements of the list and returns the rest. 

**Exercise:** make a function `take` that takes an an int `n` and a list that returns the first `n` elements of the list. 
    

```haskell
lengthOfList :: [Int] -> Int
lengthOfList [] = 0
lengthOfList (_:xs) = 1 + lengthOfList xs 
``` 
  

# Strings

Strings are just a list of characters. 

Type into ghci

```haskell
 ['s', 'u','g','m','a']
```

And it will show you that it is just a string. (It's like java where single quotes are charactres and double quotes are strings)

Exercise: Do the Java love-hate thing in haskell. 


Hint:  You can match recursively

```haskell
  important :: String -> String
  important ('j' :'o' :'h' :'n') = "You are cool."
  important other = "I hate you"
```

What does this do?

# Conditinoal

For our last thing we are leaning about conditionals

Like java/c++, whatever, conditinoals work with the two things booleanvalues, True, and False (they are capital)

The syntax looks like this

```haskell
if condition then value_if_true else value_if_false 
```

``` haskell
describeNumber :: Int -> String
describeNumber n = 
  if n > 0 
  then "Positive" 
  else if n == 0 
       then "Zero" 
       else "Negative"   
```


Exercise: something interesting about if is that the if statement is actually not needed. Make your own version of the if statement as a function. 


Challenge: make a generic replace method where you don't replace hate with love, but any arbitrary phrase. 

**Hint**: use the `take` and `drop` method that I told you to implement earlier. 

Ok that's probably enough and I'll probably do the rest later


If you thought that this was a terrible tutorial, please send in a pull request fixing it or lower your standards. 
  
