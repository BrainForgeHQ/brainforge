from brainforge.builders.knowledge_builder import KnowledgeBuilder
from brainforge.domain.evidence import Evidence


def test_knowledge_builder_creates_knowledge_unit_from_evidence():
    evidence = Evidence(
        source_type="youtube_transcript",
        source_title="sample",
        content="Artificial Intelligence will transform every industry.",
    )

    builder = KnowledgeBuilder()

    ku = builder.build(evidence)

    assert ku.title == "Artificial Intelligence will transform every industry"
    assert ku.statement == "Artificial Intelligence will transform every industry."
    assert ku.evidence[0] == evidence
    assert ku.confidence == 0.80