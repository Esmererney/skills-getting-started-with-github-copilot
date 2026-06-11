"""
Pytest configuration and fixtures for FastAPI tests.
Provides isolated app instances and TestClient for each test.
"""
import pytest
from fastapi.testclient import TestClient
from src import app as app_module


@pytest.fixture
def client():
    """
    Fixture: Create a fresh TestClient with isolated activities state.
    Each test gets a clean in-memory database.
    """
    # Arrange: Reset activities to initial state
    app_module.activities.clear()
    app_module.activities.update({
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball league and training",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": []
        },
        "Soccer Club": {
            "description": "Soccer practice and friendly matches",
            "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
            "max_participants": 22,
            "participants": []
        },
        "Art Studio": {
            "description": "Painting, drawing, and sculpture classes",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": []
        },
        "Drama Club": {
            "description": "Theater performances and acting workshops",
            "schedule": "Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": []
        },
        "Debate Team": {
            "description": "Competitive debate and public speaking",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": []
        },
        "Science Club": {
            "description": "Hands-on experiments and STEM exploration",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": []
        }
    })
    
    # Return TestClient with reset state
    return TestClient(app_module.app)


@pytest.fixture
def sample_activity():
    """
    Fixture: Provide sample activity data for tests.
    """
    return {
        "name": "Chess Club",
        "email": "newstudent@mergington.edu"
    }
