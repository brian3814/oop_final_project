--Command to create food table--
CREATE TABLE IF NOT EXISTS Food (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  food_name VARCHAR ( 25 )  NOT NULL,
  carb REAL CHECK(carb>=0) NOT NULL ,
  protein REAL CHECK(protein>=0) NOT NULL,
  fat REAL CHECK(fat>=0) NOT NULL,
  calories REAL GENERATED ALWAYS AS (carb*4 + protein*4 + fat*9) STORED
);

INSERT INTO Food (food_name,carb,protein,fat)
VALUES
    ('蔥燒牛肉麵(1包)',23.3,9.7,18.1),
    ('統一肉燥麵(1包)',52.4,10.1,20.2),
    ('維力炸醬麵(1包)',59,11,21),
    ('雞肉滑蛋粥(1碗)',37.7,14.4,12.6),
    ('肉醬麵(1份)',60.7,17.8,14.2),
    ('叉燒包(1個)',46,7,3),
    ('肉絲麵(1碗)',75.7,25.6,13.3),
    ('滷肉飯(1碗)',102,21,18),
    ('甘蔗汁(1杯)',73,0,0),
    ('蘋果汁(1杯)',11,0.1,0.1),
    ('蔬菜汁(1罐)',18,0.1,0),
    ('寶礦力(1罐)',16.8,0,0),
    ('維大力(1罐)',24.4,0,0),
    ('全脂奶(一杯)',8,12,8),
    ('低脂奶(一杯)',8,12,4),
    ('脫脂奶(一杯)',8,12,0),
    ('香菇(100g)',15,0,0),
    ('蘿蔔(100g)',15,0,0),
    ('香蕉(一根)',15,0,0),
    ('富士蘋果(小)',15,0,0),
    ('木瓜(一顆)',45,0,0),
    ('apple',20,0,0),
    ('banana',30,0,0),
    ('orange',25,0,0),
    ('burger',50,20,15);


--Command to create meal table--
CREATE TABLE IF NOT EXISTS Meal(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    account_id INTEGER NOT NULL,
    meal_time TIMESTAMP NOT NULL,
    meal_desc VARCHAR (25) NOT NULL,
    intake INTEGER[]
);


INSERT INTO Meal(meal_desc,inTake,meal_time,account_id)
VALUES
    ('breakfirst','{1,2,8}','2020-10-10 08:30:30',1),
    ('lunch','{10,8,9}','2020-10-10 12:30:30',2),
    ('dinner','{15}','2020-10-10 18:30:30',3),
    ('breakfirst','{16,8,2}','2020-10-11 08:30:30',1),
    ('lunch','{1,2,3}','2020-10-11 12:30:30',2),
    ('dinner','{9,4,11}','2020-10-11 18:30:30',3),
    ('breakfirst','{5,12}','2020-10-12 08:30:30',1),
    ('lunch','{9,2}','2020-10-12 12:30:30',2),
    ('dinner','{3,4}','2020-10-12 18:30:30',3);


--Command to create access table--
CREATE TABLE  IF NOT EXISTS Access(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    level INTEGER  NOT NULL,
    --access_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP--
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

INSERT INTO Access (email, password, level)
VALUES ('Andy@email.com','22b1f2d414e57f030312bc8239b5449e',1),
    ('Paige@email.com','c371ae865fc676853cf9edf059adc13c',1),
    ('Julia@email.com','baa72de59cc663a75f5345e40533292c',1),
    ('Brian@email.com','98e74052d0db8b82de760cd7ab135f3c',1),
    ('guest','01f533aed3d60f81346edbe9173bd861',0);

--Command to create account table--
CREATE TABLE IF NOT EXISTS Account(
    id INTEGER NOT NULL PRIMARY KEY,
    account_type VARCHAR(25) NOT NULL,
    first_name VARCHAR (25) NOT NULL,
    last_name VARCHAR (25) NOT NULL,
    gender VARCHAR (10) NOT NULL,
    birthday DATE NOT NULL,
    height REAL NOT NULL,
    weight REAL NOT NULL,
    meals INTEGER [],
    hobbies INTEGER []
);

INSERT INTO Account (id,first_name,last_name,account_type,gender,birthday,weight,height)
VALUES 
    (1,'Andy','Andy','person','male','2000-01-01', 70,180),
    (2,'Paige','Peige','person','female','2000-02-01',45,170),
    (3,'Julia','Julia','person','female','2000-03-01',45,170),
    (4,'Brian','Brian','person','male','2000-04-01',65,175),
    (5,'guest','guest','person','male','1911-10-10',70,180);


CREATE TABLE IF NOT EXISTS Level(
    level_no INTEGER NOT NULL PRIMARY KEY,
    level_desc VARCHAR (25) NOT NULL,
    max_account_no INTEGER DEFAULT 1
);   

INSERT INTO Level (level_no,level_desc,max_account_no)
VALUES
(0,'guest',1),
(1,'user',2),
(2,'vip',3);

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

INSERT INTO Genre (description)
VALUES 
    ('notBALL'),
    ('isBALL'),
    ('Pearson'),
    ('Interactive'),
    ('Dynamic'),
    ('Static'),
    ('Outdoor'),
    ('Indoor');

--Command to create sports & genre mapping--
CREATE TABLE IF NOT EXISTS SportsGenre(
    sport_id INTEGER PRIMARY KEY,
    genre_id INTEGER []
);

INSERT INTO SportsGenre (sport_id,genre_id)
VALUES
    (1, '{8,6,4,2}'),
    (2, '{8,6,4,1}'),
    (3, '{8,6,3,2}'),
    (4, '{8,6,3,1}'),
    (5, '{8,5,4,2}'),
    (6, '{8,5,4,1}'),
    (7, '{8,5,3,2}'),
    (8, '{8,5,3,1}'),
    (9, '{7,6,4,2}'),
    (10,'{7,6,4,1}'),
    (11,'{7,6,3,2}'),
    (12,'{7,6,3,1}'),
    (13,'{7,5,4,2}'),
    (14,'{7,5,4,1}'),
    (15,'{7,5,3,2}'),
    (16,'{7,5,3,1}'); 

--Command to create sport table--
CREATE TABLE IF NOT EXISTS Sport(
    sport_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    sport_name VARCHAR(25) NOT NULL,
    calories_burned_per_hr REAL NOT NULL,
    basic_continuous_time REAL 
);

INSERT INTO Sport (sport_name,calories_burned_per_hr)
VALUES
    ('BowlingMorePeople',149),
    ('YogaMorePeople',124),
    ('BowlingSingle',149),
    ('YogaSingle',124),
    ('Badminton',224),
    ('Dancing',238),
    ('ShootingBaskets',224),
    ('Trampoline',174),
    ('GolfMorePeople',224),
    ('TaiChiMorePeople',199),
    ('GolfSingle',224),
    ('TaiChi',199),
    ('Baseball',249),
    ('RunMorePeople',398),
    ('BasketballSingle',398),
    ('RockClimbing',547),
    ('ActivityEND',0);

--Command to create event table--
CREATE TABLE IF NOT EXISTS Event(
    event_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    event_name VARCHAR(25) NOT NULL,
    host uuid NOT NULL,
    location VARCHAR(25) NOT NULL,
    time Date NOT NULL,
    min_participants REAL CHECK (min_participants >1),
    event_contents INTEGER[] 
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
