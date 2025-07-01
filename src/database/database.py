import sqlite3
import json

class CharacterDatabase:
    def __init__(self, db_path='characters.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                user_id INTEGER PRIMARY KEY,
                character_data TEXT
            )
        ''')
        self.conn.commit()

    def save_character(self, user_id, character):
        cursor = self.conn.cursor()
        character_json = json.dumps(character)
        cursor.execute('''
            REPLACE INTO characters (user_id, character_data) 
            VALUES (?, ?)
        ''', (user_id, character_json))
        self.conn.commit()

    def load_character(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT character_data FROM characters WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return json.loads(result[0]) if result else None

    def close(self):
        self.conn.close()
