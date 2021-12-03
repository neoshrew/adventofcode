import scala.io.Source

object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  val vectors = Map(
    "forward" -> (1, 0),
    "down" -> (0, 1),
    "up" -> (0, -1),
  )

  def main(args: Array[String]): Unit = {
    // x, y -> horizontal, depth
    val location = Source.fromFile(filename)
      .getLines()
      .map(_.split(" ", 2))
      .map(splitline => (
        (vectors(splitline(0)), splitline(1).toInt)
      ))
      .map({case (direction, velocity) => {
          (direction._1*velocity, direction._2*velocity)
      }})
      .foldLeft((0, 0))({case ((x, y), (dx, dy)) => {
        (x+dx, y+dy)
      }})

    println(location._1 * location._2)
  }
}
