

DROP TABLE IF EXISTS FoodInfo;
DROP TABLE IF EXISTS Food_Category;

CREATE TABLE FoodInfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INT,
    [name] VARCHAR(50),
    nickname VARCHAR(50),
    taste VARCHAR(50),
    efficacy TEXT,
    suitable_for TEXT,
    not_suitable_for TEXT,
    note TEXT,
    image BLOB,
    thumbnail BLOB,
    FOREIGN KEY (category_id) REFERENCES Food_Category(id)
);

CREATE TABLE Food_Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);