# Module 2: Managing Tasks & Concurrency

This module focuses on doing multiple things at once. You will need to look up how `asyncio` handles concurrent execution.

---

## Problem 6: The Basic Gatherer

**Goal**: Run multiple coroutines concurrently.

**Scenario**:
You need to fetch data for 3 different user IDs (1, 2, and 3). Each fetch takes a different amount of time (e.g., 2s, 3s, 1s).

**Requirements**:
1.  Create a fetch coroutine that simulates the delay and returns the data.
2.  In your main function, trigger all 3 fetches so they run **simultaneously**.
3.  Collect the results of all 3 fetches into a list.
4.  **Verification**: The total execution time of the program must be roughly equal to the *longest* individual delay (3s), not the sum of them (6s).

---

## Problem 7: The Faulty Gatherer

**Goal**: Handle exceptions when running multiple tasks concurrently.

**Scenario**:
You are running 3 tasks concurrently. One of them is guaranteed to crash (raise an Exception).

**Requirements**:
1.  Create a success task (returns "OK") and a failing task (raises `ValueError`).
2.  Run 3 tasks together: [Success, Fail, Success].
3.  **Part A**: Run them normally. Observe that the entire batch likely crashes or halts.
4.  **Part B**: Modify your approach so that you still get the results for the successful tasks, and the exception object for the failed task, in a single list (e.g., `["OK", ValueError(...), "OK"]`).

---

## Problem 8: The Task Group (Modern Concurrency)

**Goal**: Use the modern context manager approach (Python 3.11+) to manage background tasks.

**Scenario**:
You want to fire off two "printer" tasks that run in the background while your main function waits for them to finish.

**Requirements**:
1.  Use the `asyncio.TaskGroup` context manager (or look up how to use it).
2.  Schedule two tasks inside the group: one prints "A" after 1s, the other prints "B" after 2s.
3.  Prove that the context manager (`async with ...`) waits until *both* tasks are complete before exiting the block.

---

## Problem 9: The Crashed Group

**Goal**: Understand "Structured Concurrency" and cancellation.

**Scenario**:
You have a TaskGroup with two workers. Worker A fails quickly. Worker B is slow but successful.

**Requirements**:
1.  Create Worker A: Sleeps 1s, then raises an Error.
2.  Create Worker B: Sleeps 5s, then prints "Finished".
3.  Run them in a TaskGroup.
4.  **Question**: Does Worker B ever print "Finished"? Run the code to find out. Understand *why* based on how TaskGroups handle sibling failure.

---

## Problem 10: Background Workers (Fire & Forget)

**Goal**: Launch a task that runs in the background while the main function continues doing other work.

**Scenario**:
You want a "Heartbeat" system that prints "Alive..." every 0.5 seconds while your main application performs a heavy job (simulated by a 2s sleep).

**Requirements**:
1.  Start the Heartbeat coroutine.
2.  Immediately (without waiting for it to finish) start the main "heavy job".
3.  Once the main job is done, stop (cancel) the heartbeat.
4.  Ensure the program exits cleanly without error traces.

---

## Problem 11: The Timeout

**Goal**: Enforce a time limit on an operation.

**Scenario**:
You are calling a slow external API that takes 5 seconds. You are only willing to wait 2 seconds.

**Requirements**:
1.  Call the slow operation.
2.  If it takes longer than 2 seconds, abort it and print "Too slow!".

---

## Problem 12: The Shield

**Goal**: Protect a critical task from being cancelled.

**Scenario**:
You have a "Save to DB" operation that takes 3 seconds. It is critical that this completes, even if the user cancels the request or the connection times out.

**Requirements**:
1.  Wrap the "Save" operation in a timeout of 1 second (simulating a user giving up).
2.  Normally, the Save operation would be cancelled when the timeout hits.
3.  **Challenge**: Prevent the cancellation of the "Save" task. The timeout should still trigger (raising an error in the main flow), but the "Save" task should continue running in the background until it finishes.
