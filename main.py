import sqlite3

conn = sqlite3.connect('shopdatabase.db')
cursor = conn.cursor()

def add_customers():
    customers_data = [
        ('Анна', 'Шевченко', 'shevcehko@gmail.com'),
        ('Володимир', 'Мельник', 'volodumur2@gmail.com'),
        ('Царів', 'Коваленко', 'chariv@gmail.com')
    ]
    for customer in customers_data:
        try:
            cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", customer)
        except sqlite3.IntegrityError:
            print(f"Пропускаємо дубльовану адресу: {customer[2]}")
    conn.commit()

def add_orders():
    orders_data = [
        (1, 1, 3, '2024-01-27'), 
        (2, 2, 2, '2024-01-27'), 
        (3, 3, 1, '2024-01-27')  
    ]
    cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)", orders_data)
    conn.commit()

def add_products():
    products_data = [
        ('Apple iPhone 12', 'смартфони', 23999.99),
        ('Samsung Galaxy S20', 'смартфони', 1999.99),
        ('Lenovo ThinkPad X1 Carbon', 'ноутбуки', 99999.99),
        ('Apple iPad Air', 'планшети', 20000.99)
    ]
    cursor.executemany("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", products_data)
    conn.commit()

def main_menu():
    while True:
        print("1. Додати клієнтів")
        print("2. Додати замовлення")
        print("3. Додати продукти")
        print("4. Завершити")
        choice = input("Оберіть опцію: ")
        if choice == "1":
            add_customers()
            print("Клієнти були успішно додані.")
        elif choice == "2":
            add_orders()
            print("Замовлення були успішно додані.")
        elif choice == "3":
            add_products()
            print("Продукти були успішно додані.")
        elif choice == "4":
            decision = input("Зберегти зміни у базі даних? (Так/Ні): ")
            if decision.lower() == "так":
                conn.commit()
                print("Зміни збережено.")
            break
        else:
            print("Недійсний вибір. Будь ласка, спробуйте ще раз.")
    conn.close()

if __name__ == "__main__":
    main_menu()
