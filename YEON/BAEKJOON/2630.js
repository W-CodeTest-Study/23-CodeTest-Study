const path = __dirname + '/data.txt'
// const path = '/dev/stdin'

const input = require('fs').readFileSync(path).toString().trim().split('\n')
let [N, ...paper] = input

paper = paper.map(el => el.split(' ').map(Number))
let blue = 0
let white = 0

const quadrant = (r, c, n) => {
    if (isFilledSameColor(r, c, n)) {
        if (paper[r][c] === 1) blue++
        else white++
        return
    }
    let half = n / 2
    quadrant(r, c, half)
    quadrant(r, c + (half), half)
    quadrant(r + (half), c, half)
    quadrant(r + (half), c + (half), half)
}

const isFilledSameColor = (r, c, n) => {
    const base = paper[r][c];
    for (let i = r; i < r + n; i++) {
        for (let j = c; j < c + n; j++) {
            if (base !== paper[i][j]) return false
        }
    }
    return true
}

quadrant(0, 0, +N)

console.log(`${white}\n${blue}`)
