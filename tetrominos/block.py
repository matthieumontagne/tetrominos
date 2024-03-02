"""This class contains the code related to Blocks objects
The Block is the smallest subdivision of the game matrix.
A collection of blocks, with known coordinates can be represented in a BlockCollection
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = ["Block", "BlockCollection"]


@dataclass
class Block:
    """This class represents a block."""

    color: tuple[int, int, int]


class BlockCollection:
    """The BlockCollection is a dataclass whose purpose is to
    store a collections of blocks with their coordinates
    The data is contained inside a dict where:
    - the key is the coordinate
    - the value is a block object
    This structure is intended to improve performance when accessing
    the block existing at a certain coordinate
    """

    def __init__(self) -> None:
        self.collection: dict[tuple[int, int], Block] = {}

    def add(self, coordinate: tuple[int, int], block: Block) -> None:
        """Add a new block to the collection"""
        self.collection[coordinate] = block

    def pop(self, coordinate: tuple[int, int]) -> None:
        """Remove a block from the collection"""
        self.collection.pop(coordinate)

    def __or__(self, other_collection) -> BlockCollection:
        """Define the or operator (|) as a merge operator for this class"""
        merged_dicts: dict[tuple[int, int], Block] = (
            self.collection | other_collection.collection
        )
        merged_collection = BlockCollection()

        for coordinates, blocks in merged_dicts.items():
            merged_collection.add(coordinates, blocks)

        return merged_collection
