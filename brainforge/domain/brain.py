from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import List
from uuid import UUID, uuid4

from brainforge.domain.knowledge_unit import KnowledgeUnit


@dataclass
class Brain:
    """
    A continuously evolving cognitive system that organizes knowledge
    around a specific domain, person, company, project, or topic.
    """

    id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: str = ""
    purpose: str = ""
    knowledge_units: List[KnowledgeUnit] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    version: str = "0.1.0"
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def add_knowledge_unit(self, knowledge_unit: KnowledgeUnit) -> None:
        self.knowledge_units.append(knowledge_unit)