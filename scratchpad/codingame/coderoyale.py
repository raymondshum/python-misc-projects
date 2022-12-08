import sys
import math

class Utils:
    @staticmethod
    def print_debug(message):
        print(message, file=sys.stderr, flush=True)

    @staticmethod
    def print_list(list):
        for item in list:
            Utils.print_debug(item)
    
    @staticmethod
    def print_status(site_list, unit_list):
        Utils.print_debug("Site status:")
        Utils.print_list(site_list)
        
        Utils.print_debug("\nUnit status:")
        Utils.print_list(unit_list)


class Site:
    # structure_type: -1 = No structure, 2 = Barracks
    structure_types = {
        -1: "No structure",
        2: "Baracks",
        None: "Not Init."
    }

    # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
    owner_types = {
        -1: "No structure",
        0: "Player owner",
        1: "Enemy owner",
        None: "Not Init."
    }

    param2_types = {
        -1: "No structure",
        0: "Knight",
        1: "Archer",
        None: "Not init."
    }

    def __init__(self, site_id, x, y, radius):
        self.site_id = site_id
        self.x = x
        self.y = y
        self.radius = radius
        self.structure_type = None
        self.owner = None
        self.param1 = None # Num turns before a creep can be trained. 0 if can be trained this turn.
        self.param2 = None

    def set_current_turn_status(self, input_list):
        self.site_id, _, _, self.structure_type, self.owner, self.param1, self.param2 = input_list

    def __str__(self):
        return f"[{self.site_id}] ({self.x}, {self.y} | {self.radius}) : {Site.structure_types.get(self.structure_type)}, " \
            + f"{Site.owner_types.get(self.owner)}, {self.param1} turns left, {Site.param2_types.get(self.param2)}"
    
    def __repr__(self):
        return str(self)

class Unit:
    owner_types = {
        0: "PLAYER",
        1: "ENEMY",
        None: "Not Init."
    }
    # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
    unit_types = {
        -1: "Queen",
        0: "Knight",
        1: "Archer",
        None: "Not init."
    }

    QUEEN_RADIUS = 30
    QUEEN_MAX_DISTANCE = 60

    def __init__(self, x, y, owner, unit_type, health):
        self.x = x
        self.y = y
        self.owner = owner
        self.unit_type = unit_type
        self.health = health

    def __str__(self):
        return f"[{Unit.owner_types.get(self.owner)}] ({self.x}, {self.y}): {Unit.unit_types.get(self.unit_type)}, {self.health}HP"
    
    def __repr__(self):
        return str(self)

class Game:

    def __init__(self):
        self.site_list: list[Site] = []
        self.num_sites, self.site_list = self.load_sites()
        self.gold = 0
        self.touched_site = 0
        self.unit_list = []
    
    def load_sites(self):
        num_sites = int(input())
        site_list = []
        for i in range(num_sites):
            site_id, x, y, radius = [int(j) for j in input().split()]
            site_list.append(Site(site_id, x, y, radius))
        return num_sites, site_list
    
    def load_current_turn_status(self):
        self.gold, self.touched_site = [int(i) for i in input().split()]
        self._load_current_site_status()
        self._load_current_units_status()
    
    def _load_current_site_status(self):
        for i in range(self.num_sites):
            self.site_list[i].set_current_turn_status([int(j) for j in input().split()])
    
    def _load_current_units_status(self):
        num_units = int(input())
        self.unit_list = []
        for i in range(num_units):
            x, y, owner, unit_type, health = [int(j) for j in input().split()]
            self.unit_list.append(Unit(x, y, owner, unit_type, health))
    
    def get_queen_move(self):
        queen = self._get_queen()
        closest_site = self._get_closest_capturable_site(queen)
        if (queen_is_touching_site := self.touched_site != -1) \
            and (site_is_unbuilt := self.site_list[self.touched_site].owner == -1):
            # get type to build
            unit_type = "KNIGHT"
            return f"BUILD {self.touched_site} BARRACKS-{unit_type}"
        elif closest_site:
            return f"MOVE {closest_site.x} {closest_site.y}"
        else:
            return "WAIT"

    def _get_queen(self):
        for unit in self.unit_list:
            if Unit.unit_types.get(unit.unit_type) == "Queen":
                return unit

    def _get_closest_capturable_site(self, queen):
        capturable_sites = [site for site in self.site_list \
            if site.owner == (unbuilt := -1) and self.touched_site != site.site_id]

        closest_site = None
        min_distance = math.inf
        for site in capturable_sites:
            distance = self._getDistanceFromQueentToSite(queen, site)
            if distance < min_distance:
                closest_site = site
                min_distance = distance
        return closest_site
    
    def _getDistanceFromQueentToSite(self, queen, site):
        return math.sqrt( (queen.x - site.x) ** 2 + (queen.y - site.y) ** 2 )
    
    def get_train_move(self):
        ready_barracks: list[Site] = self._get_ready_barracks()
        trainable_units = self.gold // 80
        if trainable_units == 0 or not ready_barracks :
            return "TRAIN"
        else:
            barracks_nums = ""
            for barracks in ready_barracks:
                if self.gold - 80 < 0:
                    break
                barracks_nums += f"{barracks.site_id} "
                self.gold -= 80
            return f"TRAIN {barracks_nums}".strip()
    
    def _get_ready_barracks(self):
        return [site for site in self.site_list \
            if site.owner == (player := 0) and site.param1 == 0]

    def main(self):
        while True:
            self.load_current_turn_status()
            Utils.print_status(self.site_list, self.unit_list)

            queen_move = self.get_queen_move()
            train_move = self.get_train_move()

            # First line: A valid queen action
            # Second line: A set of training instructions
            print(queen_move)
            print(train_move)

if __name__ == "__main__":
    theGame = Game()
    theGame.main()


