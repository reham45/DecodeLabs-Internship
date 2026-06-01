# DecodeLabs-Internship
# Project Overview

A robust Python Command Line Suite focusing on core engineering principles, security, and defensive design pattern execution.

---

## 📦 Application Summary

### 1. To-Do List Manager

* Implements clean structural pattern matching (`match`/`case`) instead of nested conditionals.
* Manages data allocation dynamically on the heap and scales massive arrays by splitting "Giant Lists" into sub-lists.

### 2. Expense Tracker

* Tracks financial records across categorized limits.
* Uses a strict accumulator loop equipped with an automated kill-switch that breaks execution immediately if the preset budget ceiling is breached.

### 3. Enterprise Password Generator

* Generates mathematically secure, brute-force-resistant passwords using low-level OS hardware noise via `secrets.choice()`.
* Evaluates cryptographic strength via information entropy:

$$E = \text{Len} \cdot \log_2(R)$$



---

## 📐 Project Measurement Metrics

* **Defensive Stability (Poka-Yoke):** Achieved via mandatory type transformation and zero unhandled crashes using specific `try-except` error containment.
* **Quality Standard Pillars:** Every module is evaluated against four strict baselines: *Stability*, *Defense*, *Control*, and *Initial State Management*.
* **Control:** The kill switch prints the final total before terminating.
* **State:** The total variable is initialized OUTSIDE the loop.
