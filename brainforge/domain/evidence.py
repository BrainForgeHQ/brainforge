from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Dict, List
from uuid import UUID, uuid4


@dataclass
class Evidence:
    """
    A source-backed piece of information that supports one or more Knowledge Units.
    """

    id: UUID = field(default_factory=uuid4)
    source_type: str = ""
    source_title: str = ""
    source_url: str = ""
    content: str = ""
    author: str = ""
    published_at: str = ""
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))