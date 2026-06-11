"""
Tests for GET / endpoint.
Verify root redirect to static index.html.
"""


def test_root_redirect(client):
    """
    Test: GET / redirects to /static/index.html
    
    Arrange: Client is ready
    Act: Make GET request to root
    Assert: Response redirects with 307 status code
    """
    # Arrange
    expected_status = 307
    expected_location = "/static/index.html"
    
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == expected_status
    assert response.headers["location"] == expected_location
