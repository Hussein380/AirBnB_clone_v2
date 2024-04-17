-- Create the  db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges on nthe hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELCT privileges on the performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- FLush privileges to apply changes
FLUSH PRIVILEGES;
