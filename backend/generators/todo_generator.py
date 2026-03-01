def generate_todo_list(event_data):

    event_name = event_data.get("event_name", "Event")
    category = event_data.get("primary_category", "")
    location = event_data.get("location", "")
    activities = event_data.get("secondary_activities", [])

    todos = []

    # Core event tasks
    todos.extend([
        "Finalize event theme and objectives",
        f"Confirm venue booking in {location}",
        "Prepare event budget and resource allocation",
        "Design promotional materials and posters",
        "Launch social media marketing campaign",
        "Open event registrations",
        "Recruit volunteers and assign responsibilities",
        "Arrange sound system, lighting, and equipment",
        "Coordinate security and safety arrangements"
    ])

    # Category specific tasks
    if category == "music":
        todos.extend([
            "Book artists / bands",
            "Arrange stage setup and sound testing",
            "Prepare performance schedule",
            "Organize backstage management"
        ])

    elif category == "tech":
        todos.extend([
            "Prepare hackathon problem statements",
            "Invite mentors and judges",
            "Set up WiFi and coding environment",
            "Prepare evaluation criteria"
        ])

    elif category == "sports":
        todos.extend([
            "Register teams",
            "Arrange sports equipment",
            "Create tournament brackets",
            "Assign referees and match officials"
        ])

    elif category == "academic":
        todos.extend([
            "Invite speakers or instructors",
            "Prepare presentation materials",
            "Arrange seating and workshop resources"
        ])

    # Add tasks for secondary activities
    for activity in activities:
        todos.append(f"Plan logistics for {activity}")

    # Final event day tasks
    todos.extend([
        "Verify venue setup",
        "Conduct final technical checks",
        "Welcome participants and guests",
        "Execute event schedule",
        "Capture photos and videos for promotion",
        "Collect feedback from participants"
    ])

    return {
        "event_name": event_name,
        "todo_list": todos
    }
