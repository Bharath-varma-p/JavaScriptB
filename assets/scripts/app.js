const defaultResult = 0;     
let currentResult = defaultResult;


function add() {
    // currentResult = currentResult + +userInput1.value; //works as converting string into int
    oldResult = currentResult
    currentResult = currentResult + parseInt(userInput1.value);
    discription = `The sum of ${oldResult} + ${userInput1.value} = ${currentResult}`
    outputResult(currentResult,discription);
}

addBtn.addEventListener('click',add);



// outputResult(currentReslult, 'Tend');
// console.log('hello bharath')
// console.log(`The result for you bharath ${currentReslult} `)


// functions sep 7th