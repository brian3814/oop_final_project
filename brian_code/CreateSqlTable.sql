CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--Command to create food table--
CREATE TABLE Food (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  food_name VARCHAR ( 25 )  NOT NULL,
  carb REAL CHECK(carb>0) NOT NULL ,
  protein REAL CHECK(protein>0) NOT NULL,
  fat REAL CHECK(fat>0) NOT NULL
  --calories REAL GENERATED ALWAYS AS (carb*4 + protein*4 + fat*9) STORED--
);

--Command to create meal table--
CREATE TABLE Meal(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    account uuid NOT NULL,
    meal_time DATE NOT NULL,
    meal_desc VARCHAR (25) NOT NULL,
    intake INTEGER NOT NULL
);

--Command to create access table--
CREATE TABLE Access(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
);

--Command to create account table--
CREATE TABLE Account(
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    account_name VARCHAR (25) NOT NULL,
    email VARCHAR (50) UNIQUE NOT NULL,
    pasword VARCHAR (25) NOT NULL,
    gender VARCHAR (1) NOT NULL CONSTRAINT gender_check CHECK(gender IN ('m','f')),
    birthday DATE NOT NULL,
    height REAL NOT NULL,
    weight REAL NOT NULL
);

--Command to create Genre table--
CREATE TABLE Genre(
    sport_id INTEGER PRIMARY KEY,
    is_outdoor BOOLEAN DEFAULT FALSE,
    is_indoor BOOLEAN DEFAULT FALSE,
    is_static BOOLEAN DEFAULT FALSE,
    is_dynamic BOOLEAN DEFAULT FALSE,
    is_interactive BOOLEAN DEFAULT FALSE,
    is_pesronal BOOLEAN DEFAULT FALSE,
    is__ball BOOLEAN DEFAULT FALSE
);

--Command to create sport table--
CREATE TABLE Sport(
    sport_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    sport_name VARCHAR(25) NOT NULL,
    calories_burned_per_hr REAL NOT NULL,
    basic_continuous_time REAL NOT NULL
);

--Command to create event table--
CREATE TABLE Event(
    event_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    event_name VARCHAR(25) NOT NULL,
    host uuid NOT NULL,
    location VARCHAR(25) NOT NULL,
    time Date NOT NULL,
    min_participants REAL CHECK (min_participants >1)
);

