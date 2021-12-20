import pytest
from Models.user import GeneralUser


@pytest.fixture(scope='function')
def general_user():
    new_user = GeneralUser(first_name='James', last_name='White', email='email@email.com', password="my_password",
                           dob="30/04/98")
    yield new_user
