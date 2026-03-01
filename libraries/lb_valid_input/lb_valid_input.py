def numberinput(prompt=">>> ", min_val=None, max_val=None):
    """Asks for a number with optional range check."""
    while True:
        data = input(prompt).strip().replace(",", ".")
        try:
            val = float(data)
            if val.is_integer():
                val = int(val)
            if min_val is not None and val < min_val:
                print(f"Error: Min value is {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Error: Max value is {max_val}")
                continue
            return val
        except ValueError:
            print("Error: Enter a valid number.")

def choiceinput(question, choices):
    """
    Automatically formats the prompt as: Question (Choice1, Choice2): 
    Example: choiceinput("Закрыть счет?", ["Да", "Нет"])
    """
    # Создаем строку вариантов для промпта: "Да, Нет"
    options_str = ", ".join(choices)
    full_prompt = f"{question} ({options_str}): "
    
    # Список для проверки (в нижнем регистре)
    valid_choices = [str(c).lower() for c in choices]
    
    while True:
        data = input(full_prompt).strip().lower()
        if data in valid_choices:
            # Возвращаем тот вариант, который совпал (в оригинальном регистре)
            index = valid_choices.index(data)
            return choices[index]
        print(f"Error: Please choose from {options_str}")

def rangeinput(prompt, start, end):
    """Shortcut for range check."""
    return numberinput(prompt, min_val=start, max_val=end)
