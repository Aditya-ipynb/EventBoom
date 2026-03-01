import streamlit as st
from datetime import date
import json
import os
import shutil

from analyzer.prompt_analyzer import analyze_prompt
from planner.task_planner import execute_plan
from generators.form_generator import generate_form_schema

st.set_page_config(page_title="EventBoom AI", layout="wide")

# -------------------------
# SESSION STATE
# -------------------------
if "selected_event" not in st.session_state:
    st.session_state.selected_event = None


# -------------------------
# SIDEBAR HISTORY
# -------------------------

st.sidebar.title("📂 Previous Events")
# NEW EVENT BUTTON
if st.sidebar.button("➕ Create New Event"):
    st.session_state.selected_event = None

event_map = {}

if os.path.exists("prompt_history"):

    folders = sorted(os.listdir("prompt_history"), reverse=True)

    for folder in folders:

        try:
            with open(f"prompt_history/{folder}/data.json") as f:

                data = json.load(f)

                name = data["event_data"]["event_name"]

                event_map[name] = folder

        except:
            continue


for name, folder in event_map.items():

    if st.sidebar.button(name):

        st.session_state.selected_event = folder


# -------------------------
# MAIN TITLE
# -------------------------
st.markdown("---")

st.markdown("""
<style>

/* Hide default Streamlit header */
header[data-testid="stHeader"] {
    display: none;
}

/* Global top header */
.global-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 80px;
    background-color: #0e1117;
    z-index: 9999;
    border-bottom: 1px solid #2b2b2b;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* Title */
.global-title {
    font-size: 30px;
    font-weight: 700;
}

/* Subtitle */
.global-subtitle {
    font-size: 14px;
    color: #aaa;
}

/* Push entire app below header */
.stApp {
    padding-top: 90px;
}

/* Sidebar also moves down */
section[data-testid="stSidebar"] {
    margin-top: 80px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-testid="stCheckbox"] > label {
    justify-content: flex-end;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="global-header">
    <div class="global-title">EventBoom AI Event Planner</div>
    <div class="global-subtitle">Generate a complete event launch kit from a single prompt.</div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# EVENT INPUT
# -------------------------

if st.session_state.selected_event is None:

    prompt = st.text_area(
        "Describe your event",
        placeholder="Example: Plan a 2-day college music festival called Spark 2026 in Mumbai for 2000 students featuring live bands and DJ night"
    )

    event_date = st.date_input(
        "Select Event Date",
        min_value=date.today()
    )

    st.markdown("---")

# -------------------------
# SAVE GENERATION
# -------------------------
def save_generation(prompt, event_date, event_data, result):

    import shutil
    os.makedirs("prompt_history", exist_ok=True)
    event_id = f"event_{len(os.listdir('prompt_history'))+1}"
    event_folder = f"prompt_history/{event_id}"
    os.makedirs(event_folder, exist_ok=True)

    saved_posters = []
    if "poster" in result:
        for i, poster in enumerate(result["poster"]):

            poster_path = f"{event_folder}/poster_{i+1}.png"

            if os.path.exists(poster):
                shutil.copy(poster, poster_path)
                saved_posters.append(poster_path)

    data = {
        "prompt": prompt,
        "event_date": str(event_date),
        "event_data": event_data,
        "result": result,
        "posters": saved_posters
    }

    with open(f"{event_folder}/data.json", "w") as f:
        json.dump(data, f, indent=4)

# ----------------
# TODO List
# -------------
def render_todo_list(event_folder, todo_data):

    todo_items = todo_data["todo_list"]

    progress_file = f"prompt_history/{event_folder}/todo_progress.json"

    # -------------------------
    # LOAD PREVIOUS STATE
    # -------------------------
    if os.path.exists(progress_file):

        with open(progress_file) as f:
            progress = json.load(f)

    else:

        progress = {str(i): False for i in range(len(todo_items))}

    updated_progress = {}

    # -------------------------
    # TODO RENDER
    # -------------------------
    for i, task in enumerate(todo_items):

        cols = st.columns([1,8,1])

        with cols[0]:
            st.write(f"**{i+1}.**")

        with cols[1]:
            st.write(task)

        with cols[2]:
            checked = st.checkbox(
                "",
                value=progress.get(str(i), False),
                key=f"{event_folder}_todo_{i}"
            )

        updated_progress[str(i)] = checked

    # -------------------------
    # SAVE STATE
    # -------------------------
    os.makedirs(f"prompt_history/{event_folder}", exist_ok=True)

    with open(progress_file, "w") as f:
        json.dump(updated_progress, f, indent=4)

    # -------------------------
    # PROGRESS BAR
    # -------------------------
    completed = sum(updated_progress.values())
    total = len(todo_items)

    st.progress(completed / total)
    st.caption(f"{completed}/{total} tasks completed")

# -------------------------
# REGISTRATION FORM
# -------------------------

def render_registration_form(form_schema):

    st.subheader(form_schema["form_title"])
    st.caption("Form Preview")

    for field in form_schema["fields"]:

        if field["type"] == "text":
            st.text_input(field["label"], disabled=True)

        elif field["type"] == "email":
            st.text_input(field["label"], disabled=True)

        elif field["type"] == "number":
            st.number_input(
                field["label"],
                min_value=1,
                step=1,
                format="%d",
                disabled=True
            )

    st.button("Submit Registration", disabled=True)


# -------------------------
# LOAD STORED EVENT
# -------------------------

if st.session_state.selected_event:

    folder = st.session_state.selected_event

    with open(f"prompt_history/{folder}/data.json") as f:
        stored = json.load(f)

    event_data = stored["event_data"]
    result = stored["result"]

    st.subheader("Loaded Previous Event")

    st.write("Prompt:")
    st.write(stored["prompt"])

    st.json(event_data)

    st.markdown("---")

    # Posters
    if stored.get("posters"):

        st.subheader("🎨 Poster Variations")

        cols = st.columns(2)

        for i, poster_path in enumerate(stored["posters"]):

            cols[i % 2].image(poster_path, use_container_width=True)

    # Social posts
    if "social_posts" in result:

        st.subheader("📢 Social Media Content")

        st.write(result["social_posts"])

    # Timeline
    if "timeline" in result:

        st.subheader("📅 Event Timeline")

        for step in result["timeline"]["timeline"]:
            st.write("•", step)

    # Todo list
    if "todo_list" in result:

        st.subheader("✅ Todo List")

        render_todo_list(folder, result["todo_list"])

    st.markdown("---")

    # Registration Form
    st.subheader("📝 Event Registration Form")

    form_schema = generate_form_schema(event_data)

    if st.button("Open Registration Form"):
        render_registration_form(form_schema)


# -------------------------
# GENERATE NEW EVENT
# -------------------------

if st.session_state.selected_event is None and st.button("Generate Event Plan"):
    if not prompt:
        st.warning("Please describe your event.")
        st.stop()

    event_data = analyze_prompt(prompt, event_date)

    st.subheader("Extracted Event Information")
    st.json(event_data)

    result = execute_plan(event_data)
    save_generation(prompt, event_date, event_data, result)
    st.markdown("---")

    # Posters
    if "poster" in result:
        st.subheader("🎨 Poster Variations")
        cols = st.columns(2)

        for i, poster in enumerate(result["poster"]):
            cols[i % 2].image(poster, use_container_width=True)

    # Social media
    if "social_posts" in result:
        st.subheader("📢 Social Media Content")
        st.write(result["social_posts"])

    # Timeline
    if "timeline" in result:

        st.subheader("📅 Event Timeline")

        for step in result["timeline"]["timeline"]:
            st.write("•", step)

    # Todo list
    if "todo_list" in result:

        st.subheader("✅ Todo List")
        for i, task in enumerate(result["todo_list"]["todo_list"]):

            cols = st.columns([1,8,1])

            cols[0].write(f"**{i+1}.**")
            cols[1].write(task)
            cols[2].checkbox("", key=f"new_todo_{i}")
    st.markdown("---")

    # Registration form
    st.subheader("📝 Event Registration Form")
    form_schema = generate_form_schema(event_data)

    if st.button("Open Registration Form"):
        render_registration_form(form_schema)
