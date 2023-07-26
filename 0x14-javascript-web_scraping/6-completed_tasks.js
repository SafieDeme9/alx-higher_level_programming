#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const todos = JSON.parse(body);
  const data = {};
  todos.forEach(task => {
    done = 0;
    if (task.completed === true) {
      data[task.userId] = (data[task.userId] || 0) + 1;
    }
  });
  console.log(data);
});
