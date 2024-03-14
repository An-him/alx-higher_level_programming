# 0x02-python-import_modules
### Modules are files that include Python definitions and statements
### Namespaces: Is a place where variables are stored
#### When a module is defined this is where it is stored, called to be accessed by other programs
#### Modules are written as the C equivalent of functions and invoking is done by >>>import __name__
#### import fib2 from fibo: this makes only a particular the selected modname available to a user
#### import fibo *: like the asterix wildcard in bash this selects all the functions save the ones whose name begins with _[underscore]
#### import fibo as fibonacci: this makes only a certain module available only as fibonacci
#### from fibo, import fib, fib2: makes fib and fib2 only

To execute the module name as a script append the following
if __name__ == "__main__"
   import sys
   func(int(sys,argv[1]))