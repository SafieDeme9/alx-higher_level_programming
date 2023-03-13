#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
let i = 0;

if (num) {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurences');
}
