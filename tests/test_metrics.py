import pytest

@pytest.mark.django_db
def test_metrics_endpoint(client):
    # Hit /health/ first so some metrics are generated
    client.get("/health/")

    response = client.get("/metrics/")
    assert response.status_code == 200

    text = response.content.decode("utf-8")
    # Check that one of our custom metrics appears
    assert "todo_http_requests_total" in text
