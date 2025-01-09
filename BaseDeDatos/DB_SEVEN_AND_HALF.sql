DROP DATABASE IF EXISTS seven_and_half;
CREATE DATABASE seven_and_half CHARACTER SET utf8mb4;
USE seven_and_half;

CREATE TABLE player(
	id VARCHAR(9) CONSTRAINT CHECK (CONVERT((SUBSTRING(id,1,8)) ) PRIMARY KEY,
	player_name VARCHAR(30) NOT NULL,
	is_human BOOL NOT NULL,
    risk_type INT UNSIGNED NOT NULL,
);

CREATE TABLE deck(
	id VARCHAR(5) PRIMARY KEY,
    deck_description VARCHAR(50)
);

CREATE TABLE game(
	id INT AUTO_INCREMENT PRIMARY KEY,
	start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    deck_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(id)
);

CREATE TABLE player_game(
	game_id INT UNSIGNED NOT NULL,
    player_id VARCHAR(9) NOT NULL,
	FOREIGN KEY (game_id) REFERENCES game(id),
    FOREIGN KEY (player_id) REFERENCES player(id),
    PRIMARY KEY (game_id, player_id)
);

CREATE TABLE card(
	suit VARCHAR(10) NOT NULL,
    real_value INT UNSIGNED NOT NULL,
    PRIMARY KEY (suit, real_value),
    value_in_game INT UNSIGNED NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(id)
);

CREATE TABLE player_round(
	FOREIGN KEY (partida_id) REFERENCES partida(id),
    FOREIGN KEY (jugador_id) REFERENCES jugador(id),
    ronda_num INT AUTO_INCREMENT NOT NULL,
	PRIMARY KEY (partida_id, jugador_id, ronda_num),
	puntos_iniciales INT UNSIGNED NOT NULL,
    puntos_finales INT UNSIGNED NOT NULL,
    apuesta INT UNSIGNED
);