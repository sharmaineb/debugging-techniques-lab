# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

Issue 1: TypeError - 'topping' is an invalid keyword argument for PizzaTopping

- Expected vs. Actual Output:
  - Expected Output: Successful submission of the pizza order without any errors.
  - Actual Output: Encountered a TypeError: 'topping' is an invalid keyword argument for PizzaTopping.

- Stack Trace:
  - The stack trace indicated a TypeError with the message 'topping' is an invalid keyword argument for PizzaTopping.

- Technique Used:
  - Trace Backward:
    - Identified the error in the for loop in the pizza_order_submit route (lines 78-79).
    - Realized that the argument name topping in PizzaTopping(topping=topping_str) was incorrect.

- Assumptions:
  - Assumed that the line pizza.toppings.append(PizzaTopping(topping=topping_str)) was correct.
  - Thought that the variable topping is the correct argument for creating a new instance of PizzaTopping.

- Solution:
 - for topping_str in ToppingType:
        # changed the argument name to 'topping_type'
        pizza.toppings.append(PizzaTopping(topping_type=topping_str))

Issue 2: BuildError - Could not build URL for endpoint '/'. Did you mean 'fulfill_order' instead?

- Expected vs. Actual Output:
  - Expected Output: Successful redirection to the homepage after submitting a pizza order.
  - Actual Output: Encountered a BuildError: Could not build URL for endpoint '/'. Did you mean 'fulfill_order' instead?

- Stack Trace:
  - The stack trace indicated a BuildError with the message: Could not build URL for endpoint '/'. Did you mean 'fulfill_order' instead?

- Technique Used:
  - Trace Forward:
    - Focused on the redirection line in the pizza_order_submit route (line 84).
    - Checked if there was an issue with the url_for('/').

- Debugging Steps:
  1. Trace Forward:
     - Focused on the redirection line in the pizza_order_submit route (line 84).
     - Checked if there was an issue with the url_for('/').

  2. Divide & Conquer:
     - Simplified the redirection line to return redirect('/') instead of return redirect(url_for('/')).

- Assumptions:
  - Assumed that url_for('/') would correctly resolve to the root URL for redirection.

- Solution:
  - return redirect('/')

## Exercise 2

[[Your answer goes here!]]

## Exercise 3

[[Your answer goes here!]]
