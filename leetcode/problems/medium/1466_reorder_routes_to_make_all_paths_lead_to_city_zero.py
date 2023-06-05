from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Key Point: Use DFS to traverse from city 0 to all other nodes
        and compare the path between nodes to the input.

        Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

        Method: Build an adjacency map from the input. Also build
        a set of directional edges (roads) between nodes (cities).
        Then use DFS to visit all nodes from city 0. Compare
        each edge to the edges within the set. If the edge exists,
        then the road is going in the right direction. If the 
        edge does not exist, it needs to be swapped. 

        Returns: Int representing the number of roads that need
        to have their direction swapped for all roads to lead
        city 0.
        """
        road_map:       Dict[List[int]]      = defaultdict(list)
        roads:          Set[Tuple(int, int)] = set()
        capital_city:   int                  = 0
        visited_cities: Set[int]             = set()

        # build map of initial road layout and connected cities
        for city_1, city_2 in connections:
            road_map[city_1].append(city_2)
            road_map[city_2].append(city_1)
            roads.add((city_1, city_2))

        def dfs_count_swapped_roads(city: int) -> int:
            num_roads_to_swap: int = 0
            visited_cities.add(city)
            for neighbor in road_map[city]:
                if neighbor in visited_cities:
                    continue
                if (neighbor, city) not in roads:
                    num_roads_to_swap += 1
                num_roads_to_swap += dfs_count_swapped_roads(neighbor)
            return num_roads_to_swap

        return dfs_count_swapped_roads(capital_city)