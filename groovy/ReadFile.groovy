//Read file

def filepath = "/Users/agansop/repo/developer/groovy/data.txt"
File myFile = new File(filepath)

// reading entire content as string
println myFile.text

//colllect lines into a list
def list = myFile.collect { it }
println "list : $list"

//store file content in an array
def array = myFile as String[]
println "array : $array"

//read file into a list of string
def lines = myFile.readLines()
println "lines : $lines"
println lines.getClass()

//read file line by line
myFile.eachLine { line ->
    println "line : $line"
}

//read file with line number
myFile.eachLine { line, i ->
    println "$i: $line"
}