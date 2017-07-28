function welcome(name) {
  alert('Welcome to the class, ' + name);
  alert('Please introduce yourself');
  alert('Applause');
}

welcome("Logan");
welcome("Michael");

function findMax(values) {
  var max = 0;
  for(var i = 0; i < values.length; i++) {
    if values[i] > max) {
      max = values[i]
    }
  }
  alert(max);
}

var scores = [71, 66, 88, 95, 72];

findMax(scores);

function addThree(a, b, c) {
  var sum = a + b + c;
  return sum;
}

function discount(cart, coupon) {
  var dPrice = sum(cart) * (1-coupon);
  alert(dPrice);
}

var xnum = [1,2,3];
var sale = 0.2;
discount(xnum,sale)

function sum (values) {
var sum = 0;
for(var i = 0; i < values.length; i++)
{
  sum = sum + values[i]
}
}

function square (values) {
  var num = 0;
  for(var i = 0; i <)
}
// loops

var isHealthy = true;
var cost = 5.45;

if cost < 5.00 && isHealthy) {
  alert('Buy it');
} else {
  alert('no')
}

}

var condition = true;

if (condition) {
  console.log('hi')
}
\\ says hi once

while(condition) {
  console.log('hi')
  condition = false;
}
//while is many
// false make loop stop

// console is like a print

var ['A', 'B', 'C', 'D'];
var i = 0;
while (i < letter.length) {
  console.log(letters[i]);
  i++;

}
//.length incorps all numbers
// i is element to address
// semi colon - end idea w diff line

//forloop is a short cut

for (var i = 0; i < letter.length; i++; {
  console.log(lettters[i]);
}

// use for loop for array
// guessing game - while, breaks out when correct
