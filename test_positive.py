from  validators import validate_email, validate_age

def test_validate_email_accepted():
    assert validate_email("stdent@siam.ac.th") == True

def test_validate_email_subdomain():
    assert validate_email("user@mail.example.com") == True

def test_valid_age_accepted():

    assert validate_age(25) == True

def test_boundary_ages_accepted():
    assert validate_age(0) == True
    assert validate_age(150) == True