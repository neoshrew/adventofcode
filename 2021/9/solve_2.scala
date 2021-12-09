import scala.io.Source
import scala.collection.mutable.{Set, ListBuffer}

object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  type Coord = Tuple2[Int, Int]

  def main(args: Array[String]): Unit = {
    val grid = Source.fromFile(filename).getLines()
      .map(_.split("").map(_.toInt).toList)
      .toList

    val dimY = grid.length
    val dimX = grid(0).length

    def getNeighbours(coord: Coord): List[Coord] = {
      val (x, y) = coord
      List(
        if (y > 0) Some((x,y-1)) else None, // up
        if (y < dimY-1) Some((x,y+1)) else None, // down
        if (x > 0) Some((x-1,y)) else None, // left
        if (x < dimX-1) Some((x+1,y)) else None, // right
      ).filter(_.isDefined).map(_.get)
    }

    val minPoints = ListBuffer[Coord]()
    for (y <- 0 to dimY-1) {
      for (x <- 0 to dimX-1) {
        if (
          getNeighbours((x, y)).forall({case (nX, nY) => {grid(y)(x)<grid(nY)(nX)}})
        ) minPoints.append((x, y))
      }
    }

    val basinSizes = ListBuffer[Int]()
    for (minPoint <- minPoints) {
      val queue = Set(minPoint)
      val seen = Set[Coord]()
      while (queue.size > 0) {
        val curr = queue.head
        queue.remove(curr)
        seen.add(curr)
        queue.addAll(
          getNeighbours(curr)
          .filter(!seen.contains(_))
          .filter(coord => grid(coord._2)(coord._1) < 9)
        )
      }
      basinSizes.append(seen.size)
    }
    println(basinSizes
        .sorted
        .reverse
        .slice(0, 3)
        .foldLeft(1)((acc, curr) => acc*curr)
    )
  }
}
