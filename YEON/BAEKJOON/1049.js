const fs = require('fs');
const input = fs.readFileSync('./7568.txt').toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map( i => Number(i));
const packages = [];
const singles = [];
let cost = 0;

input.forEach((i) => {
    const [p, s] = i.split(" ").map( m => Number(m));
    packages.push(p);
    singles.push(s);
});

let packagePay = Math.floor(N/6);
// packages 가격 중 최솟값이 singles 최솟값 * 6 보다 큰 경우 낱개로 사는게 이득
cost += Math.min(...packages) > Math.min(...singles) * 6 ? Math.min(...singles) * packagePay * 6 : Math.min(...packages) * packagePay;

// 낱개 최솟값 * 남은 구매 수 보다 패키지 최솟값으로 구매하는 것이 더 싼 경우 패키지 구매가 이득득cost += Math.min(...singles) * (N - (packagePay) * 6) < Math.min(...packages) ? Math.min(...singles) * (N - (packagePay) * 6) : Math.min(...packages)
console.log(cost);
