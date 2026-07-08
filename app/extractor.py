import re
import pdfplumber
import io


def read_pdf(file_bytes):
    """
    Extract text from uploaded PDF
    """
    text = ""

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def get_value(pattern, text):
    match = re.search(pattern, text, re.MULTILINE)

    if match:
        return match.group(1).strip()

    return None


def extract_fields(text):

    claim = {}

    lines = [line.strip() for line in text.splitlines()]

    i = 0

    while i < len(lines):

        line = lines[i]

        if line == "":
            i += 1
            continue

        if line.startswith("Policy Number:"):
            claim["policy_number"] = line.replace("Policy Number:", "").strip()

        elif line.startswith("Policyholder:"):
            claim["policyholder_name"] = line.replace("Policyholder:", "").strip()

        elif line.startswith("Effective Dates:"):
            claim["effective_dates"] = line.replace("Effective Dates:", "").strip()

        elif line.startswith("Date:"):
            claim["incident_date"] = line.replace("Date:", "").strip()

        elif line.startswith("Time:"):
            claim["incident_time"] = line.replace("Time:", "").strip()

        elif line.startswith("Location:"):
            claim["location"] = line.replace("Location:", "").strip()

        elif line == "Description:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["description"] = lines[i]

        elif line == "Claimant:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["claimant"] = lines[i]

        elif line == "Third Parties:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["third_parties"] = lines[i]

        elif line == "Contact Details:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["contact_details"] = lines[i]

        elif line == "Asset Type:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["asset_type"] = lines[i]

        elif line == "Asset ID:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["asset_id"] = lines[i]

        elif line == "Estimated Damage:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["estimated_damage"] = lines[i]

        elif line == "Claim Type:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["claim_type"] = lines[i]

        elif line == "Attachments:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["attachments"] = lines[i]

        elif line == "Initial Estimate:":
            i += 1
            while i < len(lines) and lines[i] == "":
                i += 1
            claim["initial_estimate"] = lines[i]

        i += 1

    return claim