// println 'Hello Groovy...!!'

// //groovy variables
// def name = "Armel"
// println 'Name is ' + name
// println "Name is ${name}"

// def (a,b,c) = [10,20,30]
// println a 
// println b
// println c

// //data types

// def x = 10
// println x.getClass().getName()

// //operators

// assert 1+2 == 3
// assert 4-3 == 1

// //ternary operator
// def y = 1
// def z = 2
// output = (y > z) ? "$y is greater than $z" : "$y not greater than $z"
// println output

// //condition statement
// def num = 0
// if (num == 10)
//     println "number is +ve"
// else if (num == 0)
//     println "number is zero"
// else
//     println "number is -ve"

// def value = 20
// def result = ""

// switch(value) {
//     case {value > 0}:
//         result = "$value is +ve"  
//     break
//     case {value < 20}:
//         result = "$value is -ve"
//     break
//     case {value == 0}:
//         result = "$value is zero"
//     break
//     default:
//         result = "Invalid number"
// }
// println result

// //for loop
// def i = 1
// for(i; i<5; i++){
//     println i
// }

// //for in loop
// for(h in 1..5){
//     println h
// }

// //exception handling
// try{
//     def n = 2/2
// }catch(Exception e){
//     println "I am inside exception block"
//     println e.getCause()
//     println e.getMessage()
//     //e.printStackTrace()
// }finally{
//     println "I am inside finally block"
// }


// String[] str = ["x","y","z"]

// for(String env: str){
//     println env
// }

// def fname = "Armel"
// def lname = "gansop"
// f_initial = fname.substring(0,1).toLowerCase()
// l_initial = lname.toLowerCase()
// println f_initial+l_initial

//Methods
def sum(int a, int b){
    def c = a + b 
    return c
}
def result = sum(10,5)
println "sum is: " + result

//closure
def str = "Hello"
def myclosure = { name -> println "$str $name" }

myclosure.call("Armel")

def myMethod(clos){
    clos.call("Groovy")
}
myMethod(myclosure)

//List
def fruits = ["Apples", "Oranges", "Grapes"]

for (i in fruits){
    println i
}

fruits.each { i ->
    println "$i"
}

fruits.eachWithIndex { x, i ->
    println "$i) $x"
}

println fruits[1]
println fruits.get(2)

//date
def d = new Date()
println d.hours+":"+d.minutes

mylist = fruits.isEmpty()
println mylist

