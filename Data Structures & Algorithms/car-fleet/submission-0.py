class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        new_list = []
        for i in range(len(position)):
            new_list.append((position[i], speed[i]))

        sorted_list = sorted(new_list, reverse=True)
        for pos, spd in sorted_list:
            t = (target - pos) / spd
            if not fleets:
                fleets.append(t)
            elif t > fleets[-1]:
                fleets.append(t)

        return len(fleets)
            
