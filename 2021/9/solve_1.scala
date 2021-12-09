import scala.io.Source


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  def main(args: Array[String]): Unit = {
    val grid = Source.fromFile(filename).getLines()
      .map(_.split("").map(_.toInt).toList)
      .toList

    val dimY = grid.length
    val dimX = grid(0).length

    var total = 0
    for (y <- 0 to dimY-1) {
      for (x <- 0 to dimX-1) {
        // Max is 9, so if it's out of bounds make it 10
        if (List(
          if (y > 0) grid(y-1)(x) else 10, // up
          if (y < dimY-1) grid(y+1)(x) else 10, // down
          if (x > 0) grid(y)(x-1) else 10, // left
          if (x < dimX-1) grid(y)(x+1) else 10, // right
        ).forall(grid(y)(x)<_)) total += grid(y)(x)+1
      }
    }

    println(total)
  }
}
