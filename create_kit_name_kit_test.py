import sender_stand_request
import data


def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == name


def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400

    def test_create_kit_1_letter_in_name_get_success_response():
        positive_assert("a")

    def test_create_kit_511_letter_in_name_get_success_response():
        name_511 = "a" * 511
        positive_assert(name_511)


    def test_create_kit_empty_name_get_error_response():
        positive_assert("")


    def test_create_kit_512_letter_in_name_get_error_response():
        name_512 = "a" * 512
        negative_assert_code_400(name_512)


    def test_create_kit_has_special_char_in_name_get_success_response():
        positive_assert('"№%@",')


    def test_create_kit_has_space_in_name_get_success_response():
        positive_assert(" A A aa ")


    def test_create_kit_has_number_in_name_get_success_response():
        positive_assert("123")


    def test_create_kit_no_name_in_body_get_error_response():
        auth_token = get_new_user_token()
        response = sender_stand_request.post_new_client_kit({}, auth_token)

        assert response.status_code == 400


    def test_create_kit_int_type_name_get_error_response():
        negative_assert_code_400(123)