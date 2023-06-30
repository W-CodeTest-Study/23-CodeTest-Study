const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split("\n");

const N = input[0];
const km = input[1].split(" ").map( i => BigInt(i));
const cost = input[2].split(" ").map( i => BigInt(i));

let i = 0;
let current = cost[i];
let total = 0n;

while(true) {
    if(current >  cost[i]) {
        current =  cost[i];
    }
    total += current * km[i];
    i+=1;

    if(i === km.length) {
        break;
    }
}

console.log(String(total));
