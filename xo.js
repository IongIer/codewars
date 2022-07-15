// Check to see if a string has the same amount of 'x's and 'o's.
// The method must return a boolean and be case insensitive. The string can contain any char.

function XO(str) {
  let x = str.toLowerCase().replace(/[^x]/g, "");
  let o = str.toLowerCase().replace(/[^o]/g, "");
  return x.length === o.length;
}
