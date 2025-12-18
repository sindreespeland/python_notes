# Module 1: The Foundations

This module covers the absolute basics of `asyncio`: defining coroutines, running them, and simple control flow.

---

## Problem 1: Hello Async (Completed)

---

## Problem 2: The Delayed Greeter (Completed)

---

## Problem 3: Sequential Execution (Completed)

**Goal**: Observe the behavior of `await` in a sequence.

**Scenario**:
You need to greet "Alice" and "Bob". Each greeting takes 1 second to prepare (simulated delay).

**Requirements**:
1.  Reuse your `greet_after_delay` coroutine.
2.  Write a `main` function that greets "Alice", and *then* greets "Bob".
3.  Run this `main` function.
4.  **Analysis**: The total execution time should be approximately 2 seconds. Verify this.

---

## Problem 4: The Retry Loop (completed)

**Goal**: Implement error handling and loops within an async flow.

**Scenario**:
You are interacting with an unstable API.

**Requirements**:
1.  Create a coroutine representing the API. It should return "Success" 20% of the time, and raise a `ValueError` (or custom exception) 80% of the time.
2.  Create a "downloader" coroutine that calls this API.
3.  If the API fails, the downloader must print "Retrying..." and wait 1 second before trying again.
4.  It should keep trying indefinitely until it succeeds.
5.  Once successful, print "Data received!".

---

## Problem 5: The Coroutine Chain (completed)

**Goal**: Pass data from one asynchronous step to another.

**Scenario**:
You have a data processing pipeline consisting of two steps.

**Requirements**:
1.  **Step 1**: Takes a raw string, simulates work (1s delay), and returns the string appended with " -> Processed".
2.  **Step 2**: Takes the processed string, simulates work (1s delay), and returns it appended with " -> Saved".
3.  **Pipeline**: Create a main entry point that takes "Input Data", passes it through Step 1, passes *that* result through Step 2, and prints the final result.
