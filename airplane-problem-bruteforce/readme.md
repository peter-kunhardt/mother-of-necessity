# Brute Forcing the Airplane Problem

A common algorithmic thinking interview question asks the candidate to consider:
- An airplane with 100 seats
- Passengers line up at random with assigned seats
- There is a glitch at the gate and the first passenger is assigned to a random seat
- All subsequent passengers sit in their own seat if it is empty, and in a random free seat if their own is taken

**What is the likelihood that the last passenger to board will be seated in their own seat?**

The somewhat counterintuitive answer is 50%. You can model every passenger with a recursive function that concludes in one of two conditions: 
- The passenger's seat is taken and they randomly sit in passenger **1's** seat, resolving the problem and letting all other passengers board normally
- The passenger's seat is taken and they randomly sit in passenger **100's** seat, meaning it will be taken when passenger 100 gets there.

In all other cases the function continues until all passengers seats are resolved. If the exit conditions of the function are equally likely
at each step, (and they are) 

## Yeah but who needs abstract thinking when you can just prove it?

This is one of those problems in probability where some folk just won't believe you until you put it in front of them. 

Stubborn as I am, I couldn't let it lie, and wrote this script to win an argument on the internet 🤓

This python applet generates randomized simulations of the problem statement and return details on how seat distributions came out, 
runs the simulation x50,000, and prints a summary of aggregate results to the console.
