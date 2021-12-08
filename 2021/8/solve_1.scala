import scala.io.Source


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  def main(args: Array[String]): Unit = {
    // looking for 1, 4, 7, and 8
    // 1 - 2 digits
    // 4 - 4 digits
    // 7 - 3 digits
    // 8 - 7 digits
    val searchDigitCounts = Set(2,4,3,7)
    val total = Source.fromFile(filename)
      .getLines()
      .map(
        line => line
          .split("\\|",2)(1)
          .trim()
          .split(" ")
          .filter(item => searchDigitCounts.contains(item.length))
          .length
      )
      .sum

    println(total)
  }
}
