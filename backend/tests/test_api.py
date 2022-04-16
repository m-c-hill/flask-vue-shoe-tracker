import pytest
import json
from app import create_app, db
from app.models import Brand, Shoe
from app.utils.brands import create_brands

# ===================================================
#   Fixtures
# ===================================================


@pytest.fixture
def client():
    app = create_app("testing")
    with app.app_context():
        with app.test_client() as client:
            db.create_all()
            create_brands(db, Brand)
            create_test_shoes()
        yield client


def create_test_shoes():
    """
    Create test data for endpoint tests
    """
    shoe_1 = Shoe(
        brand_id=10,
        model="Ghost 14",
        nickname="blue",
        distance=78,
        notes=None,
        alert_distance=500,
    )
    shoe_2 = Shoe(
        brand_id=11,
        model="Endorphin Speed 2",
        nickname="green",
        distance=120,
        notes=None,
        alert_distance=500,
    )

    db.session.add(shoe_1)
    db.session.add(shoe_2)

    db.session.commit()


@pytest.fixture
def all_brands():
    return [
        {"id": 1, "name": "Nike"},
        {"id": 2, "name": "Adidas"},
        {"id": 3, "name": "New Balance"},
        {"id": 4, "name": "Asics"},
        {"id": 5, "name": "Reebok"},
        {"id": 6, "name": "Hoka One One"},
        {"id": 7, "name": "Puma"},
        {"id": 8, "name": "Altra"},
        {"id": 9, "name": "Newton"},
        {"id": 10, "name": "Brooks"},
        {"id": 11, "name": "Saucony"},
        {"id": 12, "name": "Mizuno"},
        {"id": 13, "name": "Salomon"},
        {"id": 14, "name": "Sketchers"},
        {"id": 15, "name": "Under Armour"},
        {"id": 16, "name": "APL"},
        {"id": 17, "name": "Merrell"},
        {"id": 18, "name": "Veja"},
        {"id": 19, "name": "La Sportiva"},
        {"id": 20, "name": "On-Running"},
    ]


@pytest.fixture()
def all_shoes():
    return [
        {
            "alert_distance": 500,
            "brand": {"id": 10, "name": "Brooks"},
            "distance": 78,
            "id": 1,
            "model": "Ghost 14",
            "nickname": "blue",
            "notes": None,
        },
        {
            "alert_distance": 500,
            "brand": {"id": 11, "name": "Saucony"},
            "distance": 120,
            "id": 2,
            "model": "Endorphin Speed 2",
            "nickname": "green",
            "notes": None,
        },
    ]


@pytest.fixture()
def brand_404():
    return {
        "success": False,
        "message": "Brand 21 not found",
    }, 404


# ===================================================
#   General API tests
# ===================================================


def test_404(client):
    response = client.get("/url/does/not/exist")
    assert response.status_code == 404


# ===================================================
#   Brand endpoint tests
# ===================================================


def test_get_all_brands(client, all_brands):
    response = client.get("/brands")
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert json_response["success"] == True
    assert json_response["resource"]["brands"] == all_brands


def test_get_brand_by_id(client, all_brands):
    brand_id = 1
    response = client.get(f"/brands/{brand_id}")
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert json_response["success"] == True
    assert json_response["resource"] == all_brands[0]


def test_get_brand_by_id_not_found(client):
    brand_id = 69
    response = client.get(f"/brands/{brand_id}")
    json_response = json.loads(response.get_data())

    assert response.status_code == 404
    assert json_response["success"] == False
    assert json_response["message"] == f"Brand id={brand_id} not found"


# ===================================================
#   Shoe endpoint tests
# ===================================================


def test_get_all_shoe(client, all_shoes):
    response = client.get("/shoes")
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert json_response["success"] == True
    assert json_response["resource"]["shoes"] == all_shoes


def test_get_shoe_by_id(client, all_shoes):
    shoe_id = 1
    response = client.get(f"/shoes/{shoe_id}")
    json_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert json_response["success"] == True
    assert json_response["resource"] == all_shoes[0]


def test_get_shoe_by_id_not_found(client):
    shoe_id = 10
    response = client.get(f"/shoes/{shoe_id}")
    json_response = json.loads(response.get_data())

    assert response.status_code == 404
    assert json_response["success"] == False
    assert json_response["message"] == f"Shoe id={shoe_id} not found"


def test_delete_shoe(client, all_shoes):
    shoe_id = 2
    response = client.delete(f"/shoes/{shoe_id}")
    json_response = json.loads(response.get_data())
    db_check = db.session.query(Shoe).get(shoe_id)

    assert response.status_code == 200
    assert json_response["success"] == True
    assert db_check == None
    assert json_response["message"] == f"Shoe (id={shoe_id}) deleted"


def test_add_new_shoe(client):
    assert True


def test_update_shoe_nickname(client):
    assert True


def test_update_shoe_nickname_not_unique(client):
    assert True


def test_add_run_to_shoe(client):
    assert True


# TODO: complete final tests
