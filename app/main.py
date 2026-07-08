from fastapi import FastAPI, UploadFile, File, HTTPException
from app.schemas import ClaimResponse
from app.validator import find_missing_fields
from app.router import route_claim
from app.ai_extractor import extract_with_ai
from app.utils import save_claim
import logging
from app.extractor import (
    extract_fields,
    read_pdf
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
app = FastAPI(
    title="Insurance Claims Processing Agent",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Insurance Claims Processing Agent is Running"
    }


@app.post(
    "/process-claim",
    response_model=ClaimResponse
)
async def process_claim(file: UploadFile = File(...)):

    contents = await file.read()

   
    if file.filename.endswith(".txt"):

        text = contents.decode("utf-8")


    elif file.filename.endswith(".pdf"):

        text = read_pdf(contents)

    else:

        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported."
        )
    logger.info("Uploaded document read successfully.")

    try:
        logger.info("Using Gemini AI for field extraction.")
        claim = extract_with_ai(text)

        logger.info("Using Gemini AI for field extraction.")
        logger.info(f"Extracted Claim: {claim}")
        

    except Exception as e:

        logger.error(f"Gemini extraction failed: {e}")

        logger.info("Using rule-based extractor as fallback.")

        claim = extract_fields(text)

    missing = find_missing_fields(claim)

    route, reason = route_claim(claim, missing)

    result = {

    "extractedFields": claim,

    "missingFields": missing,

    "recommendedRoute": route,

    "reasoning": reason

}

    saved_file = save_claim(result)

    logger.info(f"Claim saved to {saved_file}")

    return result
