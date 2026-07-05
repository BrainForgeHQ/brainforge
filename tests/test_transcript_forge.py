from brainforge.pipelines.transcript_pipeline import TranscriptForge


def test_transcript_forge_creates_evidence_per_paragraph(tmp_path):
    transcript = tmp_path / "sample.md"

    transcript.write_text(
        "First paragraph.\n\nSecond paragraph.\n\nThird paragraph.",
        encoding="utf-8",
    )

    forge = TranscriptForge()

    evidence_list = forge.forge(str(transcript))

    assert len(evidence_list) == 3
    assert evidence_list[0].source_type == "youtube_transcript"
    assert evidence_list[0].source_title == "sample"
    assert evidence_list[0].content == "First paragraph."
    assert evidence_list[1].content == "Second paragraph."
    assert evidence_list[2].content == "Third paragraph."