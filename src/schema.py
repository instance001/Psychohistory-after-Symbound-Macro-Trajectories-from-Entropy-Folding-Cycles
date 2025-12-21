"""
Cycle log schema helper.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CycleLog:
    cycle_id: str
    actor_id: str
    vault_size: int
    stall_start_ts: float
    fold_ops: int
    delta_capacity: float
    insight_ts: float
    project_count: int
    new_vault_size: int
    note: Optional[str] = None
