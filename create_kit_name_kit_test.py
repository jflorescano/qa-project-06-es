import sender_stand_request
import data


# Obtener el nombre del kit
def get_kit_body(kit_name):
    current_name = data.kit_body.copy()
    current_name["name"] = kit_name
    return current_name


def positive_assert(kit_name):
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_name_test = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_name_test, token)
    assert new_user_response.status_code == 201
    assert kit_response.status_code == 201
    assert new_user_response.json()["authToken"] != ""
    print(f"Intentando crear kit con el nombre: {kit_name}")
    kit_table_response = sender_stand_request.get_kits_table()
    str_kit = kit_name_test["name"]
    assert kit_table_response.text.count(str_kit) == 1


def negative_assert(kit_name):
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_name_test = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_name_test, token)
    assert new_user_response.status_code == 201
    assert kit_response.status_code == 400
    assert new_user_response.json()["authToken"] != ""
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre de kit que ingresaste es incorrecto. "


def negative_assert_no_name(kit_body):
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_response = sender_stand_request.post_new_client_kit(token, kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


# pruebas
# Prueba 1: El número permitido de caracteres (1)
def test_create_kit_1_letter_get_success_response():
    positive_assert("A")


# Prueba 2: El número permitido de caracteres (511)
def test_create_kit_511_letter_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba 3: El numero de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_get_error_response():
    negative_assert("")


# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Prueba 5: Se permiten caracteres especiales
def test_create_kit_has_special_symbol_get_success_response():
    positive_assert("\"№%@\",")


# Prueba 6: Se permiten espacios
def test_create_kit_has_space_get_success_response():
    positive_assert(" A Aaa ")


# Prueba 7: Se permiten números
def test_create_kit_number_type_get_success_response():
    positive_assert("123")


# Prueba 8: El parámetro no se pasa en la solicitud
def test_create_kit_no_parameter_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)


# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_type_numer_get_error_response():
    negative_assert(123)
