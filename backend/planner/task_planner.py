from generators.poster_generator import generate_event_posters
from generators.social_post_generator import generate_social_posts
from generators.timeline_generator import generate_timeline
from generators.todo_generator import generate_todo_list
from generators.form_generator import generate_form_schema
from generators.website_generator import generate_website_structure


def plan_tasks(event_data):

    category = event_data.get("primary_category", "")
    attendees = event_data.get("expected_attendees", 0)

    tasks = []

    # Basic generators
    tasks.append("poster")
    tasks.append("social_posts")
    tasks.append("timeline")

    # Large events need more planning
    if attendees and attendees > 100:
        tasks.append("todo_list")

    # Tech events need registration forms
    if category in ["tech", "sports", "music"]:
        tasks.append("registration_form")

    # Optional website
    if attendees and attendees > 200:
        tasks.append("website")

    return tasks

def execute_plan(event_data):

    tasks = plan_tasks(event_data)

    results = {}

    if "poster" in tasks:
        results["poster"] = generate_event_posters(event_data)

    if "social_posts" in tasks:
        results["social_posts"] = generate_social_posts(event_data)

    if "timeline" in tasks:
        results["timeline"] = generate_timeline(event_data)

    if "todo_list" in tasks:
        results["todo_list"] = generate_todo_list(event_data)

    if "registration_form" in tasks:
        results["form"] = generate_form_schema(event_data)

    if "website" in tasks:
        results["website"] = generate_website_structure(event_data)

    return results
