import scala.collection.mutable.Map
import scala.io.Source
import scala.math.{min, max}


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  type Coord = Tuple2[Int, Int]

  def main(args: Array[String]): Unit = {
    val coveredPoints: Map[Coord, Int] = Map()

    Source.fromFile(filename).getLines().foreach(line => {
      // 0,9 -> 5,9
      val splitLine = line.split(" -> ")
      val startCoord = parseCoord(splitLine(0))
      val endCoord = parseCoord(splitLine(1))

      getPointsBetween(startCoord, endCoord).iterator.foreach(point => {
        coveredPoints.updateWith(point)(
          _ match {
            case Some(count) => Some(count + 1)
            case None => Some(1)
          }
        )
      })
    })

    val total = coveredPoints.foldLeft(0)({
      case (total, (_, pointCount)) => {total + (if (pointCount > 1) 1 else 0)}
    })

    // printGrid(coveredPoints)
    println(total)
  }

  def printGrid(pointCounts: Map[Coord, Int]): Unit = {
    var minX, minY, maxX, maxY = 0
    for (coord <- pointCounts.keys) {
      minX = min(minX, coord._1)
      maxX = max(maxX, coord._1)
      minY = min(minY, coord._2)
      maxY = max(maxY, coord._2)
    }
    for (y <- minY to maxY) {
      for (x <- minX to maxX) {
        pointCounts.get((x, y)) match {
          case Some(count) => print(count)
          case None => print(".")
        }
      }
      println()
    }
  }

  def getPointsBetween(startCoord: Coord, endCoord: Coord): IterableOnce[(Int, Int)] = {
    var ((startX, startY), (endX, endY)) = (startCoord, endCoord)
    // Lazily not validating
    if (startX == endX) {
      for (dY <- startY to endY by (if (startY > endY) -1 else 1)) yield (startX, dY)
    } else if (startY == endY) {
      for (dX <- startX to endX by (if (startX > endX) -1 else 1)) yield (dX, startY)
    } else {
      return List() // part 1 we ignore these lines.
    }
  }



  def parseCoord(coord: String): Coord = {
    val split = coord.split(",")
    (split(0).toInt, split(1).toInt)
  }
}
