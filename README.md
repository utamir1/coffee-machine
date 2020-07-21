# coffee-machine
OOP Coffee Machine (Finite-state machine)

A logic simulator of an FSM coffee machine. The machine accepts 5 states: 
* buy coffee (if a user wants to buy some coffee)
* refill (if it is time to fill out all the supplies for the coffee machine)
* take (if it is time to take out the money from the coffee machine)
* remaining (output of the resources that the coffee machine has)
* exit (turning the coffee machine off - machine running state is changed to False)

User can choose between 3 types of coffee. each coffee requires different resources:
* For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
* For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
* And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.

