# Module 3: Blocking Code & Interoperability

One of the most common mistakes in async programming is running "blocking" code (heavy calculations or synchronous IO) directly in a coroutine. This freezes the Event Loop.

---

## Problem 13: The CPU Blocker

**Goal**: Experience the "Freeze".

**Scenario**:
You have a responsive UI (simulated by a fast loop printing messages) and a heavy background calculation (e.g., summing a massive range of numbers).

**Requirements**:
1.  Create a "UI" task that prints a message every 0.1 seconds.
2.  Create a "Calculation" function (a normal `def`, not `async`) that takes about 3-5 seconds to run.
3.  Run the UI task.
4.  Call the Calculation function from your main coroutine.
5.  **Observe**: Does the UI keep printing while the calculation runs? Or does it stop? (It should stop).

---

## Problem 14: The Thread Solution

**Goal**: Unblock the loop using threads.

**Scenario**:
Fix the frozen UI from Problem 13.

**Requirements**:
1.  Take the same setup as Problem 13.
2.  Modify the way you call the Calculation function.
3.  Use `asyncio.to_thread` (Python 3.9+) to offload the calculation.
4.  **Observe**: The UI should now continue printing messages smoothy *while* the calculation happens in the background.

---

## Problem 15: Legacy Executors

**Goal**: Learn how to use Executors (required for Python < 3.9 or for specialized pools).

**Scenario**:
Same as Problem 14, but you want to explicitly use a `ProcessPoolExecutor` instead of the default thread pool. This is useful for CPU-bound tasks in Python to bypass the GIL (Global Interpreter Lock).

**Requirements**:
1.  Instantiate a `ProcessPoolExecutor`.
2.  Run the blocking calculation using `loop.run_in_executor`.
3.  Ensure the behavior is non-blocking.
