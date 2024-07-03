# Dreamcoder

[Dreamcoder](https://github.com/ellisk42/ec) is an AI program that solves problems by creating a function to solve a task. 

It is written in Python and OCaml and wrtites its programs in a dialect of Lisp. Here's an [example program](https://github.com/ellisk42/ec/blob/master/PBE_Strings_Track/phone.sl) it created:

```lisp
(set-logic SLIA)
 
(synth-fun f ((name String)) String
    ((Start String (ntString))
     (ntString String (name " "
                       (str.++ ntString ntString)
                       (str.replace ntString ntString ntString)
                       (str.at ntString ntInt)
                       (int.to.str ntInt)
                       (str.substr ntString ntInt ntInt)))
      (ntInt Int (0 1 2 3 4 5
                  (+ ntInt ntInt)
                  (- ntInt ntInt)
                  (str.len ntString)
                  (str.to.int ntString)
                  (str.indexof ntString ntString ntInt)))
      (ntBool Bool (true false
                    (str.prefixof ntString ntString)
                    (str.suffixof ntString ntString)
                    (str.contains ntString ntString)))))


(declare-var name String)

(constraint (= (f "938-242-504") "938"))
(constraint (= (f "308-916-545") "308"))
(constraint (= (f "623-599-749") "623"))
(constraint (= (f "981-424-843") "981"))
(constraint (= (f "118-980-214") "118"))
(constraint (= (f "244-655-094") "244"))

(check-synth)
```

AIUI the contraints are the bottom are the example tasks it is trying to solve, and `f` is the function it produces to solve them.

