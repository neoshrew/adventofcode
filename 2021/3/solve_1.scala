import scala.io.Source

object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  def main(args: Array[String]): Unit = {
    // Assuming that all lines are the same length
    // Assuming that there are no even counts of 1s or 0s in a column
    var total_lines = 0
    val counts = Source.fromFile(filename)
      .getLines()
      .map({line =>
        total_lines += 1;
        line.split("").map(_.toInt)
      })
      .reduce({(a, b) => a.zip(b).map(col => col._1+col._2)})

    val gamma_rate = Integer.parseInt(
      counts
        .map(a => if (2*a >= total_lines) 1 else 0)
        .map(_.toString)
        .mkString,
      2
    )
    val epsilon_rate = Integer.parseInt(
      counts
        .map(a => if (2*a < total_lines) 1 else 0)
        .map(_.toString)
        .mkString,
      2
    )

    val power_usage = gamma_rate * epsilon_rate

    println(power_usage)
  }
}
