import scala.io.Source

object solution {
  val filename = "input.txt"

  def main(args: Array[String]): Unit = {
    println(
      Source.fromFile(filename)
        .getLines()
        .map(_.toInt)
        .foldLeft((0, Int.MaxValue))(
          { case ((total, last), current) => {
            (total + (if (current > last) 1 else 0), current)
          }})
        ._1
    )
  }
}
