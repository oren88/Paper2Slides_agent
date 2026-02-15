"""Agent runtime task contracts for LLM-backed units."""
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentTaskInput:
    """Base task input."""
    task_name: str
    model: str
    messages: List[Dict[str, Any]]
    options: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentTaskOutput:
    """Base task output."""
    task_name: str
    model: str
    content: str
    raw_response: Any = None


@dataclass
class FastRagQueryInput:
    """Input for fast RAG direct query task."""
    category: str
    query: str
    model: str
    messages: List[Dict[str, Any]]
    temperature: float = 0.3


@dataclass
class FastRagQueryOutput:
    """Output for fast RAG direct query task."""
    query: str
    answer: Optional[str]
    mode: str = "fast_direct_with_vision"
    success: bool = True
    error: Optional[str] = None
