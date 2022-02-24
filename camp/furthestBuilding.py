  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

      maxheap = []
      for i in range(1,len(heights)):
          cost = heights[i] - heights[i-1]
          if cost <= 0:
              continue

          bricks -= cost
          heappush(maxheap,-1*cost)

          while bricks < 0 and ladders > 0 and len(maxheap) > 0:
              poped = -1*heappop(maxheap)
              bricks += poped
              ladders -= 1 

          if bricks < 0:
              return i-1

      return len(heights)-1 
