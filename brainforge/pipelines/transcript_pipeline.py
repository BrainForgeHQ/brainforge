from pathlib import Path

from brainforge.domain.evidence import Evidence


class TranscriptForge:
    """
    Reads a transcript and converts every paragraph into an Evidence object.
    """

    def forge(self, transcript_path: str) -> list[Evidence]:

        path = Path(transcript_path)

        content = path.read_text(encoding="utf-8")

        paragraphs = [
            p.strip()
            for p in content.split("\n\n")
            if p.strip()
        ]

        evidence_list = []

        for paragraph in paragraphs:

            evidence = Evidence(
                source_type="youtube_transcript",
                source_title=path.stem,
                source_url="",
                content=paragraph,
            )

            evidence_list.append(evidence)

        return evidence_list