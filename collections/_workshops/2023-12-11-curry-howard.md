---
layout: single
date: 2023-12-11
title: "Curry Howard isomorphism"
category: workshop
---



Start off by doing some intution on haskell. 

I'm going to steal stuff from [this page](https://en.wikibooks.org/wiki/Haskell/Higher-order_functions)


We have a function called `id` the definiton is



What is the type signature


```haskell
  id x = x
```



What type signature

```haskell
  const x y = x
```

Type Signature???

```haskell
   application f x = f x
```

Type???
```haskell
  composition f g x = f (g x) 
```


Ok, now that that is done, try to rewrite all these using only lambdas. 



Now the hint here is that you will use type variables. Now why are they called type variables? Well, I guess it's obvious that they are variabless.



but to give you a hint, haskell actually puts a forall in frot of these types. 


That's right, you can view the arrow is implication. 

*Exercise* Prove all your types are correct. 
 
Use natural deduction. 


If you did everything correctly, you should see that you need only 3 rules.

1. Implication Introduction
2. Introduction Elimination
3. Hypothesis Assumption

  


OK now, lets go over a quick thing about lambda calulus. 
 
According to wikipedia, 

The set of lambda expressions, Λ, can be defined inductively:

If x is a variable, then x ∈ Λ.
If x is a variable and M ∈ Λ, then (λx.M) ∈ Λ.
If M, N ∈ Λ, then (M N) ∈ Λ.



Lets rewrite the expressions in lambda expressions, which I should have mentioned last time. 

```haskell
  id = \x -> x
  const = \x -> \y -> x
  application = \f -> \x -> f x
  composition = \f -> \g -> \x -> f (g x)
```

These all start with the backslash which stands for lambda abstraction. In id, we then add a variable and we are done. In const, we start to add another lamda expression. In application, we do the same, but then we add a some lambda application. Similarly for compisiton, we do the same thing.


Now notice that when you do did your proof, you only had 3 rules that you used, and simialrly, lambda calculus has 3 words that you used.

this is because natural deduction *is* lambda calculus. 

Variable are Variables
Implication introduction is function abstraction
Implication elimination is function application



