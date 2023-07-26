#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const data = {};
    todos.forEach(task => {
      if (task.completed === true) {
        data[task.userId] = (data[task.userId] || 0) + 1;
      }
    });

    console.log(data);
  }
});
