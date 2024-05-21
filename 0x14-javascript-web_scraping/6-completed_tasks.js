#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.error('Usage: node 6-completed_tasks.js <API URL>');
    process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Failed to get a valid response. Status code:', response.statusCode);
    } else {
        try {
            const todos = JSON.parse(body);
            const completed = {};

            todos.forEach((todo) => {
                if (todo.completed) {
                    if (completed[todo.userId] === undefined) {
                        completed[todo.userId] = 1;
                    } else {
                        completed[todo.userId]++;
                    }
                }
            });

            console.log(completed);
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
    }
});
