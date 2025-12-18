# Mastering Python Asyncio: Hands-on Problem Set

Welcome to the expanded `asyncio` curriculum! This course is designed to take you from beginner to expert through a series of hands-on drills and scenarios. We cover everything from basic syntax to modern TaskGroups and handling blocking code.

## How to use this course

1.  **Sequential Order**: Start with Module 1. The concepts build upon each other.
2.  **Solve in Python**: Create a file for each problem (e.g., `m1_p1.py`) and write your solution.
3.  **Docs**: Keep the [Python asyncio docs](https://docs.python.org/3/library/asyncio.html) open.
4.  **Evaluation**: Ask me to review your solutions after each module!

## Curriculum

### [Module 1: The Foundations](./01_basics.md)
*Core syntax, coroutines, and flow control.*
- **P1**: Hello Async
- **P2**: The Delayed Greeter
- **P3**: Sequential Execution
- **P4**: The Retry Loop (Control Flow)
- **P5**: The Coroutine Chain (Passing Data)

### [Module 2: Managing Tasks & Concurrency](./02_concurrency.md)
*Running multiple operations at once. Updated for modern Python.*
- **P6**: The Basic Gatherer
- **P7**: The Faulty Gatherer (Handling Errors in Gather)
- **P8**: The Task Group (Modern Concurrency)
- **P9**: The Crashed Group
- **P10**: Background Workers (`create_task`)
- **P11**: The Timeout (`wait_for`)
- **P12**: The Shield (Preventing Cancellation)

### [Module 3: Blocking Code & Interoperability](./03_blocking.md)
*How to work with synchronous code without freezing the loop.*
- **P13**: The CPU Blocker (Demonstrating the problem)
- **P14**: The Thread Solution (`to_thread`)
- **P15**: Legacy Executors (`run_in_executor`)

### [Module 4: Synchronization & Communication](./04_synchronization.md)
*Coordinating shared state safely.*
- **P16**: The Safe Bank (Locks)
- **P17**: The Traffic Light (Events)
- **P18**: Producer-Consumer (Queues)
- **P19**: The Priority Worker (PriorityQueue)
- **P20**: The Club Bouncer (Semaphores)

### [Module 5: Advanced Patterns & Subprocesses](./05_advanced.md)
*Idiomatic patterns and system interaction.*
- **P21**: The Timer Context (Async Context Managers)
- **P22**: The Number Stream (Async Iterators)
- **P23**: Async List Comprehensions
- **P24**: The External Process (Subprocesses)

### [Module 6: Final Project](./06_final_project.md)
*Putting it all together.*
- **P25**: The Simulated Microservice System
