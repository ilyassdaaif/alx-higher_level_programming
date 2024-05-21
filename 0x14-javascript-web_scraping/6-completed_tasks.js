#!/usr/bin/node

const request = require('request');

if (process.argv.length < 4) {
    console.error('Usage: node 5-request_store.js <URL> <file path>');
    process.exit(1);
}

const apiUrl = process.argv[2];
const filePath = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to get a valid response. Status code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
        } else {
            console.log('File written successfully');
        }
    });
  }
});
