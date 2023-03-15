#!/usr/bin/node

const integers = process.argv.slice(2);
let firstMax, secondMax;
if (integers.length > 1) {
  for (let i = 0; i < integers.length; i++) {
    if (i === 0) {
      firstMax = parseInt(integers[i]);
      secondMax = firstMax;
    } else {
      if (parseInt(integers[i]) > firstMax) {
        firstMax = parseInt(integers[i]);
      }
      if (parseInt(integers[i]) > secondMax && parseInt(integers[i]) !== firstMax) {
        secondMax = parseInt(integers[i]);
      }
    }
  }
  console.log(secondMax);
} else {
  console.log(0);
}
