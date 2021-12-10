import scala.io.Source
import scala.collection.mutable.Stack


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  // to get the points we need to
  // - map the items in the stack to their close brackets
  // - map close brackets to points
  // But we can skip a step and just map the open brackets
  // to their close equivalents' points.
  val pointsMap = Map(
    '(' -> 1,
    '[' -> 2,
    '{' -> 3,
    '<' -> 4,
  )

  def main(args: Array[String]): Unit = {
    val scores = Source.fromFile(filename).getLines()
      .map(line => {
        parseLine(line)
      })
      .filter(_.isDefined)
      .map(_.get)
      .map(
        _.foldLeft(0L)((acc, thisVal) => (acc*5)+pointsMap(thisVal))
      )
      .toList
      .sorted

    // Autocomplete tools are an odd bunch: the winner is found by sorting
    // all of the scores and then taking the middle score.
    // (There will always be an odd number of scores to consider.)
    val score = scores(scores.length/2)
    println(score)
  }

  val bracketMap = Map(
    ')' -> '(',
    ']' -> '[',
    '}' -> '{',
    '>' -> '<',
  )

  def parseLine(line: String): Option[List[Char]] = {
    val stack = Stack[Char]()
    for (char <- line) {
      if (bracketMap.contains(char)) {
        if (stack.size == 0) return None
        if (stack.pop() != bracketMap(char)) return None
      } else {
        // Not checking for erroneous characters
        stack.push(char)
      }
    }
    // Stack is stored with last in on the left, so just
    // return the stack as a list for which characters needs to be
    // auto completed.
    return Some(stack.toList)
  }
}
