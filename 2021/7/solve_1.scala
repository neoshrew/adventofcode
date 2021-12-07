import scala.io.Source
import scala.math.abs


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  def main(args: Array[String]): Unit = {

    val crabPositions = Source.fromFile(filename).getLines().next()
      .split(",").map(_.toInt).toList

    // I was going to be smart but let's be dumb
    val minFuel = (crabPositions.min to crabPositions.max)
        .map(pos => crabPositions.map(crabPos => abs(crabPos-pos)).sum)
        .min

    println(minFuel)
  }
}
