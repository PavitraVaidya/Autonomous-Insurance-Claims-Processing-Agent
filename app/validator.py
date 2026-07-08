MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "effective_dates",
    "incident_date",
    "incident_time",
    "location",
    "description",
    "claimant",
    "contact_details",
    "asset_type",
    "asset_id",
    "estimated_damage",
    "claim_type",
    "attachments",
    "initial_estimate"
]


def find_missing_fields(claim):
    missing = []

    for field in MANDATORY_FIELDS:
        value = claim.get(field)

        if value is None or str(value).strip() == "":
            missing.append(field)

    return missing