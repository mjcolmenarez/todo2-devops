import pytest

@pytest.mark.django_db
def test_list_view_renders(client):
    # "/" is mapped to list_view via tasks/urls.py
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_kanban_view_renders(client):
    # "/kanban/" is mapped to kanban_view in tasks/urls.py
    response = client.get("/kanban/")
    assert response.status_code == 200
