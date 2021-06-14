CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--Command to create food table--
CREATE TABLE IF NOT EXISTS Food (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name VARCHAR ( 25 )  NOT NULL,
  carb REAL CHECK(carb>0) NOT NULL ,
  protein REAL CHECK(protein>0) NOT NULL,
  fat REAL CHECK(fat>0) NOT NULL
  --calories REAL GENERATED ALWAYS AS (carb*4 + protein*4 + fat*9) STORED--
);

--Command to create meal table--
CREATE TABLE IF NOT EXISTS Meal(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    meal_time DATE NOT NULL,
    meal_desc VARCHAR (25) NOT NULL,
    intake INTEGER[] 
);

--Command to create access table--
CREATE TABLE  IF NOT EXISTS Access(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    --access_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP--
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

--Command to create account table--
CREATE TABLE IF NOT EXISTS Account(
    uuid uuid DEFAULT uuid_generate_v4() NOT NULL,
    account_name VARCHAR(25) NOT NULL,
    first_name VARCHAR (25) NOT NULL,
    last_name VARCHAR (25) NOT NULL,
    email VARCHAR (50) UNIQUE NOT NULL,
    --pasword VARCHAR (25) NOT NULL,--
    gender VARCHAR (1) NOT NULL CONSTRAINT gender_check CHECK(gender IN ('m','f')),
    birthday DATE NOT NULL,
    height REAL NOT NULL,
    weight REAL NOT NULL,
    meal INTEGER [] 
);

--Command to create Genre table--
/*CREATE TABLE Genre(
    sport_id INTEGER PRIMARY KEY,
    is_outdoor BOOLEAN DEFAULT FALSE,
    is_indoor BOOLEAN DEFAULT FALSE,
    is_static BOOLEAN DEFAULT FALSE,
    is_dynamic BOOLEAN DEFAULT FALSE,
    is_interactive BOOLEAN DEFAULT FALSE,
    is_pesronal BOOLEAN DEFAULT FALSE,
    is__ball BOOLEAN DEFAULT FALSE
);*/
CREATE TABLE IF NOT EXISTS Genre(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    description VARCHAR(25) NOT NULL
);

--Command to create sports & genre mapping--
CREATE TABLE IF NOT EXISTS SportsGenre(
    sport_id INTEGER PRIMARY KEY,
    genre_id INTEGER []
);

--Command to create sport table--
CREATE TABLE IF NOT EXISTS Sport(
    sport_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    sport_name VARCHAR(25) NOT NULL,
    calories_burned_per_hr REAL NOT NULL,
    basic_continuous_time REAL NOT NULL
);

--Command to create event table--
CREATE TABLE IF NOT EXISTS Event(
    event_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    event_name VARCHAR(25) NOT NULL,
    host uuid NOT NULL,
    location VARCHAR(25) NOT NULL,
    time Date NOT NULL,
    min_participants REAL CHECK (min_participants >1),
    event_contents INTEGER[] --CHECK (cardinality(event_contents) >0)--
);

--Command to create event content--
CREATE TABLE IF NOT EXISTS Event_Content(
    content_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    serial INTEGER NOT NULL,
    sport_id INTEGER NOT NULL,
    duration INTERVAL NOT NULL
);

--Command to create event_participant table--
CREATE TABLE IF NOT EXISTS Event_Participants(
    event_id INTEGER PRIMARY KEY NOT NULL,
    participants uuid []
);
