export function fizzbuzzPlusPlus(numbers: number[], words: string[]): (string|number)[] {
    if(numbers.length!==words.length) {
      console.log(numbers.length, words.length)
      throw new Error("Number of words does not correspond to number of numbers");
    }
  
    if(numbers.length < 1) {
      throw new Error("Not enough inputs");
    }

  let rowNum = 1, rowText = "", answer = [];
  const finalRow = words.toString().replaceAll(",","");
  const startTime = performance.now();
  while (rowText !== finalRow) {
    rowText = "";
    
    for (let inputIdx=0; inputIdx<numbers.length; inputIdx++) {
      if (rowNum % numbers[inputIdx] === 0){
        rowText += words[inputIdx];
      }
    }
    
    if (rowText === "") answer.push(rowNum);
    else answer.push(rowText);
    
    if (rowNum % 1000 === 0) {
      let endTime = performance.now();
      if ((endTime - startTime) / 1000 > 600) throw new Error("Timed out");
    }
    
    rowNum ++;
  }
    
  return answer
}

console.log(fizzbuzzPlusPlus([2,3,5],["fuzz","bizz","beak"]));