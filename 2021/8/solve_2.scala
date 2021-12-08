import scala.io.Source
import collection.mutable.Map


object solution {
  // val filename = "test1.txt"
  val filename = "input.txt"

  type DigitState = Set[String]
  case class DisplayData(samples: Set[DigitState], output: List[DigitState])

  def main(args: Array[String]): Unit = {
    val total = Source.fromFile(filename)
      .getLines()
      .map(
        line => parseLine(line)
      )
      .map(displayData => (displayData, deduceWiring(displayData.samples)))
      .map({ case(displayData, stateMap) => {
          displayData.output
            .map(stateMap(_))
            .foldLeft(0)((acc, i) => (acc*10)+i)
      }})
      .sum

    println(total)
  }

  def parseLine(line: String): DisplayData = {
    val split = line
      .split("\\|", 2)
      .map( // Either the set of 10 samples or the 4 outputs
        _.trim()
        .split(" ") // seq of words e.g. {"dcaebfg", "ecagb", "gf"}
        .map(_.split("").toSet) // make each word a set
        .toList
      ).toList
    DisplayData(split(0).toSet, split(1))
  }

  def deduceWiring(sampleData: Set[DigitState]): Map[DigitState, Int] = {
    // Look for the digits with unique digit counts and
    // grab them first
    val digitMap = Map(
      List(
        // (Number, hasNDigits)
        (1, 2),
        (4, 4),
        (7, 3),
        (8, 7), // this will always be {e, f, a, b, g, c, d}, but put it here anyway
      ).map({case (number, nDigits) => (
        number, sampleData.filter(_.size == nDigits).head
      )}): _*
    )

    // 9 is the only superset of 4 apart from 8 (and 4)
    digitMap(9) = sampleData.filter(digitState =>
      digitMap(4).subsetOf(digitState) &&
      !digitMap.exists(_._2==digitState)
    ).head

    // 0, 2, 6, 8 are the only ones with 'e' - the bottom left
    // chunk_e can be gotten by removing the items in 9 from 8
    val chunk_e = digitMap(8).diff(digitMap(9))
    val zero_two_six = sampleData.filter(digitState =>
      chunk_e.subsetOf(digitState) &&
      !digitMap.exists(_._2==digitState)
    )

    // 0 is the only superset of 1 in 0, 2, and 6
    digitMap(0) = zero_two_six.filter(digitState =>
      digitMap(1).subsetOf(digitState) &&
      !digitMap.exists(_._2==digitState)
    ).head

    // 3 is the only superset of 7 we've not found yet.
    digitMap(3) = sampleData.filter(digitState =>
      digitMap(7).subsetOf(digitState) &&
      !digitMap.exists(_._2==digitState)
    ).head

    // 5 is the only one not found yet that don't have
    // 'e' - the bottom left
    digitMap(5) = sampleData.filter(digitState =>
      !chunk_e.subsetOf(digitState) &&
      !digitMap.exists(_._2==digitState)
    ).head

    // 5 + chunk_e = 6!
    digitMap(6) = digitMap(5) ++ chunk_e

    // and then all we've left to find is 2
    digitMap(2) = zero_two_six.filter(digitState =>
      !digitMap.exists(_._2==digitState)
    ).head

    return digitMap.map({case (k, v) => (v, k)})
  }
}
