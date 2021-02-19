import hashlib
import os
import sqlite3


class AccountNotExists(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class AccountAlreadyExists(Exception):
    pass


class database:
    def __init__(self, filename="users.sqlite"):
        """
        Initialize db_module object for working with database.
        The connection will automatically closed after the
        object will be deleted by GC.

        :param filename: Name of .sqlite file with all data
        """

        self.connection = sqlite3.connect(filename)
        # Some const variables for module work
        self.SALT_SIZE = 32
        self.ITERATIONS_COUNT = 100000

    def __del__(self):
        """
        Method close the connection to db after this object will be deleted
        by GC. It is useful in order not to close the connection manually.
        """

        self.connection.close()

    def is_user_by_id_exists(self, value: int) -> bool:
        """
        Method checks whether the user exists or not

        :param value: Value of id column
        :return: True if user exists, false if not
        """

        # Check that account with this login doesn't exists
        QUERY = """
                SELECT * FROM users 
                WHERE id = ?
                """
        check_result = self.connection.cursor().execute(QUERY,
                                                        (value,)).fetchall()
        return len(check_result) != 0

    def get_password_hash_with_random_salt(self, password: str) -> bytes:
        """
        Method that returns byte sequence with salt and password hash inside

        :param password: The password to hash
        :return: Byte sequence with salt and password hash
        """

        # Salt for hash
        salt = os.urandom(self.SALT_SIZE)
        # Hash of given password
        password_hash = hashlib.pbkdf2_hmac("sha256",
                                            password.encode("utf-8"),
                                            salt,
                                            self.ITERATIONS_COUNT)
        '''
        The first part of the bytes is the salt for the hash the other part is
        the hash itself. For the separation, there is SIZE value, for example:
        salt, hash = byte_sequence[:SALT_SIZE], byte_sequence[SALT_SIZE:]
        '''
        return salt + password_hash

    def get_password_hash_by_salt(self, password: str, salt: bytes) -> bytes:
        """
        Method that returns password hash by given salt

        :param password: The password to hash
        :param salt: The salt for hash
        :return: Bytes of password hash
        """

        # Hash of given password by salt
        return hashlib.pbkdf2_hmac("sha256",
                                   password.encode("utf-8"),
                                   salt,
                                   self.ITERATIONS_COUNT)

    def get_user_id_from_db_by_form_data(self, login: str, password: str) -> int:
        """
        Method returns user id by given login and password.

        :exception AccountNotExists: if the user is not found
        :exception IncorrectPassword: if the passwords don't match
        :param login: Account's login
        :param password: The checked password in clear text, not a hash
        :return: User id
        """

        # Query to get id and hash with salt from account by given login
        QUERY = """
                SELECT id, password FROM users
                WHERE login = ?
                """
        # Id and hash with salt from account by given login
        db_data = self.connection.cursor().execute(QUERY,
                                                   (login,)).fetchone()
        if db_data is None:
            raise AccountNotExists

        # Because db_data[0] is id of user
        db_password = db_data[-1]

        # Salt from password in db
        db_salt = db_password[:self.SALT_SIZE]
        # Hash from password in db
        db_hash = db_password[self.SALT_SIZE:]

        # Hash of given password by salt from db
        current_hash = self.get_password_hash_by_salt(password, db_salt)

        # Comparing passwords
        if current_hash != db_hash:
            raise IncorrectPassword

        return db_data[0]

    def add_account_to_db(self, login: str, password: str, boards_json='') -> None:
        """
        Method add to database new user by given login and password

        :exception AccountAlreadyExists: if account with give login already exists
        :param login: Account's login
        :param password: The checked password in clear text, not a hash
        :param boards_json: The json with boards data from device
        """

        # Check that account with given login doesn't exists
        QUERY_FOR_CHECK = """
                          SELECT id FROM users
                          WHERE login = ?
                          """
        check_result = self.connection.cursor().execute(QUERY_FOR_CHECK,
                                                        (login,)).fetchall()
        if check_result:
            raise AccountAlreadyExists

        QUERY = """
                INSERT INTO users (login, password, boards)
                VALUES (?, ?, ?)
                """
        # Hash of given password (with salt)
        password_hash = self.get_password_hash_with_random_salt(password)
        self.connection.cursor().execute(QUERY,
                                         (login,
                                          password_hash,
                                          boards_json))
        self.connection.commit()

    def get_boards_json_by_user_id(self, user_id: int) -> str:
        """
        Method returns json with all boards data by given user id

        :exception AccountAlreadyExists: if account with given id not exists
        :param user_id: Id of user
        """

        if not self.is_user_by_id_exists(user_id):
            raise AccountNotExists

        QUERY = """
                SELECT boards FROM users
                WHERE id = ?
                """
        result = self.connection.cursor().execute(QUERY,
                                                  (user_id,)).fetchone()
        return result[0]

    def update_boards_json_by_user_id(self, user_id: int, new_json: str) -> None:
        """
        Method updates json with all boards data by given user id

        :exception AccountNotExists: if account by given id not exists
        :param user_id: Id of user
        :param new_json: New json value
        """

        if not self.is_user_by_id_exists(user_id):
            raise AccountNotExists

        QUERY = """
                UPDATE users
                SET boards = ?
                WHERE id = ?
                """
        self.connection.cursor().execute(QUERY,
                                         (new_json, user_id,))
        self.connection.commit()
