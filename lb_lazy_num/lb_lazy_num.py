"""
Lol russian guy made this lib, and why are you here ?
"""

import re

def format_num(val, prec=2):
    try:
        n = float(val)
    except:
        return str(val)

    # Fallback для слишком здоровых чисел
    if abs(n) >= 1e21:
        return str(val)

    sign = "-" if n < 0 else ""
    n = abs(n)
    
    # Идем по убывающей
    for limit, sfx in [(1e18, 'Qi'), (1e15, 'P'), (1e12, 'T'), 
                       (1e9, 'B'), (1e6, 'M'), (1e3, 'K')]:
        if n >= limit:
            # Считаем и убираем лишние нули одной строкой
            res = f"{n/limit:.{prec}f}".rstrip('0').rstrip('.')
            return f"{sign}{res}{sfx}"
    
    # Если число меньше тысячи
    res = f"{n:.{prec}f}".rstrip('0').rstrip('.')
    return f"{sign}{res}"

def convert_size(raw, to):
    # Коэффициенты 1024
    u_map = {u: 1024**i for i, u in enumerate(['B', 'KB', 'MB', 'GB', 'TB', 'PB'])}
    
    try:
        # Дергаем цифры и буквы, игнорим пробелы
        m = re.match(r"([0-9.]+)\s*([a-zA-Z]+)", raw.strip())
        if not m: return raw
            
        val, unit = float(m.group(1)), m.group(2).upper()
        to = to.upper()

        # Фиксим короткие записи типа 'M' или 'G'
        curr = unit if unit.endswith('B') or unit == 'B' else f"{unit}B"
        targ = to if to.endswith('B') or to == 'B' else f"{to}B"

        if curr not in u_map or targ not in u_map:
            return raw

        # Считаем через байты
        res = (val * u_map[curr]) / u_map[targ]

        # Красиво причесываем результат
        out = f"{res:.10f}".rstrip('0').rstrip('.') if res < 1 else f"{res:.2f}".rstrip('0').rstrip('.')
        return f"{out}{targ}"

    except:
        return raw
