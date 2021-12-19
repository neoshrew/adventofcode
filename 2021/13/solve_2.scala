import scala.io.Source

object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  case class Coord(x: Int, y: Int)
  type Grid = Set[Coord]

  object Axis extends Enumeration {
    type Axis = Value
    val X, Y = Value
  }
  import Axis.Axis
  case class Instr(axis: Axis, pos: Int)

  def main(args: Array[String]): Unit = {
    val rawInstructions = Source.fromFile(filename).getLines()
      .filter(_!="")
      .map(parseLine)
      .toList

    var grid = rawInstructions.filter(_.isLeft).map(_.swap.toOption.get).toSet
    val instructions = rawInstructions.filter(_.isRight).map(_.toOption.get).toList

    grid = instructions.foldLeft(grid)(foldLine)
    printGrid(grid)
  }

  def foldLine(grid: Grid, instr: Instr): Grid = {
    // For now ignore dots that appear on the fold line.
    // They will be left wher they are.
    grid.map({case Coord(x, y) =>
      var dx = x
      var dy = y
      if (instr.axis == Axis.X && x > instr.pos) {
        dx = instr.pos - (x-instr.pos)
      } else if (instr.axis == Axis.Y && y > instr.pos) {
        dy = instr.pos - (y-instr.pos)
      }
      Coord(dx, dy)
    })
  }

  def printGrid(grid: Grid): Unit = {
    var maxX, minX, maxY, minY = 0
    grid.foreach({case Coord(x, y) =>
      maxX = maxX.max(x)
      minX = minX.min(x)
      maxY = maxY.max(y)
      minY = minY.min(y)
    })
    for (thisY <- minY to maxY) {
      for (thisX <- minX to maxX) {
        // print(if (grid(Coord(thisX, thisY))) "#" else ".")
        // AoC used full stops, but spaces are easier
        print(if (grid(Coord(thisX, thisY))) "#" else " ")
      }
      println("")
    }
  }

  def parseLine(line: String): Either[Coord, Instr] = {
      // hide all of the imperative nonsense here!
      if (line.startsWith("fold along ")) {
        val split1 = line.split(" ").last
        val split2 = split1.split("=", 2)
        // One day I'll learn how to use Enums
        Right(Instr(if (split2(0) == "x") Axis.X else Axis.Y , split2(1).toInt))
      } else {
        val split = line.split(",").map(_.toInt)
        Left(Coord(split(0), split(1)))
      }
  }
}
