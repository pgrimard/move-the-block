from dataclasses import dataclass


@dataclass
class Board:
    width: int
    height: int
    fps: int