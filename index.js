const heb = require("hebrew-transliteration");
const transliterate = heb.transliterate;
const answer = transliterate(process.argv[2]);
console.log(answer);
