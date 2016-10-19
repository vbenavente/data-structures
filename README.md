# Data-Structures  [![Build Status](https://travis-ci.org/vbenavente/data-structures.svg?branch=master)](https://travis-ci.org/vbenavente/data-structures)
- sample code for a number of classic data structures implemented in Python  

## Singly-Linked List  
- this is an implementation of a singly linked list in Python  

## Stack  
- this is an implementation of a simple pancake stack in Python  

## Doubly-Linked List  
- this is an implementation of a doubly linked list in Python  

### Cited Sources:  
  - http://stackoverflow.com/questions/23337471/how-to-properly-assert-that-exception-raises-in-pytest  

## Queue  
- this is an implementation of a queue in Python  
- inherited methods from our doubly linked list  

## Deque
 - this is an implementation of a deque in Python  
 - inherits methods from our doubly linked list  

## Heap
 - this is an implementation of a heap in Python  
 - our implementation is a min heap  
 - we used the builtin Python list  
 - Cris helped us out twice  

## Priority Queue  
 - this is an implementation of a priority queue in Python  

## Graph  
- this is an implementation of a graph in Python  
- this implementation is a directed simple graph  
- Nic helped us with del_edge  

### Cited Sources
  - http://stackoverflow.com/questions/11351032/named-tuple-and-optional-keyword-arguments  

## Graph Traversal  
- implements two new methods on our simple graph  
  - depth-first traversal walks through a data structure by fully exploring it's first selection and then moving on to the next and fully exploring it in turn  
  - breadth-first traversal walks through nodes by spreading out from the initial starting point and visiting every closer node before stepping through to visit their neighbors  

### Cited Sources  
  - https://github.com/welliam/data-structures/blob/traversal/src/adjacency_list.py  
  - Code review in class from Wednesday where we went over the above  

## Graph Weights
- implements edge weights on edges in our graph  

## Binary Search Tree  
- http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html  

## Trie  
- a python implementation of trie  
- an ordered tree data structure that is used to store an ordered set  
- class has insert method that inserts value token into tree  
- class has contains method that checks if token is already present, returns boolean  

### Singly vs. Doubly Linked Lists  
- A Singly Linked-List  
  - easier to implement  
  - takes up less memory  
  - faster to add or delete if you are only concerned with the next node   
- Doubly Linked-List  
  - easy access to both ends of the list  
  - can delete previous node without traversing from head node  

  A singly linked list has a few advantages over a doubly linked list.  Singly linked lists are easier to implement, take up less memory on the host machine, and it is faster to add or delete node from the list.  Doubly linked lists have a few advantages over singly linked lists, such as: easy access to both ends of the list and you can delete a node from anywhere in the list without traversing from the head.  Choosing between these different list types is a complicated question of performance vs memory concerns.  


### resources and collaborations  
- https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/  
- http://stackoverflow.com/questions/10708790/  
- microsoft-asks-singly-list-or-doubly-list-what-are-the-pros-and-cons-of-using  
- http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
