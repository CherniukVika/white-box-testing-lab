from auth import authenticate_user

def test_missing_credentials():
    db = {}
    assert authenticate_user("", "pass", db) == "Missing credentials"
    assert authenticate_user("user", "", db) == "Missing credentials"

def test_user_not_found():
    db = {}
    assert authenticate_user("user", "pass", db) == "User not found"

def test_account_locked():
    db = {"user": {"password": "pass", "attempts": 3}}
    assert authenticate_user("user", "pass", db) == "Account locked"

def test_invalid_password():
    db = {"user": {"password": "pass", "attempts": 0}}
    assert authenticate_user("user", "wrong", db) == "Invalid password"
    assert db["user"]["attempts"] == 1

def test_success():
    db = {"user": {"password": "pass", "attempts": 1}}
    assert authenticate_user("user", "pass", db) == "Authenticated"
    assert db["user"]["attempts"] == 0

def test_attempts_edge_cases():
    # Тести для кращого MC/DC та Condition Coverage
    # attempts = 1 (граничне значення)
    db = {"user": {"password": "pass", "attempts": 1}}
    assert authenticate_user("user", "wrong", db) == "Invalid password"
    assert db["user"]["attempts"] == 2

    # attempts = 2
    db = {"user": {"password": "pass", "attempts": 2}}
    assert authenticate_user("user", "wrong", db) == "Invalid password"
    assert db["user"]["attempts"] == 3

def test_missing_credentials_variations():
    # Додаткові варіації першої умови
    db = {}
    assert authenticate_user(None, "pass", db) == "Missing credentials"   # username is None
    assert authenticate_user("user", None, db) == "Missing credentials"   # password is None