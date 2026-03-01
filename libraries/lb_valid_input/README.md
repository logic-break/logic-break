
# lb_valid_input
© Copyright logic-break 2026

https://github.com/logic-break/logic-break/tree/main/libraries/lb_valid_input

> lib made for lazy, by lazy  

installation:

    pip install lb-valid-input

**NOTE: in code, you must import lb_valid_input**


# Usage:

**`.numberinput(prompt, min_val, max_val)`** Safely gets a number (int/float). Prevents crashes from text input and checks optional min/max range.
**`.choiceinput(question, choices)`** Asks a question with a list of options. Forces the user to pick one from the list (case-insensitive). 
**`.choiceinput(question, choices)`** Asks a question with a list of options. Forces the user to pick one from the list (case-insensitive).

# Example:
```
import lb_valid_input as lbi

# It will ask "What do you want to do? (Deposit, Withdraw, Exit)"
action = lbi.choiceinput("What do you want to do?", ["Deposit", "Withdraw", "Exit"])

if action == "Deposit":
    amount = lbi.numberinput("Enter amount to deposit: ", min_val=0.01)
    print(f"Successfully deposited ${amount}")

elif action == "Withdraw":
    amount = lbi.rangeinput("Enter amount to withdraw (10-1000): ", 10, 1000)
    print(f"Please take your ${amount}")

else:
    print("Goodbye!")
```
