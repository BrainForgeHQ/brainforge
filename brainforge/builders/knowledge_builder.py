from brainforge.domain.knowledge_unit import KnowledgeUnit
from brainforge.domain.evidence import Evidence


class KnowledgeBuilder:
    """
    Builds Knowledge Units from Evidence.
    """

    def build(self, evidence: Evidence) -> KnowledgeUnit:

        title = evidence.content.split(".")[0][:80]

        return KnowledgeUnit(
            title=title,
            statement=evidence.content,
            evidence=[evidence],
            confidence=0.80,
        )