from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List
from uuid import UUID, uuid4


@dataclass
class KnowledgeUnit:
    """
    Smallest independent unit of expertise inside BrainForge.
    """

    id: UUID = field(default_factory=uuid4)
    title: str = ""
    statement: str = ""
    evidence: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    relationships: List[UUID] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
    confidence: float = 1.0
    created_at: datetime = field(default_factory=datetime.utcnow)