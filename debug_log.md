# Debug Log

**Explain how you used the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

**Issue 1: TypeError - 'topping' is an invalid keyword argument for PizzaTopping**

- **Expected vs. Actual Output:**
  - Expected: Successful pizza order submission.
  - Actual: TypeError: 'topping' is an invalid keyword argument for PizzaTopping.
- **Stack Trace:**
  - TypeError: 'topping' is an invalid keyword argument for PizzaTopping.
- **Technique:**
  - Trace Backward:
    - Identified the error in the for loop in the pizza_order_submit route (lines 78-79).
    - Found the incorrect argument name topping in PizzaTopping(topping=topping_str).
- **Assumptions:**
  - Assumed 'topping' was the correct argument for creating a PizzaTopping instance.
- **Solution:**
  - Changed the argument name to 'topping_type': `PizzaTopping(topping_type=topping_str)`.

**Issue 2: BuildError - Could not build URL for endpoint '/'. Did you mean 'fulfill_order' instead?**
- **Expected vs. Actual Output:**
  - Expected: Redirect to homepage after pizza order submission.
  - Actual: BuildError: Could not build URL for endpoint '/'.
- **Stack Trace:**
  - BuildError: Could not build URL for endpoint '/'.
- **Technique:**
  - Trace Forward:
    - Focused on the redirection line in the pizza_order_submit route (line 84).
    - Checked url_for('/') for issues.
- **Assumptions:**
  - Assumed url_for('/') would correctly resolve to the root URL.
- **Solution:**
  - Changed to `return redirect(url_for('home'))`.
- **Solutions to other errors:**
  - added `db.session.commit()` to store pizza orders.

## Exercise 2

**Issue 1: KeyError - 'name' not found in result_json**

- **Expected vs. Actual Output:**
  - Expected: Display weather info for the city.
  - Actual: KeyError: 'name' not found in result_json.
- **Stack Trace:**
  - KeyError: 'name' not found in result_json (line 52).
- **Technique:**
  - Trace Forward:
    - Checked the results route and spotted the line where KeyError occurred.
- **Assumptions:**
  - Assumed the API response always contains a 'name' key.
- **Solution:**
  - Updated `'city': result_json.get('name', 'City Name Not Available')`.

**Issue 2: KeyError - 'weather' not found in result_json**

- **Expected vs. Actual Output:**
  - Expected: Display weather info with description.
  - Actual: KeyError: 'weather' not found in result_json.
- **Stack Trace:**
  - KeyError: 'weather' not found in result_json (line 53).
- **Technique:**
  - Trace Forward:
    - Checked the results route and identified the line where KeyError occurred.
- **Assumptions:**
  - Assumed the API response always contains a 'weather' key.
- **Solution:**
  - Updated `'description': result_json.get('weather', [{'description': 'Weather Data Not Available'}])[0]['description']`.
- **Solutions to other errors:**
  - Minor fix to the `<h2>` tag in home.html

**Issue 3: TypeError - Incorrect key used for temperature in result_json**

- **Expected vs. Actual Output:**
  - Expected: Display temperature info.
  - Actual: TypeError: Incorrect key for temperature in result_json.
- **Stack Trace:**
  - TypeError: Incorrect key for temperature in result_json (line 54).
- **Technique:**
  - Trace Forward:
    - Dug into the results route and spotted the line with the TypeError.
- **Assumptions:**
  - Assumed the key for temperature in API response is 'temp'.
- **Solution:**
  - Updated `'temp': result_json.get('main', {}).get('temp', 'Temperature Data Not Available')`.

**Issue 4: No handling for API request errors**

- **Expected vs. Actual Output:**
  - Expected: No errors.
  - Actual: No handling for API request errors.
- **Technique:**
  - Trace Forward:
    - Checked the results route and identified the absence of error handling for API requests.
- **Assumptions:**
  - Assumed API requests would always be successful.
- **Solution:**
  - Added error handling for API requests.

## Exercise 3

**Issue 1: IndexError - list index out of range**

- **Expected vs. Actual Output:**
  - Expected: Successful list sorting and correct index retrieval.
  - Actual: IndexError: list index out of range.
- **Stack Trace:**
  - IndexError: list index out of range (line 36).
- **Technique:**
  - Trace Forward:
    - Took a look at the merge_sort function and identified the line with IndexError.
- **Assumptions:**
  - Assumed the merge step was functioning correctly.
- **Solution:**
  - Changed `arr[k] = right_side[i]` to `arr[k] = right_side[j]` in the merge step.

**Issue 2: TypeError - list indices must be integers or slices, not float**

- **Expected vs. Actual Output:**
  - Expected: Successful index retrieval using binary search.
  - Actual: TypeError: list indices must be integers or slices, not float.
- **Stack Trace:**
  - TypeError: list indices must be integers or slices, not float.
- **Technique:**
  - Trace Forward:
    - Checked the binary_search function and identified the line with TypeError.
- **Assumptions:**
  - Assumed mid-point calculation in binary search was correctly handled.
- **Solution:**
  - Added `mid = int(mid)` to convert mid-point value to integer.