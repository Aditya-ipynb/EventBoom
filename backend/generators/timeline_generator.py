from datetime import datetime


def generate_timeline(event_data):

    event_name = event_data.get("event_name", "Event")
    category = event_data.get("primary_category", "")
    activities = event_data.get("secondary_activities", [])
    event_date_str = event_data.get("date")

    timeline = []

    today = datetime.today().date()

    # If event date is provided
    if event_date_str:

        try:
            event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
        except:
            event_date = today

    else:
        # If date missing, assume 30 days
        event_date = today
        days_remaining = 30

    days_remaining = (event_date - today).days

    if days_remaining <= 0:
        days_remaining = 1

    timeline.append(f"Today: Planning begins for {event_name}")
    timeline.append(f"Event Date: {event_date}")

    # Planning checkpoints scaled to time remaining
    checkpoints = []

    if days_remaining >= 30:

        checkpoints = [
            int(days_remaining * 0.75),
            int(days_remaining * 0.5),
            int(days_remaining * 0.25),
            2
        ]

    elif days_remaining >= 14:

        checkpoints = [
            int(days_remaining * 0.5),
            int(days_remaining * 0.25),
            2
        ]

    elif days_remaining >= 7:

        checkpoints = [
            int(days_remaining * 0.4),
            int(days_remaining * 0.2),
            1
        ]

    else:

        checkpoints = [1]

    # Generate preparation tasks
    for days_before in checkpoints:

        timeline.append(
            f"T-{days_before} days: Preparation and logistics planning"
        )

    # Event-day schedule based on category
    if category == "music":

        timeline.extend([
            "Event Day: Stage setup and sound check",
            "Event Day: Opening performance",
            "Event Day: Main concert performances",
            "Event Day: Closing DJ set"
        ])

    elif category == "tech":

        timeline.extend([
            "Event Day: Participant check-in",
            "Event Day: Opening keynote",
            "Event Day: Hacking session begins",
            "Event Day: Project submissions and judging",
            "Event Day: Awards ceremony"
        ])

    elif category == "sports":

        timeline.extend([
            "Event Day: Team registration",
            "Event Day: Opening ceremony",
            "Event Day: Tournament matches",
            "Event Day: Final match and awards"
        ])

    else:

        timeline.extend([
            "Event Day: Opening session",
            "Event Day: Main activities",
            "Event Day: Closing ceremony"
        ])

    # Secondary activities
    for activity in activities:

        timeline.append(
            f"Event Activity: {activity.capitalize()} session"
        )

    return {
        "event_name": event_name,
        "days_remaining": days_remaining,
        "timeline": timeline
    }
