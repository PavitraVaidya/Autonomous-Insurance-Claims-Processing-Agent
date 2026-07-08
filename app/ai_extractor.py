import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_with_ai(text: str):

    prompt = f"""
You are an AI Insurance Claims Processing Agent.

Extract the following fields from the FNOL document.

Return ONLY valid JSON.

Fields:

policy_number
policyholder_name
effective_dates
incident_date
incident_time
location
description
claimant
third_parties
contact_details
asset_type
asset_id
estimated_damage
claim_type
attachments
initial_estimate

FNOL Document:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    response_text = response.text.strip()

   
    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "").replace("```", "").strip()

    return json.loads(response_text)