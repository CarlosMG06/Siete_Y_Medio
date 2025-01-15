USE seven_and_half;

CREATE OR REPLACE VIEW v_ranking AS
	SELECT 
		p.id AS player_id,
		p.player_name,
		count(DISTINCT pg.game_id) AS games_played,
		sum(timestampdiff(MINUTE, cg.start_time, cg.end_time)) AS minutes_played
	FROM player p
		JOIN player_game pg ON p.id = pg.player_id
		JOIN cardgame cg ON pg.game_id = cg.id
	GROUP BY p.id, p.player_name;

# 1
CREATE OR REPLACE VIEW v_report_most_common_initial_card AS
	WITH CardCounts AS (
		SELECT 
			pg.player_id,
			c.suit,
			pg.initial_card_id,
			count(*) AS initial_card_count,
			(SELECT count(*) 
			 FROM player_game 
			 WHERE player_id = pg.player_id) AS games_played
		FROM player_game pg
		JOIN card c ON pg.initial_card_id = c.id
		GROUP BY pg.player_id, pg.initial_card_id, c.suit
	)
	SELECT 
		cc1.player_id,
		GROUP_CONCAT(DISTINCT cc1.suit ORDER BY cc1.initial_card_id) AS suits,
		GROUP_CONCAT(cc1.initial_card_id ORDER BY cc1.initial_card_id) AS most_common_initial_card_ids,
		cc1.initial_card_count,
		cc1.games_played
	FROM CardCounts cc1
	WHERE cc1.games_played >= 3
	GROUP BY cc1.player_id, cc1.initial_card_count, cc1.games_played
    HAVING cc1.initial_card_count = (
		SELECT max(cc2.initial_card_count)
		FROM CardCounts cc2
		WHERE cc2.player_id = cc1.player_id
	);

# 2
CREATE OR REPLACE VIEW v_report_highest_bet AS
	SELECT 
		pgr.game_id,
		GROUP_CONCAT(DISTINCT pgr.player_id ORDER BY pgr.player_id) AS player_ids,
		pgr.bet_amount AS highest_bet_amount
	FROM player_game_round pgr
	GROUP BY pgr.game_id, pgr.bet_amount
	HAVING pgr.bet_amount = (
			SELECT max(pgr2.bet_amount)
			FROM player_game_round pgr2
			WHERE pgr2.game_id = pgr.game_id
			);

# 3
CREATE OR REPLACE VIEW v_report_lowest_bet AS
	SELECT 
		pgr.game_id,
		GROUP_CONCAT(DISTINCT pgr.player_id ORDER BY pgr.player_id) AS player_ids,
		pgr.bet_amount AS lowest_bet_amount
	FROM player_game_round pgr
	GROUP BY pgr.game_id, pgr.bet_amount
	HAVING pgr.bet_amount = (
			SELECT min(pgr2.bet_amount)
			FROM player_game_round pgr2
			WHERE pgr2.game_id = pgr.game_id
			);

# 4
CREATE OR REPLACE VIEW v_report_round_win_percentage AS 
	WITH RoundsWon AS (
		SELECT pgr1.game_id, pgr1.player_id,
			sum(IF((pgr1.ending_points - pgr1.starting_points) = (
					SELECT max(ending_points - starting_points)
					FROM player_game_round pgr2
					WHERE pgr2.game_id = pgr1.game_id 
					  AND pgr2.round_number = pgr1.round_number),
					1, 0)
			) AS rounds_won
		FROM player_game_round pgr1
		GROUP BY pgr1.game_id, pgr1.player_id
	)
	SELECT 
		pgr.game_id,
		pgr.player_id,
		g.rounds,
		round(avg(pgr.bet_amount), 3) AS avg_bet,
		rw.rounds_won,
		round((rw.rounds_won / g.rounds * 100), 3) AS round_win_percentage
	FROM player_game_round pgr
		JOIN cardgame g ON pgr.game_id = g.id
		JOIN RoundsWon rw ON pgr.game_id = rw.game_id 
                          AND pgr.player_id = rw.player_id
	GROUP BY pgr.game_id, pgr.player_id, g.rounds, rw.rounds_won;
	
# 5
CREATE OR REPLACE VIEW v_report_bot_wins AS
	SELECT 
		pg.game_id,
		(pg.ending_points - pg.starting_points) AS points_gained_by_winning_bot
	FROM player_game pg
		JOIN player p ON pg.player_id = p.id
	WHERE p.is_human = FALSE
	  AND (pg.ending_points - pg.starting_points) = (
		  SELECT max(ending_points - starting_points)
		  FROM player_game
		  WHERE game_id = pg.game_id
		  )
	ORDER BY pg.game_id;
        
# 6
# 6.1
CREATE OR REPLACE VIEW v_report_bank_wins_per_player AS
	SELECT 
		pgr1.game_id,
        pgr1.player_id,
		sum(IF(pgr1.is_bank = True 
				 AND (pgr1.ending_points - pgr1.starting_points) = (
					   SELECT MAX(ending_points - starting_points)
					   FROM player_game_round pgr2
					   WHERE pgr2.game_id = pgr1.game_id 
						 AND pgr2.round_number = pgr1.round_number
				     ), 1, 0)
		) AS rounds_won_as_bank
	FROM player_game_round pgr1
    WHERE pgr1.is_bank = True
	GROUP BY pgr1.game_id, pgr1.player_id;
# 6.2
CREATE OR REPLACE VIEW v_report_bank_wins AS
	SELECT 
		pgr1.game_id,
		sum(IF(pgr1.is_bank = True 
				 AND (pgr1.ending_points - pgr1.starting_points) = (
					   SELECT MAX(ending_points - starting_points)
					   FROM player_game_round pgr2
					   WHERE pgr2.game_id = pgr1.game_id 
						 AND pgr2.round_number = pgr1.round_number
				     ), 1, 0)
		) AS rounds_won_by_bank
	FROM player_game_round pgr1
	GROUP BY pgr1.game_id;

# 7
CREATE OR REPLACE VIEW v_report_bank_players AS
	SELECT game_id, count(DISTINCT player_id) AS bank_players_count
    FROM player_game_round
    WHERE is_bank = True
    GROUP BY game_id;

# 8
CREATE OR REPLACE VIEW v_report_avg_bet AS
	SELECT game_id, round(avg(bet_amount), 3) AS avg_bet
    FROM player_game_round
    GROUP BY game_id;
# 9
CREATE OR REPLACE VIEW v_report_avg_bet_1st_round AS
	SELECT game_id, round(avg(bet_amount), 2) AS avg_bet_1st_round
    FROM player_game_round
    WHERE round_number = 1
    GROUP BY game_id;
# 10
CREATE OR REPLACE VIEW v_report_avg_bet_last_round AS
	SELECT pgr.game_id, round(avg(pgr.bet_amount), 2) AS avg_bet_last_round
    FROM cardgame g JOIN player_game_round pgr ON g.id = pgr.game_id
    WHERE pgr.round_number = g.rounds
    GROUP BY g.id;