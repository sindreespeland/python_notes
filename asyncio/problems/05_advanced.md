# Module 5: Advanced Patterns

---

## Problem 21: The Timer Context

**Goal**: Create a reusable tool for timing code blocks.

**Scenario**:
You often need to measure how long an `await` takes.

**Requirements**:
1.  Create an Asynchronous Context Manager (class with `__aenter__` and `__aexit__`).
2.  Usage should look like:
    ```python
    async with AsyncTimer():
        await some_slow_process()
    ```
3.  It should automatically print the elapsed time when the block exits.

---

## Problem 22: The Number Stream

**Goal**: Work with Async Generators.

**Scenario**:
You need to stream a sequence of numbers where each number takes some time to generate.

**Requirements**:
1.  Create a function `async_stream(limit)` that yields numbers 0 to `limit`, pausing for 0.5s between each one.
2.  Iterate over this stream in your main function using `async for`.

---

## Problem 23: Async List Comprehensions

**Goal**: Build a list from an async source.

**Scenario**:
Reuse the stream from Problem 22.

**Requirements**:
1.  Instead of a loop, use an asynchronous list comprehension (`[x async for x in ...]`) to collect all numbers into a list.
2.  Filter the list to keep only even numbers inside the comprehension itself.

---

## Problem 24: The External Process

**Goal**: interact with the OS.

**Scenario**:
You need to run a shell command (e.g., `ping`) and process its output line-by-line as it happens.

**Requirements**:
1.  Use `asyncio.create_subprocess_exec` to run a command (e.g., `ping -c 3 google.com`).
2.  Read from the process's `stdout` continuously.
3.  Print each line with a prefix "RECEIVED: ".
4.  Wait for the process to exit completely.
