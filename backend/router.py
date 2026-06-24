def route_query(message):
    import re

    msg = message.lower()

    # Calculator
    if re.fullmatch(r"[0-9\s\+\-\*\/\(\)\.]+", msg):
        return "calculator"

    # Weather
    elif "weather" in msg:
        return "weather"

    # GitHub
    elif "github" in msg:
        return "github"

    # Railway
    elif "railway" in msg or "train" in msg or "pnr" in msg:
        return "railway"

    # Parking
    elif "parking" in msg:
        return "parking"

    # Traffic
    elif "traffic" in msg:
        return "traffic"

    # Hospital
    elif "hospital" in msg:
        return "hospital"

    # Police
    elif "police" in msg:
        return "police"

    # News
    elif "news" in msg:
        return "news"

    # Fuel
    elif "fuel" in msg:
        return "fuel"

    # EV
    elif "ev" in msg:
        return "ev"

    # Sensors
    elif "sensor" in msg:
        return "sensor"

    # Resume
    elif "resume" in msg:
        return "resume"

    # Portfolio
    elif "portfolio" in msg:
        return "portfolio"

    # Research
    elif "research" in msg or "analyze" in msg:
        return "research"

    # PDF
    elif "pdf" in msg:
        return "pdf"

    # Image
    elif "image" in msg:
        return "image"

    # Coding
    elif any(word in msg for word in [
        "code",
        "react",
        "python",
        "javascript",
        "html",
        "css",
        "fastapi"
    ]):
        return "code"

    return "llm"