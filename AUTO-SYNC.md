# Automatic native corpus synchronization

Every registered corpus update to its `main` branch is eligible for automatic
master refresh. The master checks all 18 public native heads every five minutes,
on master pushes, or on manual/authorized repository-dispatch runs. No new secret
or cross-repository write credential is required for the scheduled mechanism.
GitHub may delay scheduled jobs; five minutes is the configured polling interval,
not a guaranteed delivery deadline. GitHub can disable public-repository schedules
after 60 days without repository activity; check the workflow status if it stops.

The workflow compares exact native main commit IDs with the accepted state.
Unchanged members avoid cloning and recomputation. A changed member is checked
out at the exact discovered commit and its actual `scripts/validate_ai_skill.py`
is run before the master advances that member's checkpoint. If native main moves
during validation, or the skill fails, the previous accepted commit stays pinned
and [the status page](MEMBER-STATUS.md) reports pending/failed status explicitly.
The following outputs update automatically:

- [registry/member-state.json](registry/member-state.json): exact observed and
  accepted commits, skill and bundle hashes, source parent, scope and status.
- [MEMBER-STATUS.md](MEMBER-STATUS.md): the readable per-corpus state.
- [migration/member-checkpoints.json](migration/member-checkpoints.json): accepted
  source revisions used by dedicated native-member CI.
- The generated master fingerprint index and instruction-only starter download.

No native inscription payload is copied and no scholarly interpretation is
invented by synchronization. `SKILL.md` instructs readers to use the refreshed
state and current native authorities. Scientific gates, source dependence,
uncertainty and source-specific rights remain native responsibilities. New member
admission or a changed skill contract requires deliberate registry review.

Publication checks that the master source parent still matches remote main.
Concurrent source changes skip or reject publication; outputs are never rebased
or force-pushed. The same job validates generated files before publishing because
workflow-token pushes do not trigger an additional GitHub Actions push build.

Instant native-to-master dispatch would additionally require a GitHub App/token
with access to the master repository. The configured polling route works without
that additional credential and does not require anyone to refresh manually.
