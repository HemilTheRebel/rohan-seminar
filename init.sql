create table users ( 
    id serial primary key, 
    username varchar(255) unique not null, 
    password text null, 

    -- Optional columns --
    email text, 
    phone_number varchar(10) 
);