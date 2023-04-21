const heb = require("hebrew-transliteration");

const answer = heb.transliterate(process.argv[2]);
console.log(answer);
