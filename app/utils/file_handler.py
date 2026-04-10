import os
import tempfile
import logging
from fastapi import UploadFile, HTTPException


logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = {
    ".fasta": "fasta",
    ".fa": "fasta",
    ".fastq": "fastq",
    ".fq": "fastq",
}

def detect_format(file: UploadFile) -> str:
    _, ext = os.path.splitext(file.lower())

    if ext not in SUPPORTED_FORMATS:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported file format '{ext}'." 
                    f"Supported formats are: {', '.join(SUPPORTED_FORMATS.keys())}"
        )

    return SUPPORTED_FORMATS[ext]


async def save_upload_to_temp(file: UploadFile) -> str:
    contents = await file.read()
    _, ext = os.path.splitext(file.filename)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=ext)

    try:
        tempfile.write(contents)
        tempfile.flush()
    finally:
        tempfile.close()

    logger.info(f"Saved uploaded file to temporary location: {temp_file.name}")
    
    return temp_file.name


def delete_temp_file(file: str):
    try:
        os.remove(file)
        logger.info(f"Deleted temporary file: {file}")
    except FileNotFoundError:
        pass