#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const [, , arg1, arg2] = process.argv;
console.log(`${arg1} is ${arg2}`);
