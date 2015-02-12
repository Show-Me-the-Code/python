drop table if exists message_board;
create table message_board (
    id integer primary key autoincrement,
    username varchar(64) not null,
    message text not null,
    time datetime not null
);
