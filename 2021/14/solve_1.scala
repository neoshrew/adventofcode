import scala.io.Source
import collection.mutable.{Map=>MutableMap}


object solution {
  // val filename = "test1.txt"
  // val filename = "test2.txt"
  val filename = "input.txt"

  // Maps a pair and number of steps to 
  // Map(((N,C), 10)) -> Map(N->4, C->5)
  val countCache = MutableMap[Tuple2[Tuple2[Char, Char],Int],Map[Char,Int]]()

  def main(args: Array[String]): Unit = {
    val lines = Source.fromFile(filename).getLines()

    val startingPattern = lines.next()
    lines.next()
    // maps a pair to the inserted character
    val transforms = lines.map(line => 
      // Massively cheese this...
      ((line(0), line(1)), (line(line.length-1)))
    ).toMap

    val nSteps = 10

    val badCounts = startingPattern
      .sliding(2, 1).map(pair=>(pair(0), pair(1)))
      .map(getCounts(transforms, _, nSteps))
      .reduce(addCounts)
    
    // Oh man, srsly there must be a better way of doing this...
    val counts = addCounts(
      badCounts,
      startingPattern.slice(1, startingPattern.length-1).map(_ -> -1).toMap
    )   

    val answer = counts.map(_._2).max - counts.map(_._2).min
    println(answer)
    

  }

  def getCounts(transforms: Map[Tuple2[Char, Char], Char],
                pair: Tuple2[Char, Char],
                nSteps: Int
              ): Map[Char, Int] = {
    val cacheKey = (pair, nSteps)
    if (!countCache.contains(cacheKey)) {
      if (nSteps > 0 && transforms.contains(pair)) {
        val innerChar = transforms(pair)
        // Oh man there must be a better way to account for the
        // doubly-counted inner char in the recursion than this...
        countCache(cacheKey) = addCounts(addCounts(
          getCounts(transforms, (pair._1, innerChar), nSteps-1),
          getCounts(transforms, (innerChar, pair._2), nSteps-1),
        ), Map(innerChar -> -1))
      } else {
        if (pair._1 == pair._2) {
          countCache(cacheKey) = Map(pair._1->2)
        } else {
          countCache(cacheKey) = Map(pair._1->1, pair._2->1)
        }
      }
    }
    countCache(cacheKey)
  }

  def addCounts(a: Map[Char, Int], b: Map[Char, Int]): Map[Char, Int] = {
    a.keys.toSet.union(b.keys.toSet).map(
      char => (char, a.getOrElse(char, 0)+b.getOrElse(char, 0))
    ).toMap
  }

}
