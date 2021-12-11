import scala.io.Source
import collection.mutable.{ListBuffer, Set, Queue}


object solution {
  // val filename = "test1.txt"
  // val filename = "test2.txt"
  val filename = "input.txt"

  type Coord = Tuple2[Int, Int]
  type Grid = ListBuffer[ListBuffer[Int]]

  def main(args: Array[String]): Unit = {
    val grid = Source.fromFile(filename).getLines()
      .map(
        _.split("")
        .map(_.toInt)
        .to(ListBuffer)
      )
      .to(ListBuffer)

    var totalFlashes = 0
    printGrid(grid)
    for (x <- 1 to 100) {
        totalFlashes += step(grid)
        printGrid(grid)
    }
    println(totalFlashes)
  }

  def printGrid(grid: Grid): Unit = {
    println("-------")
    grid.foreach(row =>
      println(
        row.map(_.toString).mkString("")
      )
    )
    println("-------")
  }

  def step(grid: Grid): Int = {
    val toExplode = Queue[Coord]()

    for ((row, y) <- grid.zipWithIndex) {
      for ((_, x) <- row.zipWithIndex) {
        row(x) = row(x) + 1
        if (row(x) == 10) toExplode.append((x, y))
      }
    }

    while (toExplode.size > 0) {
      val curr = toExplode.dequeue()
      for ((x, y) <- neighbours(grid, curr)) {
        grid(y)(x) = grid(y)(x) + 1
        if (grid(y)(x) == 10) {
          toExplode.append((x, y))
        }
      }
    }

    var totalFlashes = 0
    for ((row, y) <- grid.zipWithIndex) {
      for ((currVal, x) <- row.zipWithIndex) {
        if (currVal >= 10) {
          row(x) = 0
          totalFlashes += 1
        }
      }
    }
    totalFlashes
  }

  def neighbours(grid: Grid, coord: Coord): List[Coord] = {
    val (x, y) = coord

    val retVal = ListBuffer[Coord]()
    for (dX <- List(-1, 0, 1)) {
      val nX = x+dX
      if (nX >= 0 && nX < grid(0).length) {
        for (dY <- List(-1, 0, 1)) {
          val nY = y+dY
          if (nY >= 0 && nY < grid.length) {
            if ((nX, nY) != coord) retVal.append((nX, nY))
          }
        }
      }
    }
    retVal.toList
  }
}
