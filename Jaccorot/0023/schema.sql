DROP  TABLE  if EXISTS entries;
CREATE TABLE entries(
  id INTEGER PRIMARY KEY autoincrement,
  name text NOT NULL ,
  text text NOT NULL,
  time datetime NOT NULL
);