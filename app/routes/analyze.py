import logging
import time

from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.metrics import analyze_records
from app.services.parser import parse_sequences
from app.schemas.response import AnalysisResponse, HealthResponse
from app.utils.file_handler import detect_format, save_upload_to_temp, delete_temp_file


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", version="1.0.0", timestamp=int(time.time()))


@router.get("/analyze")
async def analyze_info():
    return {
        "message": "Use POST /analyze with a FASTA or FASTQ file."
    }


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze(file: UploadFile = File(...)):
    start_time = time.time()
    logger.info(f"Received file for analysis: {file.filename} ({file.content_type})")

    file_format = detect_format(file.filename)
    temp_file = await save_upload_to_temp(file)

    try:
        try:
            sequences = parse_sequences(temp_file, file_format)
        except ValueError as e:
            raise HTTPException(status_code=422, detail=str(e))
        
        metrics = analyze_records(sequences, file_format)
    
    finally:
        delete_temp_file(temp_file)
    
    elapsed_time = round(time.time() - start_time, 2)
    logger.info(f"Completed analysis for {file.filename} with {metrics['total_sequences']} in {elapsed_time} seconds")

    return AnalysisResponse(
        filename=file.filename,
        file_format=file_format,
        **metrics,
    )