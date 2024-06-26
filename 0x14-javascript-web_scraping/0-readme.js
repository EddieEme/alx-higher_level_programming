#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

const filePath = process.argv[2];

// Read the file with error handling
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err); // Print the error object
  } else {
    console.log(data);
  }
});
