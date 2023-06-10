from models import User, Audio


class PostgresSaver:
    def __init__(self, pg_conn):
        self.pg_conn = pg_conn

    def save_user(self, user: User) -> None:
        self._insert_data('users', user)

    def save_mp3(self, audio: Audio) -> None:
        self._insert_data('audios', audio)

    def _insert_data(self, table: str, extract_data: User | Audio) -> None:
        cursor = self.pg_conn.cursor()
        fields_table = extract_data.__fields__

        str_fields = ','.join(field for field in fields_table)
        str_s = ','.join('%s' for _ in fields_table)

        args = cursor.mogrify(f"({str_s})", tuple(extract_data.__dict__.values())).decode()

        query_str = f"""INSERT INTO content.{table}
            ({str_fields})
            VALUES {args}
            ON CONFLICT (id) DO NOTHING;"""

        cursor.execute(query_str)


class PostgresReader:
    def __init__(self, pg_conn):
        self.pg_conn = pg_conn

    def get_mp3(self,mp3_id: str, user_id: str):
        query_str = f"""
        select
            a.mp3 as mp3
        from content.audios as a
        where a.id = '{mp3_id}' and a.user_id = '{user_id}' 
        """
        cursor = self.pg_conn.cursor()
        cursor.execute(query_str)
        rec = cursor.fetchone()
        if rec:
            path_to_mp3 = f"mp3/{mp3_id}.mp3"
            with open(path_to_mp3, "wb") as binary_file:
                binary_file.write(dict(rec)['mp3'])
        else:
            path_to_mp3 = None

        return path_to_mp3


class PostgresChecker:
    def __init__(self, pg_conn):
        self.pg_conn = pg_conn

    def check_user_token(self, user_id: str, token: str) -> bool:
        cursor = self.pg_conn.cursor()
        exists_query = f'''
            select exists (
                select 1
                from content.users
                where id = '{user_id}' and token = '{token}' 
            )'''
        cursor.execute(exists_query)
        return cursor.fetchone()[0]


