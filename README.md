# campus_credentials
Step 1: init_tuple = (1,) * 3
This line creates a tuple.

The expression (1,) creates a tuple with a single element: (1,).

The comma is necessary because () by itself would be interpreted as just an empty parentheses, not a tuple.

The * 3 part means you're repeating the tuple (1,) three times.

So, init_tuple = (1,) * 3 results in the tuple (1, 1, 1).

Step 2: init_tuple[0] = 2
This line tries to modify the first element of the tuple (init_tuple[0]) and set it to 2.

However, tuples are immutable in Python, meaning that once they are created, their contents cannot be changed. So, trying to assign a new value to init_tuple[0] will raise an error.

Error Explanation:

Since tuples are immutable, attempting to modify an element of the tuple using an assignment like init_tuple[0] = 2 will result in a TypeError.

Step 3: print(init_tuple)
This line will never be reached due to the error in Step 2. If the code were fixed, it would print the current state of the tuple, which, in this case, would be (1, 1, 1).