DROP DATABASE IF EXISTS seven_and_half;
CREATE DATABASE seven_and_half CHARACTER SET utf8mb4;
USE seven_and_half;

CREATE TABLE player(
	id VARCHAR(9) PRIMARY KEY,
	player_name VARCHAR(30) NOT NULL,
	is_human BOOL NOT NULL,
    risk_type INT UNSIGNED NOT NULL
);

CREATE TABLE deck(
	id VARCHAR(5) PRIMARY KEY,
    deck_description VARCHAR(50)
);

CREATE TABLE card(
	id VARCHAR(3) PRIMARY KEY,
	suit VARCHAR(10) NOT NULL,
    real_value INT UNSIGNED AS(CAST(SUBSTR(id, -1, 2) AS DECIMAL)),
    value_in_game INT UNSIGNED AS(IF(real_value>7, 0.5, real_value)) STORED
);

CREATE TABLE deck_card(
	card_id VARCHAR(3) NOT NULL,
    FOREIGN KEY (card_id) REFERENCES card(id),
	deck_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(id)
);

CREATE TABLE cardgame(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    players INT UNSIGNED NOT NULL,
	start_time DATETIME NOT NULL,
    rounds INT UNSIGNED NOT NULL,
    end_time DATETIME NOT NULL,
    deck_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(id)
);

CREATE TABLE player_game(
	game_id INT UNSIGNED NOT NULL,
    player_id VARCHAR(9) NOT NULL,
	FOREIGN KEY (game_id) REFERENCES cardgame(id),
    FOREIGN KEY (player_id) REFERENCES player(id),
    PRIMARY KEY (game_id, player_id),
    initial_card_id VARCHAR(3) NOT NULL,
    FOREIGN KEY (initial_card_id) REFERENCES card(id),
    starting_points INT NOT NULL,
    ending_points INT NOT NULL
);

CREATE TABLE player_game_round(
	game_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (game_id) REFERENCES cardgame(id),
    round_number INT NOT NULL,
    player_id VARCHAR(9) NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player(id),
	PRIMARY KEY (game_id, round_number, player_id),
    is_bank BOOL NOT NULL,
	bet_amount INT UNSIGNED,
	starting_points INT NOT NULL,
    #  cards_value INT UNSIGNED NOT NULL,
    ending_points INT NOT NULL
);