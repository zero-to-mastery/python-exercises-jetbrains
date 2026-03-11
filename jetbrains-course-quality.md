# JetBrains Course Quality (Phase 2)

A skill for designing the teaching approach and implementing interactive tasks for JetBrains Academy courses.

**Phase 2 Focus:**
Designing tasks, adding placeholders, and configuring task files.
The goal is to produce deterministic course structure and tasks.

Follow the instructions exactly.
Do not invent alternative workflows.

# Prerequisite

Phase 1 must be completed (course structure and content transferred).

---

# What Phase 2 Does

For **each task in the lesson**:

1. Design the teaching approach
2. Write or improve the task description
3. Add placeholders in the code
4. Calculate byte offsets
5. Configure `task-info.yaml`
6. Finalize the task before moving to the next one

---

# Teaching Philosophy: Guided Discovery

Students learn best when they **discover solutions themselves**.

Do not give exact answers. Instead:

* explain concepts (**what and why**)
* let students implement (**how**)
* provide hints when necessary
* encourage experimentation

## Socratic Teaching Approach
    ❌ Traditional Approach
    ```python
    my_list = [1, 2, 3]
    first = my_list[0]
    ```

    Students copy the code without understanding.

    ✅ Guided Discovery Approach

    Explain the concept and let students implement it.

    Example task description:
    Lists store multiple values using square brackets.

    You can access elements using their index (starting at 0).
## Your Task
Create a list and access its elements.

Students must figure out the implementation themselves.

### Rules

* Explain concepts before exercises
* Do not show the exact solution code
* Examples must differ from exercises
* Allow students to experiment and learn from errors

Goal: **productive struggle with guidance**.

---

# Task Design Principles

### 1. Learning by Coding

Exercises must require **writing code**, not guessing values.

❌ Bad

```python
result = list(range(___))
# expected: [0,1,2,3,4]
```

Students only guess numbers.

✔ Good

```python
squares = []
for num in range(___):
    squares.append(num ** 2)
```

Students practice loops and transformations.

## Avoid Prediction-Only Tasks

Avoid tasks where students can obtain the correct answer simply by running the code.

Bad example:
```python
counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *= 2

print(counter)
```

Rule: Students should not be able to solve the task simply by running the program.

Prefer coding tasks where students must implement logic themselves.

---

### 2. Each Test Teaches Something New

Avoid repetitive exercises.

❌ Repetition

```python
enumerate(fruits)
enumerate(colors, start=1)
```

✔ Diverse applications

```python
# basic iteration
enumerate(fruits)

# numbered menu
f"{i}. {food}"

# conditional logic
if i % 2 == 0:
```

Each test should introduce a new idea or application.

---

### 3. Prefer Practical Patterns

Tasks should resemble real programming scenarios.

❌ Academic example

```python
for key, value in user.items():
    result[key] = value
```

✔ Practical example

```python
for key, value in user.items():
    result.append(f"{key}: {value}")
```

---

### 4. Task Description Must Match Exercises

Whenever exercises change, update `task.md`.

Check:

* description reflects the exercises
* examples match actual patterns
* outdated wording removed

### 5. Suggest Improvements Before Changing Tasks

If the user reports that a task is unclear or poorly designed:

1. Suggest improvements first
2. Wait for confirmation
3. Apply changes only after approval

Never modify task design immediately without user confirmation.

---

# Task Analysis Framework

Always evaluate tasks from two perspectives.

### Teacher Perspective

* What concept does the task teach?
* Are exercises diverse?
* Does the task build useful skills?

### Student Perspective

* Is the task clear?
* Is the objective understandable?
* Is the difficulty appropriate?

---

# Quick Design Checklist

### Learning Design

* learning by coding
* diverse tests
* practical patterns
* guided discovery

### Task Quality

* clear objective
* concise explanation
* no solution leaks

### Technical

* offsets calculated from final files
* run tests after changes
* propose improvements before implementing

---

# When to Use This Skill

Use **after Phase 1** and **before Phase 3**.

Phase 2 focuses on:

* designing the teaching approach
* defining student actions
* improving exercises
* ensuring learning through coding

---

# Placeholder Format (JetBrains Plugin)

```yaml
placeholders:
  - offset: <byte_position>
    length: 3
    placeholder_text: "TODO: implement condition"
```

`placeholder_text` appears as a TODO description in the IDE.

# placeholder_text Design Rule: Keep Code Syntactically Valid

**Important:** `placeholder_text` **replaces the author’s solution in the file that students see.**

This means the text inside `placeholder_text` becomes part of the student's code.
Therefore the unfinished code **must remain syntactically valid even before the student solves the task.**

---

❌ **Bad**

```python
a = # TODO
```

```yaml
placeholders:
  - offset: <byte_position>
    length: 3
    placeholder_text: "# TODO"
```

**Problem:**

* The placeholder replaces the real solution
* The resulting code becomes invalid Python
* Students immediately see syntax errors

---

✔ **Better**

```python
a = None  # TODO: replace with the answer
```

```yaml
placeholders:
  - offset: <byte_position>
    length: 3
    placeholder_text: "None  # TODO: replace with the answer"
```

**Benefits:**

* Code remains syntactically valid
* Students do not see many red syntax errors
* Code can run even before solving the task
* Tests can detect which placeholders remain unresolved
* Error messages can be more precise

---

**Rule:** placeholders must never break Python syntax.

## Phase 2 Workflow: Task-by-Task Teaching Design

For **each task**, follow this simplified workflow.

---

### Step 1 — Read the Task

Review the files created in Phase 1:

* `task.py` — starter code
* `task.md` — learning objective

Check:

* What concept the code demonstrates
* What students should learn
* Whether examples are clear and relevant

Goal: identify **one main concept** for the task.

---

### Step 2 — Think Like a Teacher

Decide how students should learn the concept.

Ask:

* What is the **single concept** this task teaches?
* What should be **explained in the description**?
* What should students **figure out themselves**?

Tasks should encourage **discovery through coding or reasoning**.

---

### Step 3 — Choose the Task Type

Select the task type that best supports learning.

JetBrains tasks use different `type` values in **task-info.yaml**.

---

#### Coding Task (preferred)

Students **write code**.

Used for practicing syntax, logic, or patterns.

`task-info.yaml` example:

```yaml
type: edu
files:
  - name: task.py
placeholders:
  - offset: 120
    length: 3
    placeholder_text: "TODO: implement condition"
```

Example exercise:

```python
def get_evens(numbers):
    result = []
    for num in numbers:
        if ___:
            result.append(___)
    return result
```

Students implement the missing logic.

---

#### Theory Task

Students **run code to observe behavior**.

Used when introducing a new concept.

`task-info.yaml` example:

```yaml
type: theory
files:
  - name: task.py
```

Example:

```python
numbers = [1, 2, 3]

for index, num in enumerate(numbers):
    print(index, num)
```

Students run the code and observe the behavior.

---

#### Output Task

Students **predict the output of code**.

Used to check understanding of execution flow.

`task-info.yaml` example:

```yaml
type: output
files:
  - name: task.py
placeholders:
  - offset: 10
    length: 3
    placeholder_text: "expected output"
```

Example exercise:

```python
prediction = ___

count = 0
for i in range(5):
    count += i

print(count)
```

Students predict the output.

---

### Step 4 — Design Placeholders

Placeholders should target **the concept being learned**.

Good placeholders:

```python
if ___:
    result.append(___)
```

Students write logic such as:

```
num % 2 == 0
num
```

Avoid placeholders for:

* variable names
* trivial syntax
* obvious code

Placeholders should require **thinking**, not guessing.
---

### Step 5 — Improve Examples (if needed)

Review examples from the original repository.

Keep them if they are:

* clear
* concise
* practical

Modify them if they are:

* overly complex
* abstract or academic
* based on guessing values

Example improvement:

❌ Guessing numbers

```python
result = list(range(___))
```

✔ Coding practice

```python
squares = []
for num in range(___):
    squares.append(num ** 2)
```

---

### Step 6 — Keep Code Clean

Avoid unnecessary output or noise.

❌

```python
print("Starting...")
result = calculate()
print(result)
print("Done")
```

✔

```python
result = calculate()
```

Tests should verify the **result variable**.

---

### input() Usage

Avoid `input()` in **coding tasks**.

❌

```python
name = input("Enter name: ")
greeting = "Hello, " + ___
```

Rule: Avoid `input()` in coding tasks because it forces students to run the code before understanding the problem.

✔

```python
name = "Alice"
greeting = "Hello, " + ___
```

Immediate clarity.

`input()` is acceptable in **theory tasks** when the goal is to demonstrate how input works.

## Task Description Size Rule

Task descriptions must be concise.

When reviewing `task.md`:

- remove unnecessary sections
- merge repetitive explanations
- keep only the concepts required to solve the task

Recommended size:

- simple topics → 80–120 words
- typical topics → 120–180 words
- advanced topics → 180–250 words

Avoid descriptions longer than ~250 words.

Avoid sections such as:

- "What You'll Learn"
- long conceptual introductions
- repeated explanations of basic concepts

Students should learn primarily by **reading code and completing the task**, not by reading long explanations.

## Choosing the Task Description Style

When writing or improving `task.md`, choose the description style based on the **purpose of the task**.

### Instructional Style (Program Interaction)

Use this style when the task focuses on **running and interacting with a program**, for example:

* the first program in a course
* tasks demonstrating `input()` and `print()`
* tasks where students must run the program and observe behavior

In these cases:

* guide the student step-by-step
* explain how to run the program
* explain where input and output appear
* focus on interaction rather than theory

When basic syntax is introduced, prefer **short code snippets with inline comments** to explain what the code does.

Example:

```python
name = input("What is your name?\n")  # waits for the user to type a name
print("Hello " + name)                # prints a greeting
```

Guidelines:

* explain syntax directly **next to the code**
* use **inline comments** for short explanations
* avoid long conceptual paragraphs describing the same behavior
* keep examples small (1–3 lines)

Preferred structure:

```
Short introduction
Example code with comments
What the program does
How to run it
Your task
```

Avoid long conceptual explanations in such tasks.

---

### Conceptual Style (Programming Concepts)

Use this style when the task teaches a **programming concept**, such as:

* inheritance
* functions
* classes
* algorithms
* data structures

In these tasks:

* explain the concept briefly
* show a small example
* then present the exercise

Example:

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass
```

Preferred structure:

```
Concept explanation
Example
Important rule (optional)
Your task
```
Keep explanations concise and focused on what the student needs to solve the task.

Avoid turning the description into a long theoretical lecture.

#### Step 7: Create or Update Task Description (`task.md`)

After designing what students will do in the task, write the **task description**.

The description explains the concept students need before solving the exercise.

The goal is to:

* explain the concept
* show typical syntax
* prepare students for the exercise

The description **must not reveal the solution**.

---

## Task Description Structure

````markdown
# Concept Name

## What Is [Concept]?

Explain the concept in a short paragraph.

Example:

Conditional logic lets your program make decisions based on conditions.  
It allows different code to run depending on whether conditions are true or false.

## Concept Explanation

Explain how the concept works and show **short code examples**.

Example:

Python uses three keywords for conditional logic:

**if** – Executes code when a condition is True

```python
if age >= 18:
    print("Adult")
````

**elif** – Checks another condition if previous conditions were False

```python
elif age >= 13:
    print("Teenager")
```

**else** – Executes when all previous conditions are False

```python
else:
    print("Child")
```

## Additional Patterns

Show other common ways the concept is used.

Example:

Use logical operators to combine conditions:

* `and` – both conditions must be True
* `or` – at least one condition must be True
* `not` – inverts the condition

```python
if is_adult and has_license:
    print("Can drive")
```

## Important Behavior

Explain important rules students must understand.

Example:

Python checks conditions **from top to bottom**.
Once a condition becomes `True`, its block runs and the remaining conditions are skipped.

## Your Task

Explain what students should do with the provided code.

Example:

This is a **prediction exercise**:

1. Study the conditional logic code provided
2. Predict what output each section will produce
3. Run the code to verify your understanding

**Challenge:** Why does the first version print different output than the improved version?

<div class="hint">
Remember that Python evaluates `if`, `elif`, and `else` conditions from top to bottom.  
Once a condition becomes True, the remaining conditions are skipped.
</div>
```

---

## Code Example Rules

Concept sections should include **small code examples**.

These examples help students understand syntax and usage.

Guidelines:

* Keep examples short (1–4 lines)
* Use several small snippets rather than one large block
* Examples should demonstrate syntax or behavior

Important rule:

Examples in the description **must not reuse the same variables, values, or logic as the exercise code**, otherwise the solution may be revealed.

If a student can solve the task by copying the example from the description with minimal edits, the example is too close to the exercise.

---

## Hints

Hints are written using HTML blocks:

```html
<div class="hint">
Helpful reminder for students who are stuck.
</div>
```

The platform automatically renders this block as **Hint**.

Hints are used when students may get stuck.

Hints should:

* remind students of syntax
* highlight an important rule
* point out a common mistake

Hints should **not** reveal the solution.

Concept explanations belong in the main description, not in hints.

## Special Rule for `theory` Tasks

Before inserting placeholders, check the task type in `task-info.yaml`.

If the task type is:

```yaml
type: theory
```

then no placeholders should be added to the code.

Theory tasks are used only for observing program behavior, not for filling missing code.

Action required:
- do not modify task.py
- do not insert placeholders
- do not configure placeholders in task-info.yaml

If the task type is theory, skip:
- Step 8 (Insert Temporary Placeholders)
- Step 9 (Calculate Offsets)
- Step 10 (Configure task-info.yaml)
- Step 11 (Replace Temporary Placeholders)

Proceed directly to the final verification step for the task.

#### Step 8: Insert Temporary Placeholders in Code

Now insert **temporary placeholders** into the exercise code.

⚠️ **Important rule:**
The temporary placeholder must have the **same length as the author's final answer**.

Do **not** use `___` if the real answer is longer.

Instead, replace the answer with a sequence of `_` characters that matches the length of the author solution.

This ensures that offsets remain correct when multiple placeholders exist.

---

### Example

Author answers:

```python
lambda x: x * 2
lambda x: x % 2 == 0
```

Lengths:

* `lambda x: x * 2` → 15 characters
* `lambda x: x % 2 == 0` → 20 characters

Temporary `task.py` used for offset calculation:

```python
def regular_function(x):
    return x * 2

numbers = [1, 2, 3, 4]

# placeholder length matches "lambda x: x * 2"
doubled = list(map(_______________, numbers))

# placeholder length matches "lambda x: x % 2 == 0"
evens = list(filter(____________________, numbers))
```

---

### Placeholder Placement Guidelines

Placeholders should represent **the concept students must implement**.

Good placeholders represent:

* expressions
* conditions
* lambda functions
* function calls
* small logic fragments

Avoid placeholders for:

* single obvious keywords (e.g., `lambda`, `for`, `if`)
* variable names
* trivial syntax

---

### ❗ Important Rule

Placeholder length **must equal the length of the author answer**.

Example:

Author answer:

```
lambda x: x * 2
```

Temporary placeholder:

```
_______________
```

This guarantees that all offsets remain correct when multiple placeholders are present.

---

#### Step 9: Calculate Byte Offsets

Offsets must be calculated from the **temporary file containing the underscore placeholders**.
Important: Offsets must be calculated only after all placeholders are inserted into the temporary file.

Example script:

```python
import re

def calculate_offsets(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    offsets = []

    pattern = re.compile(rb'(?<!\w)_{1,}(?!\w)')

    for match in pattern.finditer(content):
        offsets.append((match.start(), len(match.group())))

    return offsets
```

Example output:

```
Offset 120 length 15
Offset 186 length 20
```

These values will be used when configuring `task-info.yaml`.

#### Step 10: Configure `task-info.yaml`

After adding placeholders to the code and calculating offsets, configure them in **`task-info.yaml`**.

Each placeholder in the file must have a corresponding configuration entry.

---

## Example `task-info.yaml`

```yaml
type: edu
files:
- name: task.py
  visible: true
  placeholders:
  - offset: 120
    length: 15
    placeholder_text: "#TODO: write lambda expression that doubles the number"

  - offset: 186
    length: 20
    placeholder_text: "#TODO: write lambda condition to filter even numbers"

- name: task.md
  visible: false
```

---

## Field Explanations

### `type`

Defines the **task type**.

Examples:

```yaml
type: edu      # coding task
type: theory   # run code to observe behavior
type: output   # predict program output
```

---

### `offset`

Byte position of the placeholder in the file.

This value must match the position calculated in **Step 9**.

---

### `length`

Length of the **author's hidden answer** in the file.

Examples:

```yaml
length: 15   # for "lambda x: x * 2"
length: 20   # for "lambda x: x % 2 == 0"
```
This value must match the exact number of characters in the final author answer that will be hidden from the student.
---

### `placeholder_text`

Text displayed in the IDE when the student hovers over the placeholder.

It should describe **what the student needs to implement**, not what keyword to insert.

Good examples:

```yaml
"TODO: write lambda expression that doubles each number"
"TODO: complete the condition"
"TODO: create lambda expression for filtering"
```

Avoid overly trivial descriptions such as:

```yaml
"TODO: add lambda keyword"
```

because this encourages guessing instead of understanding.

---

## Important Rule

`placeholder_text` should describe the **conceptual task**, not the exact syntax.

Good:

```yaml
"TODO: write lambda expression to double numbers"
```

Bad:

```yaml
"TODO: add lambda keyword"
```

Students should think about the **logic they need to implement**, not just insert a specific token.

---

## Final Step

After `task-info.yaml` is ready, reopen **`task.py`** and replace each temporary underscore placeholder with the **real author answer**.

The placeholder system will hide that answer from the student and display `placeholder_text` instead.

---

## Verification Checklist

Before finishing this step:

* Every placeholder region in the code has a corresponding placeholder entry
* Offsets match the values from Step 9
* `length` matches the length of the real author answer
* Temporary underscore placeholders were replaced with the real author answers
* `placeholder_text` clearly describes the task

#### Step 11: Replace Temporary Placeholders with Author Answers

After configuring `task-info.yaml`, reopen **`task.py`** and replace each temporary underscore placeholder with the **real author answer**.

These answers will be hidden from students by the placeholder system and replaced in the editor with `placeholder_text`.

---

## Example

### Temporary `task.py` (used for offset calculation)

```python
def regular_function(x):
    return x * 2

numbers = [1, 2, 3, 4]

doubled = list(map(_______________, numbers))
evens = list(filter(____________________, numbers))
```

Where:

* `_______________` corresponds to the author answer `lambda x: x * 2`
* `____________________` corresponds to the author answer `lambda x: x % 2 == 0`

---

### Final `task.py` (after inserting author answers)

```python
def regular_function(x):
    return x * 2

numbers = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

Students will **not see these answers** in the editor.

Instead, the IDE will display the placeholder defined in `task-info.yaml`, for example:

```
TODO: write lambda expression that doubles the number
```

---

## Important Rules

* The author answers must exactly match the `length` specified in `task-info.yaml`.
* Do not change the file structure after calculating offsets.
* Do not modify whitespace or indentation around placeholders, otherwise offsets may break.

---

## Verification Checklist

Before finishing this step:

* All temporary underscore placeholders were replaced with author answers
* Author answers match the `length` specified in `task-info.yaml`
* The file still runs correctly
* Offsets in `task-info.yaml` still point to the correct positions

#### Step 12: Verify Task Completion

Before moving to the next task, verify that the current task is fully configured.

First check the task type in `task-info.yaml`.

---

### If the task type is `edu` or `output`

Verify the following:

* `task.md` exists and explains the concept
* `task.py` contains the final author answers (temporary placeholders removed)
* Every placeholder in `task.py` has a corresponding entry in `task-info.yaml`
* `offset` values match the positions calculated in Step 9
* `length` matches the length of the hidden author answer
* `placeholder_text` clearly describes what the student must implement
* `task.md` is marked as invisible in `task-info.yaml`

The number of placeholders in the code must match the number of placeholder entries in `task-info.yaml`.

---

### If the task type is `theory`

Verify the following:

* `task.md` exists and explains the concept
* `task.py` contains the demonstration code for the concept
* no placeholders are present in the code
* `task-info.yaml` contains `type: theory`
* `task.md` is marked as invisible in `task-info.yaml`

Theory tasks should not contain placeholders or placeholder configuration.

---

If everything is correct, the task is ready for **Phase 3 (test implementation)**.
### Phase Transition

After completing **Phase 2** for the current task:

→ Proceed immediately to **Phase 3** for the **same task**.

Phase 2 and Phase 3 operate at the **task level**, while tasks are processed **sequentially within the current lesson**.

In Phase 3 you will implement the tests located in the task directory.

Example structure:

```
L01/
  T01/
    task.py
    task.md
    task-info.yaml
    tests/
  T02/
    task.py
    task.md
    task-info.yaml
    tests/
``` 

Processing order inside the lesson:

1. **Phase 2 → T01** (design task)
2. **Phase 3 → T01** (implement tests)
3. **Phase 2 → T02**
4. **Phase 3 → T02**
5. Continue until all tasks in the lesson are completed.

After Phase 3 for the current task is complete:

1. The task is fully implemented
2. Move to the **next task in the lesson** (`T02`, `T03`, ...)

For the next task:

→ Return to **Phase 2** and repeat the process.