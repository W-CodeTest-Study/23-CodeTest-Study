function solution(wallpaper) {
    var answer = [];

    // #(file) 들의 좌표를 담은 새로운 배열 생성
    const filesX = []; // x값
    const filesY = []; // y값

    wallpaper.forEach((wall, i) => {
        for(let j = 0; j < wall.length ; j++) {
            if(wall[j] === '#') {
                filesX.push(i);
                filesY.push(j);
            }
        }
    });

    // files들 중 x값 중 가장 작은 값과 y값 중 가장 작은 값이 S[x,y]
    // files들 중 x값 중 가장 큰 값과 y값 중 가장 큰 값이 E[x,y]
    const S = [Math.min(...filesX), Math.min(...filesY)];
    const E = [Math.max(...filesX)+1, Math.max(...filesY)+1];


    return [...S, ...E];
}
