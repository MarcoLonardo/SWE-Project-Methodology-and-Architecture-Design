import pytest
from Models.user import GeneralUser


@pytest.fixture(scope='function')
def general_user():
    new_user = GeneralUser(first_name='Marco', last_name='Lonardo', email='email@email.com', password="pssw")
    yield new_user
