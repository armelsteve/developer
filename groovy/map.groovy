//Maps - key-value pair

def employee = [
    'name' : 'John',
    'age' : 30
]
println employee
println employee.name
println employee['name']
println employee.get('age')
println employee.getAt('age')
println employee.size() //get the size of the map
employee.put('city', 'Paris') //add element in the map
println employee
println employee.containsKey('city')
println employee.containsValue('Paris')
println employee.getClass()

def emp2 = employee.clone()
println emp2

//for loop
employee.each { key,value ->
    println "$key : $value"
}

employee.eachWithIndex { key, value, i ->
    println "$i | $key : $value"
}

employee.eachWithIndex { entry, i ->
    println "$i | $entry.key : $entry.value"
}

def map1 = ['a' : 1, 'b' : 2]

def entries = map1.entrySet()

entries.each { entry ->
    assert entry.key in ['a','b']
    assert entry.value in [1,2]
}