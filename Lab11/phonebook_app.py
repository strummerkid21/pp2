import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="phonebook",
        user="postgres",
        password="1234",
        port=5432
    )

def search_pattern(cur):
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_or_update(cur, con):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
    con.commit()
    print("Inserted or updated.")

def bulk_insert(cur, con):
    names = input("Enter names (comma separated): ").split(',')
    surnames = input("Enter surnames (comma separated): ").split(',')
    phones = input("Enter phones (comma separated): ").split(',')
    if len(names) != len(phones) or len(names) != len(surnames):
        print("Mismatched list lengths!")
        return
    cur.execute("CALL bulk_insert_users(%s, %s, %s)", (names, surnames, phones))

    con.commit()
    print("Bulk insert completed.")

def get_page(cur):
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user(cur, con):
    mode = input("Delete by name or phone? (n/p): ").strip().lower()
    if mode == 'n':
        name = input("Enter name: ")
        cur.execute("CALL delete_user(%s, NULL)", (name,))
    elif mode == 'p':
        phone = input("Enter phone: ")
        cur.execute("CALL delete_user(NULL, %s)", (phone,))
    else:
        print("Invalid option.")
        return
    con.commit()
    print("Deleted user.")

def main():
    con = connect()
    cur = con.cursor()
    
    menu = '''\nChoose an option:
1. Search pattern
2. Insert or update user
3. Bulk insert users
4. Get paginated data
5. Delete user
6. Exit
'''

    while True:
        choice = input(menu).strip()
        if choice == '1':
            search_pattern(cur)
        elif choice == '2':
            insert_or_update(cur, con)
        elif choice == '3':
            bulk_insert(cur, con)
        elif choice == '4':
            get_page(cur)
        elif choice == '5':
            delete_user(cur, con)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

    cur.close()
    con.close()

if __name__ == '__main__':
    main()
