#!/usr/bin/node
// Write a script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

const request = require('request');

const movieId = process.argv[2];

// Build the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the GET request
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    if (data.title) {
      console.log(data.title);
    } else {
      console.error(`${movieId}`);
    }
  }
});
