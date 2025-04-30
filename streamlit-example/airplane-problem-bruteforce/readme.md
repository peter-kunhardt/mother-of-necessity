# Brute Forcing the Airplane Problem

A common algorithmic thinking interview question asks the candidate to consider:
- An airplane with 100 seats
- Passengers line up at random with assigned seats
- There is a glitch at the gate and the first passenger is assigned to a random seat
- All subsequent passengers sit in their own seat if it is empty, and in a random free seat if their own is taken

**What is the likelihood that the last passenger to board will be seated in their own seat?**

The somewhat counterintuitive answer is 50%. You can model every passenger after the first with a recursive function that concludes in one of two conditions: 
- the passenger randomly sits in passenger 1's seat, resolving the problem and letting all other passengers board normally
- The passenger randomly sits in passenger 100's seat, meaning it will be taken when passenger 100 gets there.

In all other cases the function continues until all passengers seats are resolved. If the exit conditions of the function are equally likely at each step, 
(and they are) 

## Yeah but who needs abstract thinking when you can just prove it?

This is one of those problems in probability where some folk just won't believe you until you put it in front of them. 
This python applet can generate randomized simulations of the problem statement and return details on how seat distributions came out, 
runs the simulation 5000x, and returns a summary of aggregate results.
