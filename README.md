# Hopscotch
A simple esoteric programming language.
# Overview
Hopscotch programs are made of the commands `+><^/\*?@_` and integer literals.  The commands are chained linearly, but integer literals and the `?` can cause the intruction pointer to jump.
# Memory
Hopscotch has a stack of theoreticly unlimited length.  Additionally, it has a register.  Each command is passed the value on the regester, and the value it return is placed on a regester.  When the code jumps, the register may be affected.  Hopscotch programs are executed according to an instruction pointer, which is incremented after each command, and can be further modified by certian commands.
# Code
All characters exept `+><^/\*?@_0123456789-` are ignored.  
Each command is one token long.  Each of `+><^/\*?@_` is a token individually, and successive `0123456789-` are grouped into a single token.  This token is interpreted as a single integer.  Sequences such as `123-456` are illgal, as `123-456` is not a isngle integer.  Sequential integers must be seperated with `_` or annother command.  
Code is executed one command at a time, beginning eith the first command and terminating if the instruction pointer points beyond or before the code.
# Commands
There are ten commands and integer literals in Hopscotch
## `+`
`+` pops the top two items off the stack and then places the sum on the regester.
## `>`
`>` takes the value on the regester and pushes it on the stack, leaving it unchanged.
## `<`
`<` pops the top value on the stack and sets the regester to it.
## `^`
`^` reads the top value of the stack, without removing it, and places that value on the register.
## `/`
`/` writes the ascii character represented by the value on the regester to std out, leaving the regester unchanged.
## `\`
`\` reads one character from stdin and writes that value to the regester
## `*`
`*` pops two values from the stack and sets the regester to the product.
## `?`
`?` If the value in the regester is set to a non-zero number, then the instruction pointer is incremented by one (in addition to the normal one).  Regardless, the regester remains unchanged.
## `@`
`@` rotates the top _n_ values of the stack, where _n_ is the value in the regester. That is, pops the _nth_ item on the stack, and pushes it to the top.  The regester remains unchanged
## `_`
`_` is a NOP.  No action is taken and the regester is unchanged.
## Integer literals.
An integer literal is a relative jump.  The normal increment of one of the instruction pointer is replaced by an increment by the integer.  If the token immediatly before the desination of a jump is an integer literal, then the regester is set to that value.

# Computational Class
I belive that Hopscotch is Turing-Complete, as I belive that BrainF ck can be implemented. There is no formal proof.

# Helpful hints
To represent data, `3_nc` works, where `n` is an integer literal to have the regester set to it as command `c` is executed.
