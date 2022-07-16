// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

function moveZeros(arr) {
  noZero = arr.filter((x) => x !== 0);
  zero = arr.filter((y) => y === 0);
  return noZero.concat(zero);
}
