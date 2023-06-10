import uuid
import datetime
import psycopg2
from psycopg2.extras import DictCursor, register_uuid

from models import User, Audio, POSTGRES_DSN
from db import PostgresSaver, PostgresChecker, PostgresReader


def create_user(name: str) -> dict:
    data_user = {
        'name': name,
        'id': uuid.uuid4(),
        'token': uuid.uuid4(),
        'created_at': datetime.datetime.now()
    }

    user = User(**data_user)

    with psycopg2.connect(**POSTGRES_DSN, cursor_factory=DictCursor) as pg_conn:
        try:
            register_uuid()
            pg_saver = PostgresSaver(pg_conn)
            pg_saver.save_user(user)
            print("data recorded successfully...")

        finally:
            if pg_conn.closed:
                pg_conn.close()

    return data_user


def create_mp3(file: bytes, user_id: str, token: str) -> dict:
    data_mp3 = {
        'id': uuid.uuid4(),
        'user_id': user_id,
        'mp3': file,
        'created_at': datetime.datetime.now()
    }

    audio = Audio(**data_mp3)

    with psycopg2.connect(**POSTGRES_DSN, cursor_factory=DictCursor) as pg_conn:
        try:
            pg_checker = PostgresChecker(pg_conn)
            if pg_checker.check_user_token(user_id, token):
                register_uuid()
                pg_saver = PostgresSaver(pg_conn)
                pg_saver.save_mp3(audio)
                print("data recorded successfully...")
                url = f"http://localhost:8000/record?id={audio.id}&user={audio.user_id}"
            else:
                url = {"error": True, "error_text": "Does't exist such user + token"}
        except Exception as ex:
            url = {"error": True, "error_text": str(ex)}
        finally:
            if pg_conn.closed:
                pg_conn.close()
    return url


def get_mp3(mp3_id: str, user_id: str):
    with psycopg2.connect(**POSTGRES_DSN, cursor_factory=DictCursor) as pg_conn:
        try:
            pg_reader = PostgresReader(pg_conn)
            path_to_mp3 = pg_reader.get_mp3(mp3_id, user_id)
        except Exception as ex:
            path_to_mp3 = {"error": True, "error_text": str(ex)}
        finally:
            if pg_conn.closed:
                pg_conn.close()
    return path_to_mp3

