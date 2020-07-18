
function change(){
var a = document.getElementById('hello')
    a.innerHTML='Abu Bakkar Siddik'
    a.style.color = 'yellow'
}


////////////////////////////////////////////////////////////////

// DOM Practice

//var header = document.querySelector('h1')
//
//function randomColor(){
//    var letters = "0123456789ABCDEF";
//    var color = '#';
//    for (var i = 0; i < 6; i++) {
//        color += letters[Math.floor(Math.random()*16)];
//    }
//    return color
//}
//
//function changeHeaderColor(){
//    colorInput = randomColor()
//    header.style.color = colorInput;
//}
//
//setInterval("changeHeaderColor()", 500);

//////////////////////////////////////////////////////////////


// addEventListener

//var headOne = document.querySelector("#one")
//var headTwo = document.querySelector("#two")
//var headThree = document.querySelector("#three")
//
//headOne.addEventListener("click", function(){
//    headOne.innerHTML="Mouse Currently over";
//    headOne.style.color='red';
//})
//
//headOne.addEventListener("click", function(){
//    headOne.innerHTML="Mouse over Me!";
//    headOne.style.color='white';
//})


///////////////////////////////////////////////////////////////

//function hello(name){
//console.log('Hello World!!'+name)
//}
//
//function addNum(num1, num2){
//console.log(num1+num2)
//}
//
//function formal(name='Abu Bakkar Siddik', title='Software Engineer'){
//console.log("Name:"+name +"\n"+"Title:" + title)
//}



////////////////////////////////////////////////////


//function sleepIn(weekday, vacation){
//    return (!weekday || vacation)
//}
//
//
//
//function monkeyTrouble(aSmile, bSmile){
//    return (aSmile && bSmile) || (!aSmile && ! bSmile)
//}
//
//
//
//function stringTimes(str, n){
//    var returnStr = "";
//    var i = 0
//    while(i<n){
//        returnStr += str
//        i++
//    }
//    return returnStr
//}
//
//
//
//function luckySum(a, b, c){
//    if (a === 13){
//        return 0
//    }else if (b === 13){
//        return a
//    }else if (c === 13){
//        return a+b
//    }else{
//        return a+b+c
//    }
//}
//
//
//
//function caught_speeding(speed, is_birthday){
//    if (is_birthday){
//        speed -= 5
//    }
//
//    if (speed<=60){
//        return 0
//    }
//    if (60 < speed <= 80){
//        return 1
//    }
//    return 2
//}
//
//
//
//function makeBricks(small, big, goal) {
//    return goal%5 >= 0 && goal%5 - small <=0 && small + 5*big >=goal;
//}


//////////////////////////////////////////////////////////////////



//var roster = []
//function addNew(){
//    var newName = prompt("What name would you like to add?")
//    roster.push(newName)
//}
//
//function remove(){
//    var remName = prompt("What name would you like to remove?")
//    var index = roster.indexOf(remName)
//    roster.splice(index, 1)
//}
//
//function display(){
//    console.log(roster);
//}
//
//
//var start = prompt("Would you like to start the roster web app? y/n")
//var request = "empty"
//
//if (start === 'y'){
//    while (request !== 'quit') {
//        request = prompt('Please select an action: add, remove, display, or quit')
//        if (request === 'add') {
//            addNew()
//        }else if (request === 'remove') {
//            remove()
//        }else if (request === 'display') {
//            display()
//        }else {
//            alert('Not Recognized!!!')
//        }
//    }
//}


////////////////////////////////////////////////////////////////


//var employee = {
//    name : "Abu Bakkar Siddik",
//    job : "Software Engineering",
//    age : 31,
//    nameLength: function(){
//        console.log(this.name.length)
//    }
//  }
//
//
//var employee1 = {
//    name : "Rakib Sarkar",
//    job : "Data Scientist",
//    age : 31,
//    display: function(){
//        alert("Name is: "+this.name+", Job is: "+ this.job+", Age is: "+this.age)
//    }
//  }
//
//var employee2 = {
//    name : "Abu Bakkar Siddik",
//    job : "Software Engineering",
//    age : 31,
//    splt: function(){
//        console.log(this.name.split(' ')[2])
//    }
//  }

////////////////////////////////////////////////////////////////////////


