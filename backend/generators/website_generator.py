def generate_website_structure(event_data):

    event_name = event_data.get("event_name", "Event")
    location = event_data.get("location", "")
    date = event_data.get("date", "")
    audience = event_data.get("target_audience", "")
    highlights = event_data.get("key_highlights", [])
    category = event_data.get("primary_category", "")

    website_structure = {
        "site_title": event_name,
        "sections": [
            {
                "type": "hero",
                "title": event_name,
                "subtitle": f"{location} • {date}"
            },
            {
                "type": "about",
                "content": f"{event_name} is an exciting {category} event designed for {audience}."
            },
            {
                "type": "highlights",
                "items": highlights
            },
            {
                "type": "timeline",
                "description": "Event schedule and activities will be displayed here."
            },
            {
                "type": "registration",
                "cta": "Register Now"
            }
        ]
    }

    return website_structure
