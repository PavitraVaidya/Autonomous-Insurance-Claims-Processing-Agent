import json
import os
from datetime import datetime


def save_claim(result):

    os.makedirs("output", exist_ok=True)

    filename = f"claim_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    filepath = os.path.join("output", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    return filepath