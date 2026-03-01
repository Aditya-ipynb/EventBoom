# EventBoom AI 🚀

### AI-Powered Event Planning & Launch Kit Generator

EventBoom AI is an intelligent event planning system that transforms a simple event description into a **complete event launch kit**.

Using AI-driven analysis and automation, the platform automatically generates:

* 🎨 Event posters
* 📢 Social media promotional content
* 📅 Event preparation timelines
* ✅ Interactive planning tasks
* 📝 Registration form structures
* 📂 Event workspaces for tracking progress

The goal of EventBoom AI is to **reduce the complexity of organizing events** by automating planning, marketing preparation, and coordination workflows.

---

# 🎯 Problem

Organizing events typically requires managing multiple parallel tasks:

* Event concept planning
* Marketing material creation
* Registration management
* Team coordination
* Scheduling and logistics

These processes are often **manual, fragmented, and time-consuming**.

EventBoom AI solves this by converting **a single natural language prompt** into a structured event planning toolkit.

---

# 💡 Solution

Users provide a simple prompt such as:

```
Organize a 2-day robotics competition called RoboRumble 2026 in Pune for
300 engineering students featuring robot battle arenas and innovation showcases.
```

EventBoom AI automatically generates:

* Event poster variations
* Social media promotional content
* Event timeline
* Interactive task planner
* Registration form structure
* Optional website structure

Each event is stored in its own **workspace**, allowing users to revisit and continue planning later.

---

# 🧠 AI System Architecture

EventBoom AI follows a modular AI pipeline architecture:

```
User Prompt
     │
     ▼
Prompt Analyzer
     │
     ▼
Task Planner
     │
     ├── Poster Generator (Diffusion Model)
     ├── Social Media Content Generator
     ├── Timeline Generator
     ├── Todo Task Planner
     ├── Registration Form Generator
     └── Website Structure Generator
```

Each module generates a specific component of the **event launch kit**.

---

# ⚙️ Core Features

## 1️⃣ Prompt Analyzer

The Prompt Analyzer converts natural language prompts into **structured event metadata**.

Extracted attributes include:

* Event name
* Event category (tech, music, sports, etc.)
* Location
* Event duration
* Target audience
* Expected attendees
* Event highlights

This structured data drives the entire generation pipeline.

---

## 2️⃣ AI Poster Generator

Generates promotional posters using **diffusion models**.

Features:

* Category-aware visual styles
* Dynamic title overlay
* Highlight integration
* Instagram-optimized dimensions
* Multiple poster variations

---

## 3️⃣ Social Media Content Generator

Automatically generates promotional content tailored for:

* Instagram
* LinkedIn
* Twitter

Each version adapts tone and formatting to the platform style.

---

## 4️⃣ Timeline Generator

Creates an event preparation timeline based on:

* Current date
* Event date
* Remaining preparation time

Example milestones:

* Venue booking
* Speaker confirmation
* Marketing campaign launch
* Equipment setup
* Event execution

---

## 5️⃣ Interactive Task Planner

EventBoom AI generates a checklist of planning tasks.

Features:

* Interactive checkbox tasks
* Persistent progress tracking
* Completion progress bar
* Stored progress inside event workspaces

This allows organizers to **track event readiness over time**.

---

## 6️⃣ Dynamic Registration Form Generator

Registration forms are generated automatically depending on event type.

Example for **tech events**:

* Team Name
* Team Size
* Programming Languages

Example for **sports events**:

* Team Name
* Player Position

The form schema adapts dynamically based on event category.

---

## 7️⃣ Event History & Workspace System

Each generated event is stored as a workspace:

```
prompt_history/
    event_1/
    event_2/
    event_3/
```

Each workspace contains:

* Event metadata
* Generated posters
* Social media content
* Timeline
* Todo progress
* Registration form structure

Users can **reopen previous events and continue planning**.

---

# 🖥️ Demo Interface

The system includes a **Streamlit interface** for interactive use.

### Interface Features

* Event prompt input
* Event date selector
* Poster preview
* Social media content preview
* Interactive task planner
* Event history sidebar
* Registration form preview

---

# 📂 Project Structure

```
backend/
│
├── analyzer/
│   └── prompt_analyzer.py
│
├── generators/
│   ├── poster_generator.py
│   ├── social_post_generator.py
│   ├── timeline_generator.py
│   ├── todo_generator.py
│   ├── form_generator.py
│   └── website_generator.py
│
├── planner/
│   └── task_planner.py
│
├── prompt_history/
│   └── event_workspaces
│
└── demo_app.py
```

---

# 🧪 Technologies Used

| Technology                | Purpose                         |
| ------------------------- | ------------------------------- |
| Python                    | Backend logic                   |
| Streamlit                 | Interactive interface           |
| HuggingFace Inference API | AI model access                 |
| Stable Diffusion          | Poster generation               |
| Pillow                    | Image processing                |
| JSON Storage              | Event workspace persistence     |
| HuggingFace CLI           | Authentication for model access |

---

# 🚀 Running the Project

## 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/EventBoom-AI.git
cd EventBoom-AI/backend
```

---

## 2️⃣ Install Dependencies

```
pip install streamlit huggingface_hub pillow
```

---

## 3️⃣ Authenticate with HuggingFace

EventBoom AI uses HuggingFace models for AI-powered generation.

Login using the HuggingFace CLI:

```
hf auth login
```

Paste your **HuggingFace access token** when prompted.

You can generate a token here:

```
https://huggingface.co/settings/tokens
```

The token will be stored locally and automatically used by the application.

---

## 4️⃣ Run the Application

```
streamlit run demo_app.py
```

The Streamlit interface will open in your browser.

---

# 🧪 Example Prompt

```
Organize a 2-day intercollege robotics competition called RoboRumble 2026 in Pune
for 300 engineering students featuring robot battle arenas,
autonomous bot challenges, and innovation showcases.
```

Generated outputs include:

* Poster variations
* Social media promotional posts
* Event preparation timeline
* Interactive todo checklist
* Registration form preview

---

# 🔮 Future Improvements

Potential future enhancements:

* Online form submission and response dashboard
* AI-driven budget estimation
* Multi-user event collaboration
* Automated event website deployment
* Ticketing platform integrations
* AI-based marketing strategy recommendations

---

# 🏁 Conclusion

EventBoom AI demonstrates how AI can transform event planning by automating:

* content creation
* coordination tasks
* preparation workflows

By combining **prompt analysis, generative AI, and workflow automation**, the system enables users to generate a **complete event launch kit from a single prompt**.

---

# 👨‍💻 Built For

**AMD Slingshot Hackathon**
Track: **AI for Everyone**
