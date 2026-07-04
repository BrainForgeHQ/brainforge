from pathlib import Path

from brainforge.pipelines.transcript_pipeline import TranscriptForge


def test_transcript_forge_reads_file(tmp_path):
    transcript = tmp_path / "sample.md"

    transcript.write_text(
        "Artificial Intelligence changes everything.",
        encoding="utf-8",
    )

    forge = TranscriptForge()

    evidence = forge.forge(str(transcript))

    assert evidence.source_type == "youtube_transcript"
    assert evidence.source_title == "sample"
    assert "Artificial Intelligence" in evidence.content