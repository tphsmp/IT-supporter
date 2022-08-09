import sqlite3


class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    # Проверка наличия в БД пользователя
    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    # Добавление пользователя в БД
    def add_user(self, user_id, first_name, last_name, message):
        self.cursor.execute('INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `message`) VALUES (?, ?, ?, ?)',
                            (user_id, first_name, last_name, message))
        return self.conn.commit()

    # Проверка отсутвия пользователя в БД и запись в БД
    def user_recorder(self, user_id, first_name, last_name, message):
        if not Database.user_exists(self, user_id):
            Database.add_user(self, user_id, first_name, last_name, message)

    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()
