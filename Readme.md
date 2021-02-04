Liquid Types Tutorial
-------------------------

This project implements the Refinement Types Tutorial (https://arxiv.org/abs/2010.07763) by
 Ranjit Jhala and Niki Vazou.


Branch Structure
---------------------
v0: LiquidTerms and Satisfiability via Z3


Folder Structure
----------------

spryte          - compiler
    core        - ASTs
    vc          - Verification Conditions
tests           - tests for all the sections


Implementation Decisions
------------------------

I believe Python is a more suitable language to implement an education-oriented compiler.
It allows a broad audience who is not an expert in either Functional Programming or Compilers
to follow the code.

Another reason for choosing Python is the wonderful and sturdy Z3 bindings.


LiquidTerms correspond to the predicate syntax in the tutorial. I have simplified it so both uninterpreted and interpreted/native/builtin functions have the same structure (LiquidApp).

In v0, LiquidTerms are not type checked. We'll assume they are always correct for now.