import os
from datetime import datetime

def log_error(message: str) -> None:
    os.makedirs('log', exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join('log', 'input_errors.log')
    
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
    except IOError as e:
        
        print(f"⚠️ Не удалось записать ошибку в файл: {e}")

def validate_range(value: float, low: float, high: float):
    
    if value < low:
        return False, f"Значение {value} меньше минимально допустимого ({low})."
    if value > high:
        return False, f"Значение {value} больше максимально допустимого ({high})."
    return True, ""

def input_number(prompt: str, low: float, high: float) -> float:
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                print("Поле не может быть пустым! Повторите ввод.")
                continue
                
            value = float(raw)
        except ValueError:
            msg = f"Ошибка: введено не число ('{raw}')."
            print(msg)
            log_error(msg)  # Пишем в лог
            continue
        
        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        
        print(msg + " Повторите ввод.")
        log_error(msg)  # Пишем в лог

if __name__ == "__main__":
    print("--- Модель роста клеток ---")
    print("Все ошибки сохраняются в папку log/input_errors.log\n")

    a_float = input_number("Введите начальное количество клеток (≥1): ", low=1, high=1000)
    a = int(a_float) 

    interval_float = input_number("Введите интервал удвоения в часах (≥1 и ≤24): ", low=1, high=24)
    interval_hours = int(interval_float)
    total_time = input_number(f"Введите общее время в часах (минимум {interval_hours}): ", 
                              low=interval_hours, high=168)
    total_time = int(total_time)

    print("\nВремя (ч)\tКоличество клеток")
    print(f"{0}\t\t{a}")

    for t in range(interval_hours, total_time + 1, interval_hours):
        a *= 2
        print(f"{t}\t\t{a}")
    

