import scala.io.Source

object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  object Command extends Enumeration {
    type Command = Value
    val forward, down, up = Value
  }

  def main(args: Array[String]): Unit = {
    val location = Source.fromFile(filename)
      .getLines()
      .map(_.split(" ", 2))
      .map(splitline => (
        (Command.withName(splitline(0)), splitline(1).toInt)
      ))
      // x, y, a -> horizontal, depth, aim
      .foldLeft((0, 0, 0))({case ((x, y, a), (command, amount)) => {
        command match {
          case Command.forward => (x+amount, y+(a*amount), a)
          case Command.down => (x, y, a+amount)
          case Command.up => (x, y, a-amount)
        }
      }})

    println(location._1*location._2)
  }
}
