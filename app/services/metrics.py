import statistics
import logging
from Bio.SeqRecord import SeqRecord


logger = logging.getLogger(__name__)
DEFAULT_QUALITY_THRESHOLD = 20

def calculate_gc(sequence: str) -> float:
    """
    Computes GC content as a percentage for a single DNA sequence string.
    """
    if len(sequence) == 0:
        return 0.0
    
    sequence = sequence.upper()
    gc_count = sequence.count("G")+sequence.count("C")

    return (gc_count / len(sequence)) * 100


def compute_length_stats(lengths: int) -> dict:
    """
    Given a list of sequence lengths, returns min, max, mean, median.
    """
    return {
        "min": min(lengths),
        "max": max(lengths),
        "mean": round(statistics.mean(lengths), 2),
        "median": round(statistics.median(lengths), 2),
    }


def quality_score(records: list[SeqRecord], threshold: int = DEFAULT_QUALITY_THRESHOLD) -> dict:
    """
     Computes per-read mean Phred quality scores for FASTQ records.
    """
    mean_quality_scores = []

    for record in records:
        qualities = record.letter_annotation.get("phred_quality", [])

        if len(qualities) == 0:
            mean_quality_scores.append(0.0)
        else:
            mean_quality_scores.append(round(statistics.mean(qualities), 4))
    
    low_quality_count = sum(1 for score in mean_quality_scores if score < threshold)

    return {
        "mean_quality_per_read": mean_quality_scores,
        "low_quality_per_count": low_quality_count,
        "quality_threshold": threshold
    }


def analyze_records(records: list[SeqRecord], file_format: str) -> dict:
    """
    Orchestrator — calls all metric functions and returns a single dict
    that maps directly onto the AnalysisResponse Pydantic schema.
    """
    sequences = [str(record.seq) for record in records]

    gc_content_per_seq = [calculate_gc(seq) for seq in sequences]
    mean_gc_content = round(statistics.mean(gc_content_per_seq), 4) if gc_content_per_seq else 0.0

    lengths = [len(seq) for seq in sequences]
    length_stats = compute_length_stats(lengths)

    quality_stats = None
    if file_format == "fastq":
        quality_stats = quality_score(records)

    logger.info(
        f"Analyzed {len(records)} records: "
        f"Mean GC content: {mean_gc_content}%, "
        f"Length stats min: {length_stats['min']}, "
        f"max: {length_stats['max']}, "
        f"Quality stats: {quality_stats}"
    )

    return {
        "total_records": len(records),
        "total_sequences": len(sequences),
        "mean_gc_content": mean_gc_content,
        "length_stats": length_stats,
        "quality_stats": quality_stats
    }