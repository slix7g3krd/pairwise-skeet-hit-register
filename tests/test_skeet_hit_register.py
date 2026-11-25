import pytest
import gameplay.skeet_hit_register as mod

CASES = [
    ("trap_server_schedule", (1,)),
    ("pellet_cone_hit", (1,)),
    ("shot_queue", (1,)),
    ("replay_av_sync", (1,)),
    ("object_pool_recycle", (1,)),
    ("hit_single_judge", (1,)),
    ("load_range", (1,)),
    ("launch", (1,)),
    ("shoot", (1,)),
    ("present", (1,)),
    ("validate_hit", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
