-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
-- Requirements:
--     Procedure ComputeAverageScoreForUser is taking 1 input:
--         user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
	BEGIN
		DECLARE user_average FLOAT DEFAULT 0.0;
		SELECT AVG(corrections.score) INTO user_average FROM corrections WHERE user_id = corrections.user_id;
		UPDATE users SET average_score = user_average WHERE id = user_id;
	END$$
DELIMITER ;
