# ---Self Assessment Questions---
# 1) The first bug I spotted was a logic error on line 6. On that line, the code set total to sale, wiping out the running sum with each iteration instead of adding to it. I found this while working alone, stepping through the loop line by line, and saying the values out loud before I even looked at any error tracebacks or asked AI. This shows that my debugging instincts are already tuned to find logic and state-tracking flaws, not just to depend on automated syntax error messages.
# 2) The apply_discount function takes a price and a tier, working out the final price by applying a discount that depends on the tier. I can use apply_discount without looking at the code, as long as the function has clear docstrings and type hints that tell me what tier strings or values are allowed.
# 3) # AI Disclosure: AI assistance was utilized to explain error tracebacks, verify scoping concepts, and refine debugging reflections. Using AI built my understanding rather than shortcutting it because I used it as an explainer to understand why specific tracebacks occurred (like IndexError and SyntaxError) only after I had already traced the code manually. This verified my reasoning and reinforced a structured, four-step debugging process that I can apply independently in future coding tasks.


# ---Exercise 1---
def calculate_tax(price, rate):
    return price * rate

tax_1 = calculate_tax(100, 0.07)
tax_2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax_1:.2f}")
print(f"Tax on $250 at 8%: ${tax_2:.2f}")

# ---Exercise 2---
def apply_discount(price, tier):
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price

price = 200
print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")

# ---Exercise 3---
def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price

initial_price = 200
discounted = apply_discount(initial_price, "gold")
tax_amount = calculate_tax(discounted, 0.07)
final_val = discounted + tax_amount

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${final_val:.2f}")

def final_price(price, tier, tax_rate):
    disc_price = apply_discount(price, tier)
    tax = calculate_tax(disc_price, tax_rate)
    return disc_price + tax

result = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${result:.2f}')

# ---Exercise 4---
def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price

def final_price(price, tier, tax_rate):
    disc_price = apply_discount(price, tier)
    tax = calculate_tax(disc_price, tax_rate)
    return disc_price + tax

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# ---Exercise 5---

#--- STEP 1: SOLO DEBUG (Identified Bugs & Rubber Duck Tracing) ---
#1. Bug 1 (Logic Error on Line 6): 
   #- Issue: `total = sale` overwrites the running total on each iteration. 
   #- Fix needed: It should accumulate using `total += sale`.
#2. Bug 2 (Syntax Error on Line 10): 
   #- Issue: The `for sale in sales` loop is missing a trailing colon (`:`).
#3. Bug 3 (Index/Off-by-One Error on Line 15): 
   #- Issue: `while i <= len(sales):` uses `<=` which tries to access `sales[5]`, raising an `IndexError`. 
   #- Fix needed: It should use strict inequality `while i < len(sales):`.


#--- STEP 2: AI EXPLAINER (Error Meanings) ---
#- SyntaxError: expected ':'
  #Meaning: Python expects a colon at the end of compound statements (like loops or conditionals) to indicate the start of an indented code block.
#- IndexError: list index out of range
  #Meaning: The code attempted to access a position in a list that does not exist (since lists are 0-indexed, the valid range for a 5-item list is 0 to 4).


#--- STEP 3: FIX IT YOURSELF (Corrected Code & Comments) ---
sales = [120, 80, 250, 175, 90]

# --- Block 1: Accumulate total sales instead of reassigning ---
total = 0
for sale in sales:
    total += sale
print(f"Total: \${total}")

# --- Block 2: Added missing colon to the for loop ---
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# --- Block 3: Changed <= to < to avoid index out of range ---
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
#--- STEP 4: CLASS DEBRIEF ---
#The error tracebacks pinpointed the exact lines and reasons for the SyntaxError and IndexError. Tracing the variables out loud also correctly exposed the logic flaw where the total was being overwritten instead of summed up.

# ---Exercise 6---

# Scope Explanation (in your own words):
# Python uses scoping. Variables created at the module level have **global** scope. When a function makes a variable with the **same** name (`x = 999`), it makes a **different,** separate local variable inside that **function's** namespace. Changing or giving a value to a **local** variable does not change the global variable of the same name unless it is specifically marked using the 'global' keyword.

x = 100  # global variable

def double_it():
    x = 999  # local variable – different from global x!
    return x * 2

print(x)                  # Prints: 100 (accesses the global variable x)
print(double_it())        # Prints: 1998 (computes 999 * 2 using the local variable x)
print(x)                  # Prints: 100 (global variable x is unaffected by the local assignment)