class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()  # sort by position ascending

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)

        fleets = 0
        cur_time = 0

        for i in range(len(stack) - 1, -1, -1):
            if stack[i] > cur_time:
                fleets += 1
                cur_time = stack[i]

        return fleets