import json
import mysql.connector

def insert_data_from_json_to_database(json_file, database_name):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="m65s76Fg.",
        database=database_name
    )
    cursor = connection.cursor()

    for product in data:
        query = "INSERT INTO petlebi (product_id, product_name, product_price, product_stock, product_category, product_brand, product_url, product_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (product['product_id'], product['product_name'], product['product_price'], product['product_stock'], product['product_category'], product['product_brand'], product['product_url'], product['product_image'])
        cursor.execute(query, values)

    connection.commit()
    connection.close()

    

if __name__ == "__main__":
    json_file = "petlebi_products.json"
    database_name = "petlebidatabase"
    insert_data_from_json_to_database(json_file, database_name)
