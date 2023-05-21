from interview_inco.contorl import compute_plan

profile = [
    ("A", 2, 15),
    ("B", 2, 5),
    ("C", 6, 5),
    ("D", 6, 5),
    ("E", 5, 3),
]


def test1():
    expected = [
        ("A", 0),
        ("B", 2),
        ("C", 0),
        ("D", 0),
        ("E", 5),
    ]
    assert compute_plan(profile, 10, 6)["plan"] == expected


def test2():
    expected1 = [
        ("A", 0),
        ("B", 2),
        ("C", 6),
        ("D", 0),
        ("E", 5),
    ]
    expected2 = [
        ("A", 0),
        ("B", 2),
        ("C", 0),
        ("D", 6),
        ("E", 5),
    ]
    plan = compute_plan(profile, 15, 6)["plan"]
    assert plan == expected1 or plan == expected2


def test3():
    expected = [
        ("A", 0),
        ("B", 0),
        ("C", 0),
        ("D", 0),
        ("E", 5),
    ]
    assert compute_plan(profile, 15, 4)["plan"] == expected
