import scala.io.Source
import scala.collection.mutable.Map


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  val totalDays = 256
  val maturityTime = 8
  val gestationTime = 6

  def main(args: Array[String]): Unit = {
    // There's only one line in the file.
    var fishCounts: Map[Int,Long] = Map()

    Source.fromFile(filename).getLines().next()
      .split(",").map(_.toInt)
      .foreach(fishDays => {
        fishCounts(fishDays) = fishCounts.getOrElse(fishDays, 0L) + 1L
      })

    // optimizaton I don't need - don't recreate the map every time
    // but switch between two.
    var otherFishCounts: Map[Int, Long] = Map()
    for (today <- 1 to totalDays) {
      otherFishCounts.clear()
      fishCounts.foreach({case (gestationDaysLeft, nFish) => {
        if (gestationDaysLeft == 0) {
          otherFishCounts(gestationTime) = otherFishCounts.getOrElse(gestationTime, 0L) + nFish
          otherFishCounts(maturityTime) = otherFishCounts.getOrElse(maturityTime, 0L) + nFish
        } else {
          otherFishCounts(gestationDaysLeft-1) = otherFishCounts.getOrElse(gestationDaysLeft-1, 0L) + nFish
        }
      }})
      // why can't I do this? Basic destructuring...
      // (fishCounts, otherFishCounts) = (otherFishCounts, fishCounts)
      val _swp = fishCounts
      fishCounts = otherFishCounts
      otherFishCounts = _swp
    }

    println(fishCounts.foldLeft(0L)((s,i) => s+i._2))
  }
}
