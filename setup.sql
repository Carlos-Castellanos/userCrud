-- Create the user table
-- DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),not null,
    last_name VARCHAR(45), not null,
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);

-- create table if not exists vehicles(
--   id integer primary key autoincrement,
--   id_user integer,
--   style text not null,
--   color text not null,
--   wheels integer not null
--   foreign key(id_user) references user(id)
-- );


-- Insert test records:

Insert into user (
    first_name, last_name, hobbies
)values (
    'John', 'smith', 'travel');
    
Insert into user (
    first_name, last_name, hobbies
)values (
    'Diana', 'McGrew', 'playing soccer');
    
Insert into user (
    first_name, last_name, hobbies
)values (
    'Donald', 'Olivier', 'climbing');


-- {
--     "id" : 8,
--     "first_name": "Ximena",
--     "last_name" : "Perez",
--     "hobbies": "playing soccer"
--  }