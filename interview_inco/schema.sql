DROP TABLE IF EXISTS turbine;
DROP TABLE IF EXISTS target_production;
DROP TABLE IF EXISTS price;

CREATE TABLE turbine (
  id TEXT PRIMARY KEY,
  capacity REAL NOT NULL,
  cost REAL NOT NULL
);

CREATE TABLE target_production (
  id INTEGER PRIMARY KEY,
  production REAL NOT NULL
);

CREATE TABLE price (
  id INTEGER PRIMARY KEY,
  price REAL NOT NULL
);

INSERT INTO turbine(id, capacity, cost)
VALUES("A", 2, 15),
      ("B", 2, 5),
      ("C", 6, 5),
      ("D", 6, 5),
      ("E", 5, 3);

INSERT INTO target_production(id, production)
VALUES(1, 0);

INSERT INTO price(id, price)
VALUES(1, 0);
