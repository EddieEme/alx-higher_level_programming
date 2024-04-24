#!/usr/bin/node
// Write a script that prints the number
// of movies where the character “Wedge Antilles” is present.

const request = require('request');

const fileApi = 'https://swapi-api.alx-tools.com/api/films/';

// Wedge Antilles ID
const characterId = 18;

function countMoviesWithCharacter(url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      callback(error);
    } else {
      try {
        const data = JSON.parse(body);
        const moviesWithCharacter = data.results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}`));
        callback(null, moviesWithCharacter.length); // Pass null for error, count for success
      } catch (error) {
        callback(error);
      }
    }
  });
}


countMovieWithCharacter(fileApi, (error, movieCount) => {
    if (error) {
        console.log(error);
    } else {
        console.log('${movieCount}');
    }
});