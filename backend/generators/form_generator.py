def generate_form_schema(event_data):

    category = event_data.get("primary_category", "")

    fields = [
        {"name": "full_name", "label": "Full Name", "type": "text"},
        {"name": "email", "label": "Email", "type": "email"},
        {"name": "phone", "label": "Phone Number", "type": "text"},
        {"name": "organization", "label": "College / Organization", "type": "text"}
    ]

    if category == "tech":
        fields.append({"name": "team_name", "label": "Team Name", "type": "text"})
        fields.append({"name": "team_size", "label": "Team Size", "type": "number"})
        fields.append({"name": "languages", "label": "Programming Languages", "type": "text"})

    elif category == "music":
        fields.append({"name": "genre", "label": "Preferred Music Genre", "type": "text"})

    elif category == "sports":
        fields.append({"name": "team_name", "label": "Team Name", "type": "text"})
        fields.append({"name": "position", "label": "Position", "type": "text"})

    return {
        "form_title": f"{event_data.get('event_name')} Registration",
        "fields": fields
    }
