class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        l = len(distance)
        if not distance:
            return 0
        
        if start < 0:
            return 0 
        if start == destination:
            return 0 
        if start>destination:
            start, destination = destination, start
            
        clockwise = 0 
        anticlockwise = sum(distance[:start]) 
        print(anticlockwise)
        print(start,destination)
        for i in range(start,destination):
            clockwise += distance[i]
        for i in range(destination, l):
            anticlockwise += distance[i]
        
        return min(clockwise,anticlockwise)