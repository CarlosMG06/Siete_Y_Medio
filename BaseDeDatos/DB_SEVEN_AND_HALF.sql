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

CREATE TABLE game(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
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
	deck_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(id),
	suit VARCHAR(10) NOT NULL,
    real_value INT UNSIGNED NOT NULL,
    PRIMARY KEY (deck_id, suit, real_value),
    value_in_game INT UNSIGNED NOT NULL
);

CREATE TABLE round_player(
	game_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (game_id) REFERENCES game(id),
    round_number INT NOT NULL,
    player_id VARCHAR(9) NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player(id),
	PRIMARY KEY (game_id, round_number, player_id),
	start_points INT UNSIGNED NOT NULL,
    end_points INT UNSIGNED NOT NULL,
    bet_amount INT UNSIGNED
);

CREATE VIEW v_game AS
	SELECT 
		g.id, g.start_time, g.end_time, g.deck_id, 
		count(DISTINCT pg.player_id) AS player_count,
        count(DISTINCT rp.round_number) AS round_count
    FROM game g LEFT JOIN player_game pg ON g.id = pg.game_id
				LEFT JOIN round_player rp ON g.id = rp.game_id
	GROUP BY g.id;

/*
SELECT sum(timestampdiff(MINUTE, vg.start_time, vg.end_time)) 
        FROM player p JOIN player_game pg ON p.id = pg.player_id
					  JOIN v_game vg ON pg.game_id = vg.game_id
GROUP BY vg.game_id;

CREATE VIEW v_ranking AS
	SELECT 
		p.id as player_id,
        p.player_name,
        count(DISTINCT pg.game_id) AS games_played,
        (
        SELECT sum(timestampdiff(MINUTE, g.start_time, g.end_time)) 
        FROM player p JOIN player_game pg ON p.id = pg.player_id
					  JOIN v_game vg ON pg.game_id
        ) AS minutes_played
	SELECT player p JOIN player_game pg ON p.id = pg.player_id
					JOIN
*/