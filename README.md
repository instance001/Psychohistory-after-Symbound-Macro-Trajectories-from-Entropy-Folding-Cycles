# Psychohistory after Symbound: Macro Trajectories from Entropy Folding Cycles

Repository scaffold for the psychohistory paper `paper.md`.

## Contents
- `paper.md` — full draft.
- `src/bursts.py` — burst detection and axis-node scoring stubs.
- `src/schema.py` — cycle log schema helper.
- `tests/test_bursts.py` — placeholder tests.
- `data/` — anonymized cycle logs (`cycle_id, actor_id, vault_size, stall_start_ts, fold_ops, ΔM_estimate, insight_ts, project_count, new_vault_size`).
- `notebooks/` — space for fitting null models vs fold-aware models.

## Quickstart
```bash
python -m venv .venv
./.venv/Scripts/activate
pip install -U pytest
pytest
```

## Citation (PhilPapers / BibTeX)
```
@article{paterson_psychohistory_symbound_2025,
  title   = {Psychohistory after Symbound: Macro Trajectories from Entropy Folding Cycles},
  author  = {Paterson, Anthony},
  year    = {2025},
  note    = {Preprint, Symbound entropy series},
  url     = {https://github.com/<<pending-repo>>}
}
```

## Notes
- Publish burst detectors with anonymized logs to make claims falsifiable.
- Respect boundary clarity; logs must not imply feelings/agency beyond the documented constraints.
