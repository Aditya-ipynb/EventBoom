import os
from huggingface_hub import InferenceClient
from PIL import Image, ImageDraw, ImageFont

FINAL_WIDTH = 1080
FINAL_HEIGHT = 1350

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN")
)

EVENT_PROMPT_STYLES = {

    "music": """
    massive concert crowd, stage lights, DJ or live band,
    energetic festival atmosphere, neon lighting, night event
    """,

    "tech": """
    futuristic tech conference stage, glowing screens,
    developers with laptops, modern technology environment,
    cyberpunk lighting, innovation theme
    """,

    "sports": """
    stadium environment, cheering crowd, athletes in action,
    stadium floodlights, energetic sports atmosphere
    """,

    "academic": """
    university lecture hall, presentation stage,
    academic conference environment, students and speakers
    """,

    "cultural": """
    colorful cultural festival, traditional decorations,
    vibrant lighting, celebration atmosphere
    """,

    "business": """
    modern corporate conference stage,
    professional seminar setting, business presentation
    """,

    "social": """
    festive gathering, celebration event,
    decorative lights, joyful crowd atmosphere
    """
}

VARIATIONS = [
    "cinematic lighting",
    "dramatic spotlight",
    "neon festival lighting",
    "fireworks celebration lighting"
]


def add_title_overlay(image, event_name):

    draw = ImageDraw.Draw(image)
    width, height = image.size

    font_path = os.path.join(os.path.dirname(__file__), "BebasNeue-Regular.ttf")

    max_width = width * 0.9
    font_size = 150

    words = event_name.split()

    while font_size > 30:

        font = ImageFont.truetype(font_path, font_size)

        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + " " + word if current_line else word
            bbox = draw.textbbox((0, 0), test_line, font=font)
            test_width = bbox[2] - bbox[0]

            if test_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        line_widths = [
            draw.textbbox((0, 0), line, font=font)[2] for line in lines
        ]

        if max(line_widths) <= max_width:
            break

        font_size -= 5

    line_height = draw.textbbox((0, 0), "Ay", font=font)[3]

    padding = 60
    overlay_height = len(lines) * line_height + padding

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    overlay_draw.rectangle(
        [(0, 0), (width, overlay_height)],
        fill=(0, 0, 0, 160)
    )

    image = Image.alpha_composite(image, overlay)
    draw = ImageDraw.Draw(image)

    y = (overlay_height - len(lines) * line_height) / 2

    for line in lines:

        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]

        x = (width - text_width) / 2

        draw.text(
            (x, y),
            line,
            font=font,
            fill="white",
            stroke_width=4,
            stroke_fill="black"
        )

        y += line_height

    return image


def add_highlights_overlay(image, highlights):

    if not highlights:
        return image

    draw = ImageDraw.Draw(image)
    width, height = image.size

    font_path = os.path.join(os.path.dirname(__file__), "BebasNeue-Regular.ttf")
    font = ImageFont.truetype(font_path, 45)

    max_width = width * 0.9

    words = highlights
    lines = []
    current_line = ""

    for word in words:

        item = word.upper()

        test_line = current_line + " • " + item if current_line else item

        bbox = draw.textbbox((0, 0), test_line, font=font)
        test_width = bbox[2] - bbox[0]

        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = item

    if current_line:
        lines.append(current_line)

    line_height = draw.textbbox((0, 0), "Ay", font=font)[3]

    overlay_height = len(lines) * line_height + 60
    start_y = height - overlay_height - 20

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    overlay_draw.rectangle(
        [(0, start_y), (width, height)],
        fill=(0, 0, 0, 160)
    )

    image = Image.alpha_composite(image, overlay)

    draw = ImageDraw.Draw(image)

    y = start_y + 20

    for line in lines:

        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]

        x = (width - text_width) / 2

        draw.text(
            (x, y),
            line,
            font=font,
            fill="white",
            stroke_width=2,
            stroke_fill="black"
        )

        y += line_height

    return image

def shorten_title(title, max_words=3):

    words = title.split()

    if len(words) <= max_words:
        return title

    return " ".join(words[:max_words])

def build_poster_prompt(event_data, variation):

    category = event_data.get("primary_category", "social")
    keywords = " ".join(event_data.get("keywords", []))
    highlights = ", ".join(event_data.get("key_highlights", []))

    style_prompt = EVENT_PROMPT_STYLES.get(category, EVENT_PROMPT_STYLES["social"])

    prompt = f"""
    professional poster background for a {category} event,
    {style_prompt},
    key elements: {keywords},
    event highlights: {highlights},
    {variation},
    poster layout, no text, no watermark,
    large empty gradient space at top for title text,
    cinematic lighting, highly detailed, photorealistic
    """

    return prompt

def generate_event_posters(event_data, num_variations=4):

    event_name = event_data.get("event_name", "Event")
    poster_title = shorten_title(event_name)
    category = event_data.get("primary_category", "social")
    highlights = event_data.get("key_highlights", [])

    style_prompt = EVENT_PROMPT_STYLES.get(category, EVENT_PROMPT_STYLES["social"])

    poster_paths = []

    for i in range(num_variations):

        variation = VARIATIONS[i % len(VARIATIONS)]

        image_prompt = build_poster_prompt(event_data, variation)

        image = client.text_to_image(
            prompt=image_prompt,
            model="black-forest-labs/FLUX.1-schnell",
            width=832,
            height=1024
        )

        image = image.resize((FINAL_WIDTH, FINAL_HEIGHT), Image.LANCZOS)
        image = image.convert("RGBA")

        image = add_title_overlay(image, poster_title)
        image = add_highlights_overlay(image, highlights)

        output_path = f"poster_variation_{i+1}.png"
        image.save(output_path)

        poster_paths.append(output_path)

    return poster_paths
