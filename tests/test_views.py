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


@pytest.mark.django_db
def test_create_view_renders(client):
    # "/new/" is mapped to create_view in tasks/urls.py
    response = client.get("/new/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_view_missing_task_returns_404(client):
    # No task with pk 999 exists, so delete view should return 404
    response = client.get("/delete/999/")
    assert response.status_code == 404
