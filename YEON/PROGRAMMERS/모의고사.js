// 모의고사
// https://school.programmers.co.kr/learn/courses/30/lessons/42840

function solution(answers) {
    var answer = [];

    const answer1 = [ 1,2,3,4,5 ];
    const answer2 = [ 2,1,2,3,2,4,2,5];
    const answer3 = [ 3,3,1,1,2,2,4,4,5,5 ];

    const Correct1 = compare(answers, answer1);
    const Correct2 = compare(answers, answer2);
    const Correct3 = compare(answers, answer3);

    const CorrectArray = [ Correct1, Correct2, Correct3 ];

    const correctMax = Math.max(...CorrectArray);

    CorrectArray.forEach(function(answers, index){
        if( correctMax === answers ){
            answer.push(index+1);
        }
    });

    return answer;
}

function compare(answers, studentAnswer){

    let correct = 0;

    answers.forEach(function(answer, index){
        index = index % studentAnswer.length
        if( answer === studentAnswer[index]){
            correct++;
        }

    });
    return correct;
};
