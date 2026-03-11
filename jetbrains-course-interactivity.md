# JetBrains Course Test Implementation (Phase 3)

A skill for implementing tests for JetBrains Academy tasks.

**Phase 3 Focus:** test implementation, 2-test workflow verification, and final task validation.

## ⚠️ IMPORTANT: Task-by-Task Workflow

This skill works on **ONE TASK at a time** within the current lesson.

### Workflow

1. Phase 1 completes course structure (course structure and content transferred)
2. Phase 2 designs and configures the current task
3. **Phase 3 (this skill)** implements tests for the **same task**
4. Human reviews the task
5. Move to the next task in the lesson
6. After all tasks in the lesson are completed, move to the next lesson

**Before starting:** confirm which task you are testing. It should be the same task just completed in Phase 2.

---

## Prerequisites for This Task

- Phase 1 complete
- Phase 2 complete **for this task**
- `task.py`, `task.md`, and `task-info.yaml` already configured
- `tests/test_task.py` exists and is ready to be implemented

**Result:** one fully tested and verified task, ready for human review.

---
## Special Rule for `theory` Tasks

If the task type in `task-info.yaml` is:

```yaml
type: theory
```

then the task must not contain automated tests.

Action required:

- delete the tests/ directory inside the task folder

- do not create tests/test_task.py

Reason:

theory tasks are used for observing program behavior and do not require automated validation.

If the task type is `theory`, Phase 3 ends.
Stop here.
Wait for user confirmation.
Do not continue automatically.
----
## Special Rule for `output` Tasks

Before implementing tests, check the task type in `task-info.yaml`.

If the task type is:

```yaml
type: output
```

then **Python unit tests must not be written**.

Output tasks validate the program by comparing the program's **stdout output** with the expected output.

### Test Structure

Instead of `tests/test_task.py`, the `tests` directory must contain:

```
tests/
  input.txt
  output.txt
```

* `input.txt` — data passed to the program through **stdin**
* `output.txt` — the **expected stdout output**

The platform automatically runs the program and compares its output with `output.txt`.

### Important Notes

* `input.txt` is optional and may be removed if the program does not require input.
* Output comparison is **exact**, including spaces and newline characters.

### Phase 3 Behavior for Output Tasks

If the task type is `output`:

* do **not create `tests/test_task.py`**
* create `tests/input.txt` and `tests/output.txt`
* ensure the program output exactly matches `output.txt`
* Phase 3 ends after preparing these files.
Stop here.
Wait for user confirmation.
Do not continue automatically.

## Purpose

Implement tests that:

- verify the learning objective from `task.md`
- fail for incomplete student solutions
- pass for correct student solutions
- fail for incorrect student solutions
- provide helpful, educational error messages

---

## Expected Input from Previous Phases

### From Phase 1
- task structure created
- task files transferred
- empty `tests/test_task.py` created

### From Phase 2
- task design finalized
- task type decided (`edu`, `theory`, `output`)
- `task.md` written
- placeholders configured
- `task-info.yaml` completed
- `task.py` contains the author solution hidden by placeholders

If Phases 1–2 are not complete for the current task, do not start Phase 3.

---

## Expected Output of This Skill

When this skill completes successfully, you will have:

- `tests/test_task.py` implemented for the current task
- 2-test workflow verified for the current task
- helpful and educational error messages
- one task ready for human review

---

## Quick Workflow Summary

### 3-Step Phase 3 Process

1. **Implement Tests** → write tests for the current task
2. **Run 2-Test Workflow** → verify fail / pass behavior
3. **Final Verification** → confirm the task is ready for review

---

## Phase 3 Workflow

### Step 1: Implement Tests for the Current Task

Write tests that verify the learning objective and student behavior for the current task.

#### 1.1 Review the Task

Before writing tests, read:

- `task.md` to understand the learning objective
- `task.py` to understand what students are expected to produce

Questions to answer:

- What concept does this task teach?
- What should the student be able to do?
- What behavior should the tests verify?
- What wrong answers should fail?

#### 1.2 Test Design Principles

Tests must:

1. fail for incomplete student solutions
2. verify the actual learning objective, not just syntax
3. check types where relevant
4. fail for wrong answers
5. pass for correct answers
6. provide helpful error messages

Important rules:

- test behavior, not implementation details, unless the implementation itself is the learning objective
- do not make tests so strict that valid alternative solutions fail
- do not reveal the answer in error messages

#### 1.3 Test Template Example

```python
import unittest

from task import a, b, ind, c


class TestCase(unittest.TestCase):
    def test_array_b_shape(self):
        self.assertEqual(a.shape, b.shape, msg="Array b needs to be of the same shape as a.")

    def test_array_b_sorted(self):
        self.assertTrue(all([b[0, n] <= b[1, n] <= b[2, n] <= b[3, n] <= b[4, n] for n in range(b.shape[1])]),
                        msg='Columns in b do not appear to be sorted.')

    def test_array_ind(self):
        self.assertEqual(a.shape, ind.shape, msg="Array ind needs to be of the same shape as a.")

    def test_array_c(self):
        self.assertEqual(a.shape, c.shape, msg="Array c needs to be of the same shape as a.")

    def test_array_c_sorted(self):
        self.assertTrue(all([c[0, n] <= c[1, n] <= c[2, n] <= c[3, n] <= c[4, n] for n in range(c.shape[1])]),
                        msg='Columns in c do not appear to be sorted.')

    def test_array_c_sorted_rows(self):
        for i in c:
            self.assertTrue(i[0] == min(i) and i[-1] == max(i), msg="Rows in array c should be sorted.")
```

#### 1.4 Register Test Files in `task-info.yaml`

After creating or modifying files inside the `tests/` directory, ensure that they are listed in `task-info.yaml`.

Test files must be **invisible to the student**.

Example configuration:

```yaml
files:
  - name: task.py
    visible: true

  - name: task.md
    visible: false

  - name: tests/test_task.py
    visible: false
```

Guidelines:

* Every file inside the `tests/` directory must appear in `task-info.yaml`
* All test files must have `visible: false`
* Test files must **never be visible to students**
* Do not add placeholders to test files


## Human Review

After tests for the current task are implemented and verified:

1. Stop the workflow.
2. Present the task for human review.
3. Wait for feedback before continuing.

After approval:
→ move to the **next task (T02, T03, …)**  
→ restart the workflow from **Phase 2**.