import java.io.File

fun sonarSweep(inputFilepath: String): Int {
    val inputNumbers = File(inputFilepath).readLines().map { numberString -> numberString.toInt() }

    val currentNextPairs = inputNumbers zip inputNumbers.slice(1 until inputNumbers.size)
    return currentNextPairs.fold(0) { acc, (current, next) ->
        if (next > current) acc + 1 else acc
    }
}

fun main(args: Array<String>) {
    println(sonarSweep("${System.getProperty("user.dir")}/../input/sonar_sweep.txt"))
}
