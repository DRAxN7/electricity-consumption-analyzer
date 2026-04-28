import mysql.connector
import pandas as pd

def load_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="judebellingham@5",
            database="electricity_analyzer"
        )
        if connection.is_connected():
            print("Connected to MySQL successfully")


        query = "SELECT * FROM consumption_data"
        df = pd.read_sql(query, connection)

        if df.empty:
            print("Warning:Table is empty")
            return None

        required_columns = ['consumption_kwh','peak_load_kwh','date']

        for column in required_columns:
            if column not in df.columns:
                print(f"Error:Missing column '{column}' in table")
                return None

        return df

    except mysql.connector.Error as err:
        print(f"MySQL Error:{err}")
        return None
    except Exception as e:
        print(f"Unexpected Error:{e}")
        return None
    finally:
        try:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("MySQL connection closed")
        except:
            pass
