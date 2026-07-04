from pathlib import Path

from brainforge.domain.evidence import Evidence


class TranscriptForge:
    """
    Reads a transcript file and converts it into an Evidence object.
    """

    def forge(self, transcript_path: str) -> Evidence:

        path = Path(transcript_path)

        content = path.read_text(encoding="utf-8")

        return Evidence(
            source_type="youtube_transcript",
            source_title=path.stem,
            source_url="",
            content=content,
        )