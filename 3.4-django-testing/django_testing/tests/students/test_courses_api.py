import pytest
from rest_framework.test import APIClient
from model_bakery import baker


from students.models import Course
import json


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):

    course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]['id'] == course[0].id


@pytest.mark.django_db
def test_get_list_course(client, course_factory):

    course = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    assert len(response.data) == 10
    for i in range(10):
        assert response.data[i]['id'] == course[i].id
        assert response.data[i]['name'] == course[i].name


@pytest.mark.django_db
def test_filter_course_id(client, course_factory):

    course = course_factory(_quantity=10)
    course_id_to_filter = course[0].id

    response = client.get(f'/api/v1/courses/?id={course_id_to_filter}')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == course_id_to_filter


@pytest.mark.django_db
def test_filter_course_name(client, course_factory):

    course = course_factory(_quantity=10)
    course_name_to_filter = course[0].name

    response = client.get(f'/api/v1/courses/?name={course_name_to_filter}')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == course_name_to_filter


@pytest.mark.django_db
def test_create_course(client):

    course_data = {
        "name": "Тестовый курс",
    }

    response_course = client.post(
        '/api/v1/courses/', data=json.dumps(course_data), content_type='application/json'
    )

    assert response_course.status_code == 201
    assert response_course.data['name'] == course_data['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):

    course = course_factory(_quantity=1)[0]
    up_data = {
        "name": "Тестовый курс"
    }

    response_up_course = client.put(
        f'/api/v1/courses/{course.id}/', data=json.dumps(up_data), content_type='application/json'
    )

    assert response_up_course.status_code == 200
    response_get_course = client.get(f'/api/v1/courses/{course.id}/')
    assert response_get_course.status_code == 200
    assert response_get_course.json()['name'] == "Тестовый курс"


@pytest.mark.django_db
def test_delite_course(client, course_factory):

    course = course_factory(_quantity=1)
    course_id = course[0].id

    response = client.delete(f'/api/v1/courses/{course_id}/')

    assert response.status_code == 204
    response_after_delete = client.get(f'/api/v1/courses/{course_id}/')
    assert response_after_delete.status_code == 404
