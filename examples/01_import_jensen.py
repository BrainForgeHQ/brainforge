from brainforge.domain.brain import Brain
from brainforge.domain.knowledge_unit import KnowledgeUnit
from brainforge.pipelines.transcript_pipeline import TranscriptForge


def main():
    brain = Brain(
        name="Jensen Huang",
        description="Knowledge Brain for NVIDIA CEO Jensen Huang.",
        purpose="Capture and organize Jensen's thinking.",
    )

    forge = TranscriptForge()

    evidence = forge.forge(
        "brains/jensen/assets/jensen_intro.md"
    )

    ku = KnowledgeUnit(
        title="AI transforms industries",
        statement="Artificial Intelligence will transform every industry.",
        evidence=[evidence],
        confidence=0.95,
    )

    brain.add_knowledge_unit(ku)

    print("===================================")
    print(" BrainForge Example")
    print("===================================")
    print(f"Brain: {brain.name}")
    print(f"Knowledge Units: {len(brain.knowledge_units)}")
    print(f"First KU: {brain.knowledge_units[0].title}")
    print(f"Evidence Type: {brain.knowledge_units[0].evidence[0].source_type}")
    print(f"Evidence Title: {brain.knowledge_units[0].evidence[0].source_title}")
    print("===================================")


if __name__ == "__main__":
    main()