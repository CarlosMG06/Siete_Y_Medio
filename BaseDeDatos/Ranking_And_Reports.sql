USE seven_and_half;

/* WIP
SELECT sum(timestampdiff(MINUTE, g.start_time, g.end_time)) 
        FROM player p JOIN player_game pg ON p.id = pg.player_id
					  JOIN v_game g ON pg.game_id = g.game_id
GROUP BY g.game_id;

CREATE VIEW v_ranking AS
	SELECT 
		p.id as player_id,
        p.player_name,
        count(DISTINCT pg.game_id) AS games_played,
        (
        SELECT sum(timestampdiff(MINUTE, g.start_time, g.end_time)) 
        FROM player p JOIN player_game pg ON p.id = pg.player_id
					  JOIN v_game g ON pg.game_id
        ) AS minutes_played
	SELECT player p JOIN player_game pg ON p.id = pg.player_id
					JOIN
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
# 6
/* WIP
CREATE VIEW v_report_bank_wins AS
	SELECT 
		g.id, count(DISTINCT pgr.round_number) AS rounds_won_by_bank
	FROM v_game g LEFT JOIN player_game_round pgr ON g.id = pgr.game_id
	WHERE bet_amount IS NOT NULL # All non-bank players
    GROUP BY game_id, round_number
		HAVING sum(if(end_points >= start_points, 1, 0)) = 0; # Don't win points (Bank wins)
*/

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