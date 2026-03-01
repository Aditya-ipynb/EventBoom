# EventBoom AI – Backend

The **EventBoom AI Backend** powers the intelligent event planning system that converts a simple text prompt into a complete **event launch kit**.

This includes:

* AI-generated event posters
* Social media content
* Event planning timeline
* Interactive todo checklist
* Registration form schema
* Event data extraction from prompts

The backend is implemented in **Python** using a modular AI pipeline architecture.

---

# Architecture Overview

```
User Prompt
     │
     ▼
Prompt Analyzer
     │
     ▼
Task Planner
     │
     ▼
Generators
 ├── Poster Generator
 ├── Social Post Generator
 ├── Timeline Generator
 ├── Todo Generator
 └── Form Generator
     │
     ▼
Structured Event Launch Kit
```

The system analyzes the prompt, determines required tasks, and dynamically generates event assets.

---

# Folder Structure

```
backend
│
├── analyzer
│   └── prompt_analyzer.py
│
├── planner
│   └── task_planner.py
│
├── generators
│   ├── poster_generator.py
│   ├── social_post_generator.py
│   ├── timeline_generator.py
│   ├── todo_generator.py
│   ├── form_generator.py
│   └── website_generator.py
│
├── prompt_history
│   └── stored event generations
│
├── demo_app.py
├── requirements.txt
└── README_backend.md
```

---

# Core Modules

## Prompt Analyzer

Extracts structured event data from a natural language prompt.

Example output:

```
{
  "event_name": "RoboRumble 2026",
  "primary_category": "tech",
  "location": "Pune",
  "duration": "2-day",
  "expected_attendees": 300,
  "date": "2026-03-28"
}
```

The analyzer uses rule-based extraction with keyword detection.

---

## Task Planner

Determines which assets should be generated.

Example decision logic:

```
if attendees > 100 → generate todo list
if tech event → generate registration form
if large event → generate website structure
```

This keeps the pipeline efficient and context-aware.

---

## Generators

Each generator produces a specific asset for the event.

### Poster Generator

Creates **AI-generated event posters** using text-to-image models.

Output:

```
poster_variation_1.png
poster_variation_2.png
poster_variation_3.png
poster_variation_4.png
```

---

### Social Post Generator

Creates platform-specific marketing content.

Platforms supported:

* Instagram
* LinkedIn
* Twitter

---

### Timeline Generator

Generates an event planning schedule based on:

* today's date
* event date
* days remaining

Example:

```
T-20 days: Begin marketing campaign
T-10 days: Confirm speakers
T-2 days: Final equipment checks
Event Day: Opening ceremony
```

---

### Todo Generator

Creates a structured **event operations checklist**.

The checklist is interactive in the UI and supports **progress tracking**.

Example:

```
1. Finalize event theme
2. Confirm venue booking
3. Launch marketing campaign
4. Recruit volunteers
5. Setup technical infrastructure
```

---

### Form Generator

Generates a **registration form schema** dynamically.

Example fields for a tech event:

```
Full Name
Email
Phone Number
College
Team Name
Team Size
Programming Languages
```

---

# Demo Application

The backend can be tested using the **Streamlit demo interface**.

Run:

```
streamlit run demo_app.py
```

The interface allows users to:

* enter an event prompt
* select event date
* generate assets
* view event history
* preview registration forms
* track todo progress

---

# Installation

### Clone repository

```
git clone https://github.com/your-username/EventBoom-AI.git
cd EventBoom-AI/backend
```

### Install dependencies

```
pip install -r requirements.txt
```

---

# Environment Variables

If using HuggingFace models:

```
HF_TOKEN=your_huggingface_api_key
```

---

# Example Prompt

```
Organize a 2-day intercollege robotics competition called RoboRumble 2026 in Pune for 300 engineering students featuring robot battles, innovation showcases, and expert tech talks.
```

Generated outputs include:

* Event posters
* Marketing posts
* Planning timeline
* Todo checklist
* Registration form

---

# Key Features

* Modular AI pipeline
* Prompt-to-event planning
* Local asset storage
* Event history tracking
* Interactive todo checklist
* Dynamic registration forms

---

# Tech Stack

Backend:

* Python
* Streamlit
* Pillow
* HuggingFace Inference API

AI Components:

* Prompt analysis
* Image generation
* Content generation
* Planning automation

---

# Future Improvements

* LLM-powered prompt understanding
* Automated sponsor suggestions
* Budget estimation
* Full event website generation
* Multi-user collaboration

---

# License

This project is for research and hackathon demonstration purposes.
