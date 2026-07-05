from brainforge.domain.brain import Brain
from brainforge.builders.knowledge_builder import KnowledgeBuilder
from brainforge.pipelines.transcript_pipeline import TranscriptForge


def main():

    brain = Brain(
        name="Jensen Huang",
        description="Knowledge Brain for NVIDIA CEO Jensen Huang.",
        purpose="Capture and organize Jensen's thinking.",
    )

    forge = TranscriptForge()
    builder = KnowledgeBuilder()

    evidence_list = forge.forge(
        "brains/jensen/assets/jensen_intro.md"
    )

    for evidence in evidence_list:

        ku = builder.build(evidence)

        brain.add_knowledge_unit(ku)

    print("===================================")
    print(" BrainForge")
    print("===================================")
    print(f"Brain: {brain.name}")
    print(f"Knowledge Units: {len(brain.knowledge_units)}")
    print()

    for ku in brain.knowledge_units:

        print(f"- {ku.title}")

    print("===================================")


if __name__ == "__main__":
    main()