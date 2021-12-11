import java.io.File

fun sonarSweep(inputFilepath: String): Int {
    val inputNumbers = File(inputFilepath).readLines().map { numberString -> numberString.toInt() }

    val currentNextPairs = inputNumbers zip inputNumbers.slice(1 until inputNumbers.size)
    return currentNextPairs.fold(0) { acc, (current, next) ->
        if (next > current) acc + 1 else acc
    }
}

fun dive(inputFilepath: String): Int {
    val inputNumbers = File(inputFilepath).readLines().map { line -> line.split(" ") }

    var distX = 0
    var depth = 0

    val moveMapping = mapOf(
        "forward" to { x: Int -> distX += x },
        "down" to { y: Int -> depth += y },
        "up" to { y: Int -> depth -= y }
    )

    inputNumbers.forEach { (direction, distance) ->
        moveMapping[direction]?.invoke(distance.toInt())
    }

    return distX * depth
}

fun main(args: Array<String>) {
    println(sonarSweep("${System.getProperty("user.dir")}/../input/sonar_sweep.txt"))
    println(dive("${System.getProperty("user.dir")}/../input/dive.txt"))
}
