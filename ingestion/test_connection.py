from database import get_connection

print("Opening connection...")

conn = get_connection()

print("Connected!")

conn.close()

print("Connection closed.")