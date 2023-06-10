-- CREATE DATABASE umusic_bewise;
-- psql -h 127.0.0.1 -U app -d umusic_bewise -f umusic_bewise_db.ddl

CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.users (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    token uuid NOT NULL,
    created_at timestamp with time zone
);


CREATE TABLE IF NOT EXISTS content.audios (
    id uuid PRIMARY KEY,
    user_id uuid NOT NULL,
    mp3 bytea,
    created_at timestamp with time zone,
    FOREIGN KEY (user_id) REFERENCES content.users (id) ON DELETE CASCADE
);



CREATE INDEX ON content.users (name, created_at);
