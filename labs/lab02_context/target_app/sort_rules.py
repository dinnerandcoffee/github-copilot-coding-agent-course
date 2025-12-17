from __future__ import annotations

from datetime import datetime
from typing import Any


def _parse_created_at(value: str) -> datetime:
    # created_at is ISO 8601 like "2025-12-01T09:00:00Z"
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)


def sort_tasks(tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        tasks,
        key=lambda task: (
            bool(task.get("done", False)),
            -int(task.get("priority", 1)),
            _parse_created_at(str(task.get("created_at", "1970-01-01T00:00:00Z"))),
        ),
    )

