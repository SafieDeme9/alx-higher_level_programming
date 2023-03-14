#!/usr/bin/node
const [arg1, arg2] = process.argv.slice(2);
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

function add (num1, num2) {
  return num1 + num2;
}
console.log(add(num1, num2));
