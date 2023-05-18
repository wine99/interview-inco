DROP TABLE IF EXISTS turbine;

CREATE TABLE turbine (
  id TEXT PRIMARY KEY,
  capacity REAL NOT NULL,
  cost REAL NOT NULL
);

INSERT INTO turbine(id, capacity, cost)
VALUES("A", 2, 15),
      ("B", 2, 5),
      ("C", 2, 5),
      ("D", 6, 5),
      ("E", 5, 3);