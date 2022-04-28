-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
-- Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!
-- DELIMITER $$
-- CREATE TRIGGER after_insert_order AFTER INSERT ON orders
-- FOR EACH ROW
-- BEGIN
-- DECLARE n_order VARCHAR(255);
-- DECLARE q_order INT ;
-- SET q_order = new.number;
-- SET n_order = new.item_name;
-- UPDATE items SET quantity = quantity - q_ordder WHERE NAME = n_order;
-- END$$
-- DELIMITER ;

CREATE TRIGGER after_insert_order AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items
	SET quantity = quantity - new.number
	WHERE name = new.item_name;
