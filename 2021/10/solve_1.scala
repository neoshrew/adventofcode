import scala.io.Source
import scala.collection.mutable.Stack


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  val pointsMap = Map(
    ')' -> 3,
    ']' -> 57,
    '}' -> 1197,
    '>' -> 25137,
  )

  def main(args: Array[String]): Unit = {
    val score = Source.fromFile(filename).getLines()
      .map(line => {
        parseLine(line)
      })
      .filter(_.isDefined)
      .map(_.get)
      .map(pointsMap(_))
      .sum
    println(score)
  }

  val bracketMap = Map(
    ')' -> '(',
    ']' -> '[',
    '}' -> '{',
    '>' -> '<',
  )

  def parseLine(line: String): Option[Char] = {
    val stack = Stack[Char]()
    for (char <- line) {
      if (bracketMap.contains(char)) {
        if (stack.size == 0) return None
        if (stack.pop() != bracketMap(char)) return Some(char)
      } else {
        // Not checking for erroneous characters
        stack.push(char)
      }
    }
    return None
  }
}
