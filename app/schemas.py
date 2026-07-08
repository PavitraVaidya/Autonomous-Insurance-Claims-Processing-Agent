from pydantic import BaseModel
from typing import Optional


from typing import Optional
from pydantic import BaseModel

class ExtractedFields(BaseModel):
    policy_number: Optional[str] = None
    policyholder_name: Optional[str] = None
    effective_dates: Optional[str] = None

    incident_date: Optional[str] = None
    incident_time: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

    claimant: Optional[str] = None
    third_parties: Optional[str] = None
    contact_details: Optional[str] = None

    asset_type: Optional[str] = None
    asset_id: Optional[str] = None

    estimated_damage: Optional[int] = None   

    claim_type: Optional[str] = None
    attachments: Optional[str] = None

    initial_estimate: Optional[int] = None  


class ClaimResponse(BaseModel):
    extractedFields: ExtractedFields
    missingFields: list[str]
    recommendedRoute: str
    reasoning: str