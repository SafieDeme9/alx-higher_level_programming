#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);

function factorial (num) {
  if (isNaN(num)) {
    return (1);
  }
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(num));
