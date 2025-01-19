import sqlite3
import random
import string


class PasswordManagerBE:
    def __init__(self):
        """
        Initialize the database and create the 'Passwords' table if it doesn't exist.
        """
        connection = sqlite3.connect("password_data.db")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Passwords
                        (Id INTEGER PRIMARY KEY AUTOINCREMENT, Website TEXT,
                        Email TEXT, Password TEXT)""")
        connection.commit()
        connection.close()

    def save_data(self, website, email, password):
        """
        Save the provided website, email, and password into the database.

        Args:
            website (str): The website name.
            email (str): The email address.
            password (str): The password.
        """
        connection = sqlite3.connect("password_data.db")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Passwords (Website, Email, Password)
                        VALUES (?, ?, ?)""", (website, email, password))
        connection.commit()
        connection.close()

    def search_password(self, website):
        """
        Search for a website's credentials in the database.

        Args:
            website (str): The website name.

        Returns:
            tuple: The result containing the website, email, and password, or None if not found.
        """
        connection = sqlite3.connect("password_data.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Passwords WHERE Website = ?""", (website,))
        result = cursor.fetchone()
        connection.close()
        return result

    def create_password(self, length=15):
        """
        Generate a random password.

        Args:
            length (int): The length of the password (default: 15).

        Returns:
            str: The generated password.
        """
        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?/"
        return ''.join(random.choice(characters) for _ in range(length))
