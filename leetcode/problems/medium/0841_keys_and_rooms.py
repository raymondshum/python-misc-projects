from collections import defaultdict
class Solution:
    """
    Key Point: Treat input as an adjacency list and traverse
    using DFS.

    Link: https://leetcode.com/problems/keys-and-rooms/

    Method: Build adjacency list from input. DFS from node
    0. If number of rooms visited is equal to total number
    of rooms, then you can visit all rooms.

    Returns: True if can visit all rooms and False if not.
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        STARTING_ROOM:       int            = 0
        can_visit_all_rooms: bool           = False
        key_ring:            Dict[Set[int]] = defaultdict(set)
        used_keys:           Set[int]       = set()

        # build adjacency list
        for room_number, keys in enumerate(rooms):
            for key in keys:
                key_ring[room_number].add(key)
        
        # travel via DFS
        def dfs_visit_room(room_number: int) -> None:
            used_keys.add(room_number)
            for key in key_ring[room_number]:
                if key in used_keys:
                    continue
                dfs_visit_room(key)
                    
        dfs_visit_room(STARTING_ROOM)
        return len(used_keys) == len(rooms)