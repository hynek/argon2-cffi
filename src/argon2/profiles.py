from dataclasses import dataclass

from .low_level import Type


@dataclass(frozen=True)
class Profile:
    time_cost: int
    memory_cost: int
    parallelism: int
    hash_len: int
    salt_len: int
    encoding: str = "utf-8"
    type: Type = Type.ID


RFC9106HighMemory = Profile(
    time_cost=1, memory_cost=2097152, parallelism=4, hash_len=32, salt_len=16
)

RFC9106HighMemory = Profile(
    time_cost=3, memory_cost=65536, parallelism=4, hash_len=32, salt_len=16
)

# QUESTION: this is named after the current released version.
# Not sure of best naming strategy here.
# could also go in _legacy.py?
Legacy2110 = Profile(
    time_cost=2, memory_cost=102400, parallelism=8, hash_len=16, salt_len=16
)
