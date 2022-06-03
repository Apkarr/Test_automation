
from api_m import MoyKlass
from settings import val_id, val_name, val_phone, val_email

mn = MoyKlass()


def test_get_api_manager(id=val_id, name=val_name, phone=val_phone, email=val_email):
    status, result = mn.get_api_manager(id, name, phone, email)
    assert status == 200
    assert isinstance(result, object)
    assert 'api_managers' in result
