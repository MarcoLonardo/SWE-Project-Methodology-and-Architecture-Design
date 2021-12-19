from Models.user import GeneralUser


def test_create_full_name(general_user):
    """
   GIVEN the first name (Marco) and the last name (Lonardo)
   WHEN the values are passed to the create_full_name function
   THEN the full_name should be Marco Lonardo
   """
    full_name = general_user.create_full_name()
    assert full_name == "Marco Lonardo"
