from datetime import datetime

from Models.user import GeneralUser


def test_create_full_name(general_user):
    """
   GIVEN a new user (created as a fixture) named James White
   WHEN  his first_name and last_name are passed to the "create_full_name" function
   THEN the full_name should be James White
   """
    full_name = general_user.create_full_name()
    assert full_name == "James White"


def test_calculate_age(general_user):
    """
    GIVEN a new user (created as fixture) born in 1998
    WHEN his date of birth (dob) is passed to the "calculate_age function"
    THEN the age should be equal to 23

    """
    age = general_user.calculate_age()
    assert age == 23
