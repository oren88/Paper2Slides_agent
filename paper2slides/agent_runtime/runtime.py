"""Centralized runtime for LLM task execution."""
from typing import Any

from .models import AgentTaskInput, AgentTaskOutput


class AgentRuntime:
    """Dispatches task-shaped LLM calls via provider clients."""

    def run_openai_task(self, client: Any, task_input: AgentTaskInput) -> AgentTaskOutput:
        response = client.chat.completions.create(
            model=task_input.model,
            messages=task_input.messages,
            **task_input.options,
        )
        content = response.choices[0].message.content or ""
        return AgentTaskOutput(
            task_name=task_input.task_name,
            model=task_input.model,
            content=content,
            raw_response=response,
        )


runtime = AgentRuntime()
