def generate_social_posts(event_data):

    event_name = event_data.get("event_name", "Exciting Event")
    location = event_data.get("location", "")
    date = event_data.get("date", "")
    audience = event_data.get("target_audience", "")
    highlights = event_data.get("key_highlights", [])
    category = event_data.get("primary_category", "")

    highlight_text = ", ".join(highlights)

    emoji_map = {
        "music": "🎵",
        "tech": "💻",
        "sports": "🏆",
        "cultural": "🎭",
        "business": "📈",
        "academic": "📚"
    }

    emoji = emoji_map.get(category, "🎉")

    # Instagram caption
    instagram_post = f"""
        {emoji} {event_name} is coming!

        📍 {location}
        📅 {date}

        🔥 Highlights: {highlight_text}

        Get ready for an unforgettable experience designed for {audience}!

        #Event #CampusLife #Festival #LiveEvents
        """.strip()

    # LinkedIn announcement
    linkedin_post = f"""
        We are excited to announce **{event_name}**!

        📍 Location: {location}
        📅 Date: {date}

        This event is designed for {audience} and will feature:

        {highlight_text}

        Stay tuned for more details and registration information.
        """.strip()

    # Twitter / X post
    twitter_post = f"""
        {emoji} {event_name} coming soon!

        📍 {location}
        📅 {date}

        Highlights: {highlight_text}

        #Event #LiveEvents
        """.strip()

    return {
        "instagram": instagram_post,
        "linkedin": linkedin_post,
        "twitter": twitter_post
    }
