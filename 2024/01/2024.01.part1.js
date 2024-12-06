// File Handling
// -------------
import fs from 'node:fs';
// Variables
let filePath = `input.txt`;
let fileData;
let fileLines;
let numLines = 0;
// Read file and store its contents
try {
    const data = fs.readFileSync(filePath, 'utf8');
    fileData = data.trim();
    fileLines = fileData.split('\n');
    numLines = fileLines.length;
} catch (readError) {
    console.error(readError);
}
console.log(fileData);


// File Processing
// ---------------
// Process file and populate lists
let list1 = new Uint32Array(numLines);
let list2 = new Uint32Array(numLines);
for (let l = 0; l < numLines; l++) {
    let currLine = fileLines.at(l).split('   ');
    list1[l] = currLine[0];
    list2[l] = currLine[1];
}
console.log(list1);
console.log(list2);
console.log();


// Problem Solving
// ---------------
// Verify lists are the same length
if(list1.length === list2.length) {
    let listLength = list1.length;

    // Sort lists
    list1.sort();
    list2.sort();
    // Verify lists are sorted
    console.log(list1);
    console.log(list2);

    // Iterate through lists to get differences
    let listDiff = new Uint32Array(listLength);
    let diff = 0;
    let sumDiff = 0;
    for (let i = 0; i < listLength; i++) {
        diff = list2.at(i) - list1.at(i);
        if (diff < 0) {
            diff *= -1;
        }
        listDiff[i] = diff;
        // Update sum of differences
        sumDiff += diff;
    }
    console.log(listDiff);
    console.log(sumDiff);
}