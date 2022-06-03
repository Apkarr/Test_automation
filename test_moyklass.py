

from api import MoyKlass
from settings import valid_email, valid_password


mk = MoyKlass()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):

    status, result = mk.get_api_key(email, password)
    assert status == 200
    assert isinstance(result, object)
    assert 'key' in result



