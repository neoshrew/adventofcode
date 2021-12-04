import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.util.control.Breaks.{breakable, break}


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  type Board = List[List[Int]]
  type Boards = List[Board]

  def main(args: Array[String]): Unit = {
    val inputLines = Source.fromFile(filename).getLines()

    val calledNumbers = inputLines.next().split(",").map(_.toInt).toList

    var boards = inputLines
      .filter(_ != "")
      .map(
        _.split(" ")
        .filter(_ != "")
        .map(_.toInt)
        .toList
      )
      .toList
      .grouped(5)
      .toList

    var winningBoard: Board = null
    var lastNumber: Int = 0
    breakable {for (calledNumber <- calledNumbers) {
        boards = removeMatches(boards, calledNumber)
        checkForWinner(boards) match {
          case Some(b) => {winningBoard = b; lastNumber=calledNumber; break()}
          case None => ()
        }

    }}

    println((boardScore(winningBoard, lastNumber)))
  }

  def boardScore(board: Board, lastNumber: Int): Int = {
    board.foldLeft(0)(_+_.sum) * lastNumber
  }

  // def printBoard(board: Board): Unit = {
  //   board.foreach(println(_))
  // }
  // def printBoards(boards: Boards): Unit = {
  //   print("==================")
  //   boards.foreach(board => {
  //     println()
  //     printBoard(board)
  //   })
  //   println("==================\n")
  // }

  def removeMatches(boards: Boards, value: Int): Boards = {
    boards.map(_.map(_.map{
      this_val => if (this_val == value) 0 else this_val
    }))
  }

  def checkForWinner(boards: Boards): Option[Board] = {
    for (board <- boards) {
      for (row <- board) {
        if (!row.exists(_!=0)) {return Some(board)}
      }
      // hard code dim of 5 here.
      for (col <- 0 to 4) {
        if (!(0 to 4).exists(row => {board(row)(col)!=0})) {return Some(board)}
      }
    }
    None
  }
}
