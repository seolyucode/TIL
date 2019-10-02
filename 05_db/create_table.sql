-- SQLite

CREATE TABLE classmates(
    -- id INTEGER PRIMARY KEY, -- id에 뭐 들어감
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id에 NULL
    name TEXT NOT NULL,  --  NOT NULL 비면 안됨
    age INT NOT NULL,
    address TEXT NOT NULL
);