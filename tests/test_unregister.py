"""
Tests for DELETE /activities/{activity_name}/unregister endpoint.
Verify unregister functionality with validation and error cases.
"""


def test_unregister_success(client):
    """
    Test: Student successfully unregisters from activity
    
    Arrange: Student is registered for activity
    Act: DELETE unregister request
    Assert: Participant removed and success message returned
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in participants
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert email in data["message"]
    assert activity_name in data["message"]


def test_unregister_participant_not_found(client):
    """
    Test: Unregister fails when participant not in activity
    
    Arrange: Student not registered for activity
    Act: DELETE unregister request for non-participant
    Assert: 400 error returned
    """
    # Arrange
    activity_name = "Chess Club"
    email = "notinlist@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "not found" in data["detail"].lower()


def test_unregister_activity_not_found(client):
    """
    Test: Unregister fails when activity doesn't exist
    
    Arrange: Activity name doesn't exist
    Act: DELETE unregister for non-existent activity
    Assert: 404 error returned
    """
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()


def test_unregister_then_signup_again(client):
    """
    Test: Student can re-sign up after unregistering
    
    Arrange: Student is registered
    Act: Unregister, then sign up again
    Assert: Both operations succeed
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    
    # Act - Unregister
    response1 = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Act - Sign up again
    response2 = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
