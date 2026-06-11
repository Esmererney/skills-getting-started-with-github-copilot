"""
Tests for POST /activities/{activity_name}/signup endpoint.
Verify signup functionality with validation and error cases.
"""


def test_signup_success(client):
    """
    Test: Student successfully signs up for activity
    
    Arrange: Activity exists, student not already signed up
    Act: POST signup request with email and activity
    Assert: Participant added and success message returned
    """
    # Arrange
    activity_name = "Basketball Team"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert email in data["message"]
    assert activity_name in data["message"]


def test_signup_duplicate_prevented(client):
    """
    Test: Student cannot sign up twice for same activity
    
    Arrange: Student already signed up for activity
    Act: Attempt to sign up again
    Assert: 400 error with appropriate message
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in participants
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"].lower()


def test_signup_activity_not_found(client):
    """
    Test: Signup fails when activity doesn't exist
    
    Arrange: Activity name doesn't exist
    Act: POST signup for non-existent activity
    Assert: 404 error returned
    """
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()


def test_signup_multiple_students_same_activity(client):
    """
    Test: Multiple different students can sign up for same activity
    
    Arrange: Activity exists
    Act: Sign up two different students
    Assert: Both successfully added
    """
    # Arrange
    activity_name = "Soccer Club"
    email1 = "student1@mergington.edu"
    email2 = "student2@mergington.edu"
    
    # Act
    response1 = client.post(
        f"/activities/{activity_name}/signup?email={email1}"
    )
    response2 = client.post(
        f"/activities/{activity_name}/signup?email={email2}"
    )
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert email1 in response1.json()["message"]
    assert email2 in response2.json()["message"]
