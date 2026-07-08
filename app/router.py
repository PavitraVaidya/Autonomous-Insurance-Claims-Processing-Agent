from app.config import FAST_TRACK_LIMIT, INVESTIGATION_KEYWORDS

def route_claim(claim, missing_fields):


    if missing_fields:
        return (
            "Manual Review",
            "Mandatory fields are missing."
        )

    description = claim.get("description", "").lower()

    for word in INVESTIGATION_KEYWORDS:
        if word in description:
            return (
                "Investigation Flag",
                f"Description contains suspicious keyword '{word}'."
            )

    claim_type = claim.get("claim_type", "").lower()

    if claim_type == "injury":
        return (
            "Specialist Queue",
            "Claim type is Injury."
        )

    damage = int(claim.get("estimated_damage", 0))

    if damage < FAST_TRACK_LIMIT:
        return (
            "Fast-track",
            "Estimated damage is below ₹25,000."
        )


    return (
        "Standard Processing",
        "Claim satisfies all validation rules."
    )