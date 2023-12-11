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

