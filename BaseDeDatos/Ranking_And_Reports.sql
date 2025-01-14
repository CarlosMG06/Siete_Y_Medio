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
),
MaxCounts AS (
    SELECT player_id, max(initial_card_count) AS max_count
    FROM CardCounts
    GROUP BY player_id
),
TiedCards AS (
    SELECT 
        cc.player_id,
        GROUP_CONCAT(cc.initial_card_id ORDER BY cc.initial_card_id) AS tied_cards,
        GROUP_CONCAT(cc.suit ORDER BY cc.initial_card_id) AS tied_suits,
        cc.initial_card_count,
        cc.games_played
    FROM CardCounts cc
    JOIN MaxCounts mc ON cc.player_id = mc.player_id 
	                  AND cc.initial_card_count = mc.max_count
    GROUP BY cc.player_id, cc.initial_card_count, cc.games_played
)
SELECT 
    player_id,
    tied_suits AS most_common_initial_cards_suits,
    tied_cards AS most_common_initial_card_ids,
    initial_card_count,
    games_played
FROM TiedCards
WHERE games_played >= 3;
/* 
CREATE OR REPLACE VIEW v_report_most_common_initial_card AS
	SELECT 
		pg.player_id,
		c.suit AS most_common_initial_card_suit,
		pg.initial_card_id AS most_common_initial_card_id,
		count(*) AS initial_card_count,
		(SELECT count(*) 
		 FROM player_game 
		 WHERE player_id = pg.player_id) AS games_played
	FROM player_game pg JOIN card c ON pg.initial_card_id = c.id
	GROUP BY pg.player_id, pg.initial_card_id, c.suit
	HAVING count(*) = (
			SELECT max(card_count)
			FROM (
				SELECT count(*) AS card_count
				FROM player_game
				WHERE player_id = pg.player_id
				GROUP BY initial_card_id
				) AS max_card_count
			) 
	AND (SELECT count(*) 
         FROM player_game 
         WHERE player_id = pg.player_id) >= 3;
*/

# 2
CREATE OR REPLACE VIEW v_report_highest_bet AS
	SELECT DISTINCT pgr.game_id, pgr.player_id, pgr.bet_amount 
	FROM player_game_round pgr
    WHERE bet_amount = (
		SELECT max(pgr2.bet_amount)
        FROM player_game_round pgr2
        WHERE pgr.game_id = pgr2.game_id
        );
# 3
CREATE OR REPLACE VIEW v_report_lowest_bet AS
	SELECT DISTINCT pgr.game_id, pgr.player_id, pgr.bet_amount 
	FROM player_game_round pgr
    WHERE bet_amount = (
		SELECT min(pgr2.bet_amount)
        FROM player_game_round pgr2
        WHERE pgr.game_id = pgr2.game_id
        );
        
# 4
CREATE OR REPLACE VIEW v_report_round_win_rate AS 
	WITH RoundsWon AS (
		SELECT pgr1.game_id, pgr1.player_id,
			count(
				IF((pgr1.ending_points - pgr1.starting_points) = (
					SELECT max(ending_points - starting_points)
					FROM player_game_round pgr2
					WHERE pgr2.game_id = pgr1.game_id 
					  AND pgr2.round_number = pgr1.round_number),
					1, NULL)
			) AS rounds_won
		FROM player_game_round pgr1
		GROUP BY pgr1.game_id, pgr1.player_id
	)
	SELECT 
		pgr.game_id,
		pgr.player_id,
		g.rounds,
		avg(pgr.bet_amount) AS avg_bet,
		rw.rounds_won,
		(rw.rounds_won / g.rounds * 100) AS round_win_percentage
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
CREATE OR REPLACE VIEW v_report_bank_wins AS
	SELECT 
		pgr1.game_id,
		count(IF(pgr1.is_bank = True 
				 AND (pgr1.ending_points - pgr1.starting_points) = (
					   SELECT MAX(ending_points - starting_points)
					   FROM player_game_round pgr2
					   WHERE pgr2.game_id = pgr1.game_id 
						 AND pgr2.round_number = pgr1.round_number
				     ), 1, NULL)
		) AS rounds_won_by_bank
	FROM 
		player_game_round pgr1
	GROUP BY 
		pgr1.game_id;

# 7
CREATE OR REPLACE VIEW v_report_bank_players AS
	SELECT g.id, count(DISTINCT pgr.player_id) AS bank_players_count
    FROM cardgame g JOIN player_game_round pgr ON g.id = pgr.game_id
    WHERE pgr.bet_amount is NULL
    GROUP BY g.id;

# 8
CREATE OR REPLACE VIEW v_report_avg_bet AS
	SELECT g.id, avg(pgr.bet_amount) AS avg_bet
    FROM cardgame g JOIN player_game_round pgr ON g.id = pgr.game_id
    GROUP BY g.id;
# 9
CREATE OR REPLACE VIEW v_report_avg_bet_1st_round AS
	SELECT g.id, avg(pgr.bet_amount) AS avg_bet_1st_round
    FROM cardgame g JOIN player_game_round pgr ON g.id = pgr.game_id
    WHERE pgr.round_number = 1
    GROUP BY g.id;
# 10
CREATE OR REPLACE VIEW v_report_avg_bet_last_round AS
	SELECT g.id, avg(pgr.bet_amount) AS avg_bet_last_round
    FROM cardgame g JOIN player_game_round pgr ON g.id = pgr.game_id
    WHERE pgr.round_number = g.round_count
    GROUP BY g.id;