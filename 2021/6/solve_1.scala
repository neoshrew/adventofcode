import scala.io.Source
import scala.collection.mutable.Map


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  val totalDays = 80
  val maturityTime = 8
  val gestationTime = 6

  def main(args: Array[String]): Unit = {
    // There's only one line in the file.
    var fishCounts: Map[Int,Int] = Map()

    Source.fromFile(filename).getLines().next()
      .split(",").map(_.toInt)
      .foreach(fishDays => {
        fishCounts(fishDays) = fishCounts.getOrElse(fishDays, 0) +1
      })

    // optimizaton I don't need - don't recreate the map every time
    // but switch between two.
    var otherFishCounts: Map[Int, Int] = Map()
    for (today <- 1 to totalDays) {
      otherFishCounts.clear()
      fishCounts.foreach({case (gestationDaysLeft, nFish) => {
        if (gestationDaysLeft == 0) {
          otherFishCounts(gestationTime) = otherFishCounts.getOrElse(gestationTime, 0) + nFish
          otherFishCounts(maturityTime) = otherFishCounts.getOrElse(maturityTime, 0) + nFish
        } else {
          otherFishCounts(gestationDaysLeft-1) = otherFishCounts.getOrElse(gestationDaysLeft-1, 0) + nFish
        }
      }})
      // why can't I do this? Basic destructuring...
      // (fishCounts, otherFishCounts) = (otherFishCounts, fishCounts)
      val _swp = fishCounts
      fishCounts = otherFishCounts
      otherFishCounts = _swp
    }

    println(fishCounts.foldLeft(0)((s,i) => s+i._2))
  }
}
