import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    qnt = db.select_product_qnt_by_id(4)
    assert qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0


@pytest.mark.database
def test_dateiled_orders():
    db = Database()
    orders = db.get_dateiled_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check srtucture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_insert_invalid_data_type():
    db = Database()
    message = db.insert_invalid_data_type('перший', 555, 777, 'десять')  # invalid data type
    assert message.startswith("Error:")


@pytest.mark.database
def test_check_data_type():
    db = Database()
    message = db.check_data_type('перший', 555, 777, 'десять')
    assert message == "Invalid data type"


@pytest.mark.database
def test_check_if_query_was_successful():
    db = Database()
    message = db.check_if_query_was_successful(99, 'тестові', 'дані', 999)
    assert message == "Query was successful"
    db.delete_product_by_id(99)