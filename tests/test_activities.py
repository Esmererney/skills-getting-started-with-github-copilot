"""
Tests for GET /activities endpoint.
Verify activity data retrieval and response structure.
"""


def test_get_activities_success(client):
    """
    Test: GET /activities returns all activities
    
    Arrange: Client is ready
    Act: Make GET request to /activities
    Assert: Response contains expected activities
    """
    # Arrange
    expected_activities = [
        "Chess Club",
        "Programming Class", 
        "Gym Class",
        "Basketball Team",
        "Soccer Club",
        "Art Studio",
        "Drama Club",
        "Debate Team",
        "Science Club"
    ]
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert len(data) == len(expected_activities)
    for activity in expected_activities:
        assert activity in data


def test_get_activities_response_structure(client):
    """
    Test: GET /activities returns correct structure
    
    Arrange: Client is ready
    Act: Make GET request and check structure
    Assert: Each activity has required fields
    """
    # Arrange
    required_fields = ["description", "schedule", "max_participants", "participants"]
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in data.items():
        for field in required_fields:
            assert field in activity_data, f"Missing field: {field} in {activity_name}"
        assert isinstance(activity_data["participants"], list)
        assert isinstance(activity_data["max_participants"], int)
