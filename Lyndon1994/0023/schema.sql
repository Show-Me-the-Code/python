drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  name string not null,
  title string not null,
  text string not null,
  created_at integer not null
);