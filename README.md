# Python Learning Repository

A collection of Python practice files covering fundamental to intermediate programming concepts.

## Files Overview

### Core Concepts
- **first.py** - Introduction to Python basics
- **conditional.py** - If/else statements and conditional logic
- **loops.py** - For and while loops
- **break&continue.py** - Loop control statements
- **strings.py** - String manipulation and operations
- **array.py** - Array and list basics
- **list&tuple.py** - Lists and tuples
- **Listpractice.py** - List practice exercises
- **sets.py** - Set operations and methods
- **dictonary.py** - Dictionary operations and manipulation

### Functions & Advanced Concepts
- **function&recc.py** - Functions and recursion
- **higher_order.py** - Higher-order functions
- **innerfunc.py** - Inner/nested functions
- **lamda.py** - Lambda functions
- **local&global.py** - Local and global variable scope

### Object-Oriented Programming
- **oops.py** - Object-oriented programming basics
- **inheritance.py** - Class inheritance and polymorphism

### Exception Handling
- **exception.py** - Try/except blocks and error handling

### Practical Applications
- **app.py** - Application example
- **banksys.py** - Bank system implementation
- **pythonchatbot.py** - OpenAI chatbot integration
- **qr.py** - QR code generation
- **module.py** - Module usage and imports

### Other Files
- **practice.py** - General practice exercises
- **trial.py** - Experimental code
- **n.py** - Miscellaneous practice

## Setup

### For Running pythonchatbot.py

This project includes a chatbot that uses the OpenAI API. To run it:

1. Install required dependencies:
   ```bash
   pip install openai python-dotenv
   ```

2. Create a `.env` file in the project root (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```

3. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the chatbot:
   ```bash
   python pythonchatbot.py
   ```

## Security

- **API keys are never committed to git** - Use environment variables (see `.env.example`)
- `.env` files are ignored via `.gitignore`
- Always keep your API keys confidential

## Getting Started

1. Clone the repository
2. Run any Python file:
   ```bash
   python filename.py
   ```

## Python Version

Tested with Python 3.10+

## License

Open for educational purposes.
