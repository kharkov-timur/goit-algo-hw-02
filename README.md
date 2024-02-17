# goit-algo-hw-02

## Request Processing System and Palindrome Checker

This project contains two independent Python programs designed to demonstrate the application of data structures such as queues and double-ended queues (deques) in solving practical tasks.

### Task 1: Request Processing System

This program simulates the reception and processing of requests in a service center.
It automatically generates new requests with unique identifiers, adds them to a queue, and sequentially removes them from the queue for processing.
This process mimics the operation of a service center where requests are processed in the order they are received.

#### Technologies
- Python
- `queue` module

### Task 2: Palindrome Checker

The program takes a string as an input parameter, adds all its characters to a double-ended queue (deque),
and then compares characters from both ends of the queue to determine if the string is a palindrome.
The program efficiently handles both strings with even and odd numbers of characters, ignoring letter case and spaces.

#### Technologies
- Python
- `collections` module

### Installation and Usage

To run each program, Python version 3.x must be installed.
Clone the repository and execute the scripts from the terminal or command line:

`python task1_service_center.py`

`python task2_palindrome_checker.py`