from pydantic import BaseModel
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    version: str


class LengthStats(BaseModel):
    min: int
    max: int
    mean: float
    median: float


class QualityStats(BaseModel):
    mean_quality_per_read: list[float]
    low_quality_per_count: int
    quality_threshold: int


class AnalysisResponse(BaseModel):
    filename: str
    file_format: str
    total_sequences: int
    gc_content_per_seq: list[float]
    mean_gc_content: float
    length_stats: LengthStats
    quality_stats: Optional[QualityStats] = None