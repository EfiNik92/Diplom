# Ефимов Никита 9 поток, финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_get_order_info_by_track():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200
