import scala.util.control.Breaks._
import scala.io.Source

object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  def main(args: Array[String]): Unit = {
    // Assuming that all lines are the same length
    implicit var total_lines = 0
    val numbers = Source.fromFile(filename)
      .getLines()
      .map({line =>
        total_lines += 1;
        line.split("").map(_.toInt).toList
      })
      .toList

    val nLength = numbers(0).length

    // Ugh I got so bored of trying to do this in an even remotely fp way.
    var oGenNums = numbers
    breakable {for (pos <- 0 to nLength-1) {
      val (_0s, _1s) = getPosCounts(oGenNums, pos)
      val wantedVal = if (_1s >= _0s) 1 else 0
      oGenNums = oGenNums.filter(_(pos) == wantedVal)

      if (oGenNums.length == 1) break()
    }}
    val oGenRating = Integer.parseInt(oGenNums(0).mkString, 2)

    var o2Nums = numbers
    breakable {for (pos <- 0 to nLength-1) {
      val (_0s, _1s) = getPosCounts(o2Nums, pos)
      val wantedVal = if (_0s <= _1s) 0 else 1
      o2Nums = o2Nums.filter(_(pos) == wantedVal)

      if (o2Nums.length == 1) break()
    }}
    val o2Rating = Integer.parseInt(o2Nums(0).mkString, 2)

    println(oGenRating*o2Rating)
  }

  def getPosCounts(numbers: List[List[Int]], pos: Int): (Int, Int) = {
    numbers.foldLeft((0, 0))({
      case ((_0s, _1s), current) => if (current(pos) == 1) (_0s, _1s+1) else (_0s+1, _1s)
    })
  }

}
