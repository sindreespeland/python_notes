# Module 4: Synchronization & Communication

When tasks run concurrently, they often need to share resources or talk to each other safely.

---

## Problem 16: The Safe Bank

**Goal**: Prevent race conditions.

**Scenario**:
A bank account has a balance of $0. 100 different tasks try to deposit $1 each at the exact same time.

**Requirements**:
1.  Create a shared Bank Account object.
2.  Implement a `deposit` method that reads the balance, sleeps for 0.01s (simulating IO), and then writes the new balance.
3.  Run 100 concurrent deposit tasks.
4.  **Issue**: Without protection, the final balance will likely be wrong (less than $100).
5.  **Fix**: Use an `asyncio.Lock` to ensure only one task can deposit at a time. The final balance must be exactly $100.

---

## Problem 17: The Traffic Light

**Goal**: Coordinate multiple tasks using a signal.

**Scenario**:
Five cars are waiting at a red light. When the light turns green, they should all go immediately.

**Requirements**:
1.  Create 5 "Car" tasks that wait for a signal.
2.  The main function waits a few seconds, then sends the signal.
3.  Use `asyncio.Event` to implement this. All cars should print "GO" effectively at the same time after the signal.

---

## Problem 18: Producer-Consumer

**Goal**: Coordinate work using a Queue.

**Scenario**:
A "Producer" generates work items at random intervals. A "Consumer" processes them.

**Requirements**:
1.  Create an `asyncio.Queue`.
2.  **Producer**: Puts 5 random numbers into the queue, then sends a "stop" signal (e.g., `None`).
3.  **Consumer**: Pulls numbers from the queue and prints them. Stops when it sees `None`.
4.  Run both concurrently.

---

## Problem 19: The Priority Worker

**Goal**: Process urgent tasks first.

**Scenario**:
You have a mix of High, Medium, and Low priority tasks.

**Requirements**:
1.  Use `asyncio.PriorityQueue`.
2.  Add tasks to the queue in a scrambled order (e.g., Low, High, Medium).
3.  The worker should automatically pull and process them in the correct order (High -> Medium -> Low).

---

## Problem 20: The Club Bouncer

**Goal**: Limit concurrency.

**Scenario**:
A nightclub has a capacity of 3 people. 10 people want to enter.

**Requirements**:
1.  Create a "enter_club" function that simulates dancing (sleeps 2s).
2.  Run 10 of these tasks concurrently.
3.  Use `asyncio.Semaphore` to ensure that **no more than 3** tasks are running (dancing) at any given moment.
