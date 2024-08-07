import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/macbook/practice_git_aqa/practice_autoqa' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_dateiled_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_invalid_data_type(self, product_id, name, description, qnt):
        try:
            query = f"INSERT products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
            self.cursor.execute(query)
            self.connection.commit()
            return "Insert successful"
        except Exception as e:
            return f"Error: {e}"
        
    def check_data_type(self, product_id, name, description, qnt):
        if isinstance(product_id, int) and isinstance(name, str) and isinstance(description, str) and isinstance(qnt, int):
            query = f"INSERT INTO products (id, name, description, quantity) \
                    VALUES ({product_id}, '{name}', '{description}', {qnt})"
            self.cursor.execute(query)
            self.connection.commit()
            return "Data type is valid"
        else:
            return "Invalid data type"
        
    def check_if_query_was_successful(self, product_id, name, description, qnt):
        try:
            query = f"INSERT INTO products (id, name, description, quantity) \
                        VALUES ({product_id}, '{name}', '{description}', {qnt})"
            self.cursor.execute(query)
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return "Query was successful"
            else:
                return "No rows were affected"
        except sqlite3.Error as e:
            return f"An error occurred: {e}"
   

   