import re

CATEGORY_KEYWORDS = {

    "music": [
        "concert", "music", "dj", "band", "festival", "gig"
    ],

    "tech": [
        "hackathon", "coding", "ai", "tech", "developer",
        "programming", "data", "machine learning"
    ],

    "sports": [
        "tournament", "football", "cricket", "sports",
        "match", "league", "championship"
    ],

    "academic": [
        "workshop", "seminar", "lecture", "conference",
        "research", "training"
    ],

    "business": [
        "startup", "pitch", "business", "networking",
        "entrepreneur"
    ],

    "cultural": [
        "dance", "cultural", "traditional", "heritage",
        "celebration"
    ]
}

CATEGORY_HIGHLIGHTS = {

    "music": [
        "Live Bands",
        "DJ Night",
        "Festival Stage",
        "Food & Drinks",
        "Celebrity Performances"
    ],

    "tech": [
        "Coding Challenge",
        "Startup Pitching",
        "Mentor Sessions",
        "Innovation Showcase",
        "Developer Networking"
    ],

    "sports": [
        "Knockout Matches",
        "Championship Finals",
        "Team Participation",
        "Live Commentary"
    ],

    "academic": [
        "Expert Talks",
        "Hands-on Workshops",
        "Knowledge Sessions",
        "Research Presentations"
    ],

    "cultural": [
        "Dance Performances",
        "Traditional Music",
        "Art Exhibitions",
        "Cultural Showcase"
    ],

    "business": [
        "Startup Pitches",
        "Investor Talks",
        "Networking Sessions",
        "Panel Discussions"
    ],

    "social": [
        "Community Gathering",
        "Entertainment",
        "Interactive Activities"
    ]
}

def detect_category(prompt_lower):

    scores = {category: 0 for category in CATEGORY_KEYWORDS}

    for category, keywords in CATEGORY_KEYWORDS.items():

        for word in keywords:

            if word in prompt_lower:
                scores[category] += 1

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return "social"

    return best_category


def extract_keywords(prompt_lower):

    keywords = []

    for category_keywords in CATEGORY_KEYWORDS.values():
        for word in category_keywords:
            if word in prompt_lower:
                keywords.append(word)

    return list(set(keywords))

def generate_highlights(category, keywords):

    base_highlights = CATEGORY_HIGHLIGHTS.get(category, CATEGORY_HIGHLIGHTS["social"])

    highlights = base_highlights[:3]

    # add keyword-driven highlight if possible
    if "hackathon" in keywords:
        highlights.append("24 Hour Build Challenge")

    if "festival" in keywords:
        highlights.append("Festival Atmosphere")

    if "football" in keywords or "cricket" in keywords:
        highlights.append("Competitive Tournament")

    return highlights[:4]

def analyze_prompt(prompt, event_date):

    prompt_lower = prompt.lower()

    # Event name extraction
    name_match = re.search(
        r"called ([A-Za-z0-9\s]+?)(?: in | for | with | featuring |$)",
        prompt,
        re.IGNORECASE
    )

    event_name = name_match.group(1).strip() if name_match else "Untitled Event"

    # Location extraction
    location_match = re.search(
        r"in ([A-Za-z\s]+?)(?: for| with| featuring| during| at|$)",
        prompt_lower
    )
    location = location_match.group(1).strip().title() if location_match else None

    # Duration
    duration_match = re.search(r"(\d+-day|\d+ day|\d+ days)", prompt_lower)
    duration = duration_match.group(0) if duration_match else None

    # Expected attendees
    attendees_match = re.search(
        r"(\d+)\s*(students|people|attendees|developers|participants|visitors|guests|engineering students|employees|friends|medical students|children)",
        prompt_lower
    )

    expected_attendees = int(attendees_match.group(1)) if attendees_match else None

    # Category detection
    category = "social"

    if any(word in prompt_lower for word in ["concert", "music", "festival", "dj", "band"]):
        category = "music"

    elif any(word in prompt_lower for word in ["hackathon", "coding", "ai", "tech"]):
        category = "tech"

    elif any(word in prompt_lower for word in ["tournament", "football", "sports"]):
        category = "sports"

    elif any(word in prompt_lower for word in ["workshop", "seminar", "lecture"]):
        category = "academic"

    keywords = extract_keywords(prompt_lower)
    highlights = generate_highlights(category, keywords)

    return {

        "event_name": event_name,
        "event_type": "event",

        "primary_category": category,
        "secondary_activities": [],

        "location": location,
        "venue_type": "outdoor",

        # Date now comes from UI
        "date": event_date.strftime("%Y-%m-%d"),

        "duration": duration,
        "target_audience": "students",

        "expected_attendees": expected_attendees,

        "budget_range": None,

        "key_highlights": highlights,
        "keywords": keywords,

        "sponsors": [],
        "tone": "exciting"
    }
