import mysql.connector
from datasets.formatting import query_table

global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="assiaemad",
    database="chatbot_db"
)

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id:int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None

def get_next_order_id():
    cursor = cnx.cursor()
    # the query for getting the maw id :
    query = f"SELECT max(order_id) from orders"

    cursor.execute(query)
    # extracting the value from the cursor :
    result = cursor.fetchone()
    # closing the cursor
    cursor.close()
    if result:
        return result[0] + 1
    return 1



def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()

        # calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        # commiting the changes & closing the cursor
        cnx.commit()
        cursor.close()
        print("order item inserted successfully")

        return 1
    except mysql.connector.Error as err:
        print(f"Error inserting the order item: {err}")

        # rollaback changes if necesary
        cnx.rollback()

        return -1
    except Exception as e:
        print(f"An error occured: {e}")
        cnx.rollback()

        return -1

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # calling the stored fct to calculate the total price :

    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)
    # extract the result from the cursor
    result = cursor.fetchone()[0]

    cursor.close()

    return result


def insert_order_tracking(next_order_id, status):
    cursor = cnx.cursor()

    query = "INSERT into order_tracking(order_id, status) VALUES (%s, %s)"

    cursor.execute(query, (next_order_id, status))

    cnx.commit()

    cursor.close()


def delete_failed_order(order_id):
    cursor = cnx.cursor()
    query = "DELETE FROM orders WHERE order_id = %s"

    cursor.execute(query, (order_id,))  # Pass a tuple with a comma (important for single parameters)

    # Check if any rows were deleted
    if cursor.rowcount == 0:
        print(f"No rows found with order_id = {order_id}.")
    else:
        print(f"Deleted {cursor.rowcount} row(s) with order_id = {order_id}.")

    cnx.commit()
    cursor.close()


if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    # print(get_next_order_id())
    print(get_order_status(41))