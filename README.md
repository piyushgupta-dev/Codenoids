# Repository Overview

Welcome to this repository.

This repository contains coding problem solutions, learning materials, implementations, and projects developed while exploring different technologies and concepts. The content is organized to track progress, document approaches, and maintain a structured collection of work.

## Contents

### Data Structures & Algorithms

Solutions to algorithmic and programming problems along with explanations of the approaches and concepts used.

### Agentic AI

Learning notes, experiments, implementations, and resources related to Agentic AI and intelligent systems.

## Directory Structure

```text
Repository/
│
├── DSA/
│   ├── Day-1/
│   │   ├── Add_Two_Numbers.cpp
│   │   └── Two_Sum.cpp
│   │
│   ├── Day-2/
│   │   ├── Longest_Substring_Without_Repeating_Characters.cpp
│   │   └── Roman_to_Integer.cpp
│   │
│   ├── Day-3/
│   │   └── Longest_Palindromic_Substring.cpp
│   │
│   ├── Day-4/
│   │   ├── Longest_Common_Prefix.cpp
│   │   └── Container_With_Most_Water.cpp
│
└── README.md
```

# 📊 Progress Summary

| Day   | Problems Completed                                               |
| ----- | ---------------------------------------------------------------- |
| Day 1 | Add Two Numbers, Two Sum                                         |
| Day 2 | Longest Substring Without Repeating Characters, Roman to Integer |
| Day 3 | Longest Palindromic Substring                                    |
| Day 4 | Longest Common Prefix, Container With Most Water                 |

**Total Problems Solved:** 7

---

# 📝 Problem Solutions

## Day 1

### 1. Add Two Numbers

**File:** `Add_Two_Numbers.cpp`

**Approach Used**

* Traversed both linked lists simultaneously.
* Added corresponding digits along with carry.
* Created a new linked list for the result.
* Continued processing until all nodes and carry were handled.

**Concepts**

* Linked Lists
* Traversal
* Carry Management

**Complexity**

* Time: O(max(n, m))
* Space: O(max(n, m))

---

### 2. Two Sum

**File:** `Two_Sum.cpp`

**Approach Used**

* Used an unordered map to store elements and indices.
* Checked whether the required complement already existed.
* Returned the pair of indices once found.

**Concepts**

* Hashing
* Arrays
* Efficient Lookup

**Complexity**

* Time: O(n)
* Space: O(n)

---

## Day 2

### 3. Longest Substring Without Repeating Characters

**File:** `Longest_Substring_Without_Repeating_Characters.cpp`

**Approach Used**

* Applied the Sliding Window technique.
* Maintained a window containing unique characters.
* Adjusted window boundaries whenever duplicates appeared.

**Concepts**

* Sliding Window
* Strings
* Hash Map

**Complexity**

* Time: O(n)
* Space: O(n)

---

### 4. Roman to Integer

**File:** `Roman_to_Integer.cpp`

**Approach Used**

* Stored Roman numeral values in a map.
* Compared current and next symbols.
* Added or subtracted values according to Roman numeral rules.

**Concepts**

* String Processing
* Mapping
* Greedy Logic

**Complexity**

* Time: O(n)
* Space: O(1)

---

## Day 3

### 5. Longest Palindromic Substring

**File:** `Longest_Palindromic_Substring.cpp`

**Approach Used**

* Used the Expand Around Center technique.
* Considered every character as a potential palindrome center.
* Checked both odd and even length palindromes.
* Updated the longest palindrome found.

**Concepts**

* Strings
* Two Pointers
* Palindrome Detection

**Complexity**

* Time: O(n²)
* Space: O(1)

---

## Day 4

### 6. Longest Common Prefix

**File:** `Longest_Common_Prefix.cpp`

**Approach Used**

* Assumed the first string as the initial prefix.
* Compared the prefix with each string in the array.
* Reduced the prefix length whenever a mismatch occurred.
* Continued until a common prefix was found for all strings.

**Concepts**

* Strings
* Prefix Matching
* Iterative Comparison

**Complexity**

* Time: O(n × m)
* Space: O(1)

Where:

* n = Number of strings
* m = Length of the shortest string

---

### 7. Container With Most Water

**File:** `Container_With_Most_Water.cpp`

**Approach Used**

* Used the Two Pointer technique.
* Initialized pointers at both ends of the array.
* Calculated the container area at each step.
* Moved the pointer with the smaller height to maximize the possible area.
* Tracked the maximum area found.

**Concepts**

* Arrays
* Two Pointers
* Optimization

**Complexity**

* Time: O(n)
* Space: O(1)

---

# 🎯 Objectives

* Strengthen problem-solving skills.
* Learn and implement Agentic AI concepts.
* Build practical projects and applications.
* Maintain consistency in learning and development.
* Document progress and implementations systematically.

---

## 📅 Current Status

✅ DSA Problems Solved: 7

🚀 Agentic AI Learning: In Progress
