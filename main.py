import os

FILENAME = "travel_diary.txt"

def add_entry():
    date = input("Дата (YYYY-MM-DD): ")
    location = input("Локація: ")
    text = input("Текст: ")

    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"Дата: {date}\nЛокація: {location}\nТекст: {text}\n---\n")

    print("Запис додано!")

def search_entries():
    query = input("Введіть дату або ключове слово для пошуку: ").lower()
    if not os.path.exists(FILENAME):
        print("Файл щоденника не знайдено.")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        entries = f.read().split("---\n")
        matches = [e for e in entries if query in e.lower()]
        if matches:
            print("\nЗнайдені записи:")
            for entry in matches:
                print(entry.strip(), "\n")
        else:
            print("Нічого не знайдено.")

def analyze_diary():
    if not os.path.exists(FILENAME):
        print("Файл щоденника не знайдено.")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        entries = f.read().split("---\n")
        entries = [e.strip() for e in entries if e.strip()]

    locations = set()
    word_count = 0

    for entry in entries:
        lines = entry.splitlines()
        for line in lines:
            if line.startswith("Локація:"):
                locations.add(line.split(":", 1)[1].strip())
            elif line.startswith("Текст:"):
                text = line.split(":", 1)[1].strip()
                word_count += len(text.split())

    print(f"Кількість записів: {len(entries)}")
    print(f"Унікальних локацій: {len(locations)}")
    print(f"Загальна кількість слів: {word_count}")

def main():
    while True:
        print("\n=== ЩОДЕННИК МАНДРІВНИКА ===")
        print("1. Додати запис")
        print("2. Пошук записів")
        print("3. Аналітика")
        print("4. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries()
        elif choice == "3":
            analyze_diary()
        elif choice == "4":
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()
