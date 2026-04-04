# 📝 Notes — Count Digits That Evenly Divide N

🔗 **Problem Link:** [Count Digits — GeeksForGeeks](https://www.geeksforgeeks.org/problems/count-digits1038/1)

---

## 📌 Core Concept
For each digit `d` in `n`:
- Skip if `d == 0` (division by zero is undefined)
- Check if `n % d == 0` (d divides n evenly)
- Count how many digits pass the check

---

## 📌 Key Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `%` | Remainder after division | 12 % 2 = 0 ✅ |
| `!=` | Not equal to | 0 != 0 → False |
| `str()` | Convert int to string | str(12) → "12" |
| `int()` | Convert char to int | int("2") → 2 |

---

## 📌 Why Convert to String?
Converting `n` to a string is the easiest way to loop over each digit individually.

```
n = 2446
str(2446) → "2446"
loop      → "2", "4", "4", "6"
int(d)    →  2,   4,   4,   6
```

---

## 📌 Why Skip Zero?
Division by zero is **mathematically undefined**.
```
n % 0  →  ZeroDivisionError 💥
```
So we always check `int(d) != 0` before doing `n % int(d)`.

---

## 📌 Dry Run

### n = 2446
```
digits → [2, 4, 4, 6]

2446 % 2 = 0  ✅ count = 1
2446 % 4 = 2  ❌
2446 % 4 = 2  ❌ (same digit, checked again)
2446 % 6 = 4  ❌

Output → 1
```

### n = 12
```
digits → [1, 2]

12 % 1 = 0  ✅ count = 1
12 % 2 = 0  ✅ count = 2

Output → 2
```

### n = 23
```
digits → [2, 3]

23 % 2 = 1  ❌
23 % 3 = 2  ❌

Output → 0
```

---

## 📌 Generator Expression (used in solution)
```python
sum(1 for d in str(n) if int(d) != 0 and n % int(d) == 0)
```
- `for d in str(n)` → loop over each digit as character
- `if int(d) != 0` → skip zero digits
- `and n % int(d) == 0` → check divisibility
- `sum(1 for ...)` → count how many pass the condition

---

## 📌 Short Circuit Evaluation
In `int(d) != 0 and n % int(d) == 0`:
- If `int(d) != 0` is **False** → Python **skips** the second condition
- This prevents `ZeroDivisionError` automatically

```
d = "0"
int(d) != 0       → False
n % int(d) == 0   → never evaluated ✅
```

---

## 📌 Complexity
| | Value |
|---|---|
| **Time** | O(d) — d is number of digits, max 7 for n ≤ 10⁶ |
| **Space** | O(1) — no extra storage |

---

## 📌 Related Concepts to Explore
- [ ] Digit Extraction using Modulo vs String
- [ ] Short Circuit Evaluation
- [ ] Generator Expressions vs List Comprehensions
- [ ] Divisibility Rules
