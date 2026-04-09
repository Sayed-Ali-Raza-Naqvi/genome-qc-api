import logging
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


logger = logging.getLogger(__name__)

def parse_sequences(file_path: str, file_format: str) -> list[SeqRecord]:
    """
    Parses a sequence file and returns a list of SeqRecord objects.

    Parameters:
    -----------
    - file_path: The path to the sequence file.
    - file_format: The format of the sequence file (e.g., "fasta", "fastq").

    Returns:
    --------
    - A list of SeqRecord objects parsed from the file.    
    SeqRecord contains:
        - record.id: The identifier of the sequence.
        - record.seq: The sequence itself as a Seq object.
        - record.letter_annotations: A dictionary of annotations for the sequence, such as quality scores for FASTQ files.

    Raises:
    -------
    - ValueError: If the file cannot be parsed or if no sequences are found.
    """
    try:
        records = list(SeqIO.parse(file_path, file_format))
    except Exception as e:
        raise ValueError(
            f"Failed to parse file: {file_format}"
            f"Make sure the file is valid: {e}"
        ) from e
    
    if len(records) == 0:
        raise ValueError("No sequences found in the file. Please upload a non-empty file.")
    
    logger.info(f"Parsed {len(records)} from {file_path} with format {file_format}")

    return records