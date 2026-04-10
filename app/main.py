import logging
from fastapi import FastAPI
from app.routes.analyze import router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Genomic Sequence Analyzer",
    description="Upload a FASTA or FASTQ file and get back GC content, length stats, and quality metrics.",
    version="1.0.0"
)

app.include_router(router)

logger.info("Application startup complete. Ready to accept requests.")