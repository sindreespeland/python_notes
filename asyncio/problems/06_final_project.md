# Module 6: Final Project

This is the capstone project.

---

## Problem 25: The Simulated Microservice System

**Goal**: Build a robust, fault-tolerant system.

**Scenario**:
You are building a backend for a web app. It consists of:
1.  **Web Server**: Receives requests.
2.  **Message Broker**: Holds requests.
3.  **Workers**: Process requests.
4.  **Database**: Stores results.

**System Requirements**:
1.  **Components**:
    - `Event`: To signal "System Startup Complete".
    - `Queue`: To act as the Message Broker.
    - `Lock`: To protect the Database.
    - `TaskGroup`: To manage the workers.

2.  **Workflow**:
    - **Step 1**: Start 3 "Worker" tasks. They should listen to the Queue.
    - **Step 2**: Start a "Web Server" task. It generates 20 requests (mix of "Read" and "Write") and puts them in the Queue.
    - **Step 3**: The Workers process items.
        - "Write" requests update the DB (simulated sleep + dict update).
        - "Read" requests just read.
        - **Crucial**: One specific request type (e.g. "Bad Request") should cause a Worker to crash (raise Exception).

3.  **Resilience**:
    - If a Worker crashes, the system should *not* stop entirely. The TaskGroup might cancel others (default behavior), OR you can try to handle it.
    - *Challenge*: Implement a "Supervisor" that restarts crashed workers, or use `return_exceptions=True` with gather if TaskGroup proves too strict for this specific requirement. (TaskGroups cancel everything on one failure, so you might need to wrap the worker logic in a strict try/except block to catch the crash *inside* the worker so it doesn't propagate to the Group).

4.  **Graceful Shutdown**:
    - After the Web Server finishes generating requests, wait for the Queue to be empty.
    - Signal the workers to stop (e.g. using a Sentinel `None` value in the queue or cancelling them).
    - Print the final Database state.
