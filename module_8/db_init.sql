use pysports;
SHOW databases;
CREATE USER 'test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'TEST';
GRANT ALL PRIVILEGES ON pysports.* TO 'test'@'localhost';
DROP USER IF EXISTS 'test'@'localhost';
CREATE TABLE team (
    team_id INT NOT NULL AUTO_INCREMENT,
    team_name varchar(75) NOT NULL,
    mascot varchar(75) NOT NULL,
    PRIMARY KEY(team_id) 
);
CREATE TABLE player (
    player_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(75) NOT NULL,
    last_name varchar(75) NOT NULL,
    team_id int NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)    
);
SHOW TABLES;
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizard');
INSERT INTO player(first_name, last_name, team_id)
    VALUES('Thorin', 'Oakenshield', 1);

SELECT team_id FROM team WHERE team_name= 'Team Sauron';
SHOW TABLES;

use pysports;
UPDATE team SET mascot = 'Orcs' WHERE team_id = '2'