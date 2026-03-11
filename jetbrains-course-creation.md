# JetBrains Course Creation — Phase 1 (Structure + Transfer)

## Role

Convert educational programming content from a GitHub repository into a **JetBrains Academy (EduTools) course skeleton**.

The output must be a **structural course draft** that mirrors the repository content but **does not yet contain interactivity**.

---

# Goal (Phase 1)

Create the JetBrains course structure and transfer source content **AS-IS**.

Tasks in this phase:

* Build **course / section / lesson / task directories**
* Copy code from GitHub **without modifying the code**
* Write `task.md` explaining **learning objectives**
* Create **empty test files**
* Add **minimal YAML configuration**
* Produce a **GitHub → JetBrains mapping summary**

---

# Out of Scope (NOT in Phase 1)

The following actions are **strictly forbidden in Phase 1**:

* Quality review or pedagogical improvements
* Adding placeholders (`___`)
* Offset calculations
* Writing tests
* Modifying the original code
* Refactoring source files
* Creating solution files

Phase 1 performs **structure creation and content transfer only**.

---

# Required Decisions (Before Creating Files)

These decisions must be made **before generating the structure**.

1. **Sections**
2. **Lesson Type**
3. **Path ID Scheme**

---

# Decision Rules


## Section Decision (Repository Structure)

Determine whether the course requires **sections** by analyzing the repository folder hierarchy.

### Hard Rule

Do NOT create sections unless the repository clearly contains a grouping layer above lessons.
Sections are allowed only when multiple groups exist and each group contains multiple lessons.

If this condition is not met → do not create sections.
### Flat Course (No Sections)

Use a **flat structure** when topic folders exist directly at repository root.

Example repository:

```
repo/
  topic1/
    task1.py
    task2.py
  topic2/
    task1.py
    task2.py
```

Mapping:

```
Course/
  L01/
    T01/
    T02/
  L02/
    T01/
    T02/
```

Use flat structure when:

* top-level folders represent topics
* folders contain exercises
* there is **no grouping layer**

---

### Course With Sections

Use sections when the repository has **topic groups above lessons**.
Important rule: use sections if there is several 
Example repository:

```
repo/
  oop/
    classes/
      task1.py
      task2.py
    inheritance/
      task1.py
  algorithms/
    sorting/
      task1.py
    searching/
      task1.py
```

Mapping:

```
Course/
  SEC01/
    L01/
      T01
      T02
    L02/
      T01
  SEC02/
    L03/
      T01
    L04/
      T01
```

Interpretation:

```
oop, algorithms → sections
classes, inheritance → lessons
```

---

### Decision Rule

```
repo/topic/tasks
→ lessons only

repo/group/topic/tasks
→ sections + lessons
```

---

## Lesson Type Decision

Choose which template type fits the lesson structure.

### Regular Lesson

Template reference: `course_lesson/`

Use when:

* tasks are independent
* each task teaches one concept
* tasks do not depend on previous tasks

Typical examples:

* variables
* loops
* functions
* small algorithms

---

### Framework / Guided Project

Template reference: `course_guided_project/`

Use when:

* tasks build a **single project step-by-step**
* framework code already exists
* later tasks depend on earlier ones

---

### Lesson Type Rule

```
Independent tasks → course_lesson/

Project progression → course_guided_project/
```

The chosen template structure must be **used consistently**.

---

# Path ID Scheme

Folder names must stay **short and stable**.

Use IDs only:

```
Sections → SEC01
Lessons  → L01
Tasks    → T01
```

Human-readable titles must be stored in **`custom_name`**.

---

# Naming Rules

Rules for folder structure:

* Every lesson **must contain task folders**
* Even if there is **only one task**, create `T01`
* All files must be placed inside the task folder

Example:

```
Course/
  SEC01/
    L01/
      T01/
        task.py
        task.md
        task-info.yaml
        tests/
          __init__.py
          test_task.py
```

---

# File Naming Rules

These rules define how **repository files are mapped into task files**.

---

## Case 1 — Single Source File

If a task contains **only one source file**, rename it to:

```
task.py
```

Example repository:

```
repo/topic/add_numbers.py
```

Course structure:

```
Course/
  L01/
    T01/
      task.py
      task.md
      task-info.yaml
      tests/
        __init__.py
        test_task.py
```

Rules:

* the file content must remain **unchanged**
* only the **filename changes**

---

## Case 2 — Multiple Source Files

If a task contains **multiple files**, preserve the **original filenames**.

Example repository:

```
repo/topic/
  calculator.py
  utils.py
  constants.py
```

Course structure:

```
Course/
  L01/
    T01/
      calculator.py
      utils.py
      constants.py
      task.md
      task-info.yaml
      tests/
        __init__.py
        test_task.py
```

Rules:

* preserve original filenames
* preserve file relationships
* do **not rename files**

---

### File Mapping Rule

```
If task contains ONE file
→ rename it to task.py

If task contains MULTIPLE files
→ keep original filenames
```

Code content must remain **unchanged**.

---

# Template Reference

Use the JetBrains template **only as a structural reference**:

https://github.com/jetbrains-academy/python-course-template/tree/konstantin/refactoring

The template shows:

* correct folder structure
* YAML configuration
* test directory placement

Do **not copy template lesson names**.

Instead use:

```
SECxx
Lxx
Txx
```

Store visible titles in `custom_name`.

---

# Minimum Task Structure

Each task directory must contain:

```
task.py or original files
task.md
task-info.yaml
tests/__init__.py
tests/test_task.py
```

Rules:

* code must be **copied AS-IS**
* test files must be **empty**
* no additional files allowed

Do **not create**:

```
solution.py
main.py
README.md
```

---

# Minimal task-info.yaml

### Single File Task

```yaml
type: edu
custom_name: "Human readable title"

files:
  - name: task.py
    visible: true
  - name: task.md
    visible: false
```

---

### Multiple File Task

```yaml
type: edu
custom_name: "Human readable title"

files:
  - name: calculator.py
    visible: true
  - name: utils.py
    visible: true
  - name: constants.py
    visible: true
  - name: task.md
    visible: false
```

Do **not add extra YAML fields**.

---

# Phase 1 Workflow

## 1 Analyze Repository

* summarize repository structure
* list folders and files
* identify topics

---

## 2 Decide Course Structure

Determine:

* sections or flat course
* lesson type
* ID naming scheme

---

## Important Rule — Do Not Rely on Repository Order

Repository order may **not reflect learning order**.

Tasks and folders can appear in **random or non-pedagogical order**.

You must reorganize them according to **conceptual progression**.

Example repository:

```
repo/topic/
  advanced_example.py
  basic_example.py
```

Correct course order:

```
L01/
  T01 basic_example.py
  T02 advanced_example.py
```

Concept progression should follow:

```
simple concept
→ basic usage
→ variations
→ advanced usage
```

Pedagogical order **always overrides repository order**.

---

## 3 Create Directory Structure

Create directories based on the approved plan.

Required configuration files:

```
course-info.yaml
section-info.yaml
lesson-info.yaml
```

---

### course-info.yaml

With sections:

```yaml
title: Course Title
summary: Course summary
programming_language: Python
environment: unittest
language: English

content:
  - SEC01
  - SEC02
additional_files:
  - name: README.md
```

Without sections:

```yaml
title: Course Title
summary: Course summary
programming_language: Python
environment: unittest
language: English

content:
  - L01
  - L02
  - L03

additional_files:
  - name: README.md
```

---

### section-info.yaml

```yaml
type: section
custom_name: "Section Title"

content:
  - L01
  - L02
```

---

### lesson-info.yaml

```yaml
custom_name: "Lesson Title"

content:
  - T01
  - T02
```

---

# 4 Transfer Content Per Task

For each task:

1. Copy GitHub code **without modification**
2. Apply the **file naming rules**
3. Write `task.md`
4. Create `task-info.yaml`

---

# Learning Objective Extraction

Before writing `task.md`, analyze the exercise file.

Learning objectives must be derived from:

```
1 Code structure
2 Author comments
```

Identify:

* main concept
* supporting concepts
* skills students practice
* concept progression
* real-world context (if present)

---

# Write task.md

`task.md` must explain the concept **before the student reads the code**.

Do **not explain how to solve the task**.

---

## Required Structure

```
# Task Title

## What You'll Learn

Short summary of the concept.

## Concept Overview

Explain what the concept is and why it matters.

## Key Concepts

### Concept 1
Explanation

### Concept 2
Explanation

## Example

Provide an example different from the exercise code.

## Your Task

Explain what students will practice.
```

---

## task.md Rules

Allowed:

* concept explanations
* contextual examples
* conceptual learning goals

Forbidden:

* solutions
* step-by-step instructions
* reuse of exercise variables

Recommended length:

```
30–50 lines
```

---

# 5 Create Empty Test Files

Each task must contain:

```
tests/
  __init__.py
  test_task.py
```

Rules:

* files must exist
* files must be empty or comments only
* no real tests in Phase 1

---

# 6 Produce Summary

At the end generate:

### Course Statistics

* number of sections
* number of lessons
* number of tasks

---

### GitHub → JetBrains Mapping

| GitHub Path        | JetBrains Path | Lesson       | Task       |
| ------------------ | -------------- | ------------ | ---------- |
| repo/topic/file.py | SEC01/L01/T01  | Lesson Title | Task Title |

---

# Output Requirements

When Phase 1 is complete the result must include:

* correct directory tree
* original GitHub code copied **AS-IS**
* `task.md` for every task
* **empty test files**
* minimal YAML configuration
* mapping summary

Phase 1 produces **structure only**.

Later phases will add:

* placeholders
* tests
* hints
* validation
* course interactivity.
