# Python Foundation Challenge
**Week 4 — Functional Thinking + Revision (Weeks 1–3)**  
*Questions 1–10*

---

## Objective
Introduce functional programming as a natural next step after three months of Python fundamentals — pure functions, `map`, `filter`, comprehensions, higher-order functions, and a first real taste of recursion. This challenge is a gauge: it tells you (and them) where they are, not where they should already be.

---

## A Word Before You Start
You've been learning Python for about three months. You can write loops, use dictionaries, build functions, and solve problems. This week introduces a new style — functional programming — and the questions below are designed to stretch you, not to confirm what you already know.

* Some questions will feel familiar — those are revision with a twist.
* Some will feel new — those are the gauge. Struggling is the point.
* Bonus questions are optional. Do not attempt them until the required ones are done.
* If you get stuck for more than 20 minutes on one question, move on, come back later, or write down what concept is blocking you. That note is more valuable than the answer.

### What "functional" means here (short version)
* **Pure functions:** A pure function takes inputs and returns an output. Same input $\rightarrow$ same output. It does not print, does not change variables outside itself, and does not depend on anything except its arguments.
* `print()` belongs outside your functions, not inside them.
* Prefer `map`, `filter`, and comprehensions over manual loops where they make the code clearer. Loops are still allowed unless a question says otherwise.
* **Recursion:** A function that calls itself. It's not always better than a loop — but it's a tool you need to know.

---

## Instructions
1. Solve the problems independently. Do not look at previous solutions.
2. Focus on producing a working solution first; clean up the code afterward if time allows.
3. No external libraries unless a question explicitly permits them.
4. If you get stuck, identify the Python concept causing the problem rather than immediately searching for a solution.
5. **Functional theme:** Prefer pure functions, avoid mutating shared state, use `map`/`filter`/comprehensions where they help. Loops are allowed unless stated otherwise.
6. Bonus questions are optional stretch goals.

---

## Pure vs. Impure — See the Difference

### ❌ Impure version
*Prints inside the function, does two jobs at once:*

```python
def is_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(4)  # prints "Even"
is_even(4)  # prints "Even" again — but you can't reuse the result
