var data = JSON.parse('{{ data | tojson | safe}}');
document.getElementById("submit").style.visibility = "hidden";
const questionSet = new Set();
questionSet.add("select");
questionSet.add("text");

// generate a question object constructor (created the type of question below)
function Question(options, question, id, require) {
    this.options = options;
    this.question = question;
    this.textbox = document.createElement("input");
    this.date = document.createElement("input");
    this.optionInput = null;
    this.optionLabel = null;
    this.id = id;
    this.require = require;
}
// prototype of radio questions
Question.prototype.createRadios = function () {
    // displaying radio buttons + options for each "select" type question
    let optionCount = 0;
    for (let eachOption in this.options) {
        this.optionInput = document.createElement("input");
        this.optionLabel = document.createElement("label");
        this.optionInput.setAttribute("type", "radio");
        this.optionInput.setAttribute("name", "question" + String(count));
        this.optionInput.setAttribute(
            "id",
            "question" + String(count) + "option" + String(optionCount)
        );
        this.optionInput.setAttribute(
            "value",
            this.options[eachOption].value
        );
        this.optionInput.className = "radioButtons";
        this.optionLabel.setAttribute(
            "for",
            "question" + String(count) + "option" + String(optionCount)
        );

        let sqID = "";
        if (this.options[eachOption].subquestionReferenceId) {
            sqID = this.options[eachOption].subquestionReferenceId;
        }
        this.optionInput.setAttribute("data-sqid", sqID);
        this.optionLabel.innerHTML = this.options[eachOption].label;
        this.question.appendChild(this.optionInput);
        this.question.appendChild(this.optionLabel);
        optionCount++;
    }
};

// prototype of textarea questions
Question.prototype.createText = function () {
    // currently using textareas for each "text" type question
    this.textbox.className = "questionInput";
    this.textbox.classList.add(this.require);
    this.textbox.id = this.id;
    this.textbox.setAttribute("type", "text");
    this.textbox.setAttribute("name",  "question" + String(count));
    this.question.appendChild(this.textbox);
};

// prototype of textarea questions
Question.prototype.createDate = function () {
    // currently using textareas for each "text" type question
    this.date.className = "questionInput";
    this.date.classList.add(this.require);
    this.date.id = this.id;
    this.date.setAttribute("type", "date");
    this.date.setAttribute("placeholder", "yyyy-mm-dd");
    this.date.setAttribute("name",  "question" + String(count));
    this.question.appendChild(this.date);
};

Question.prototype.createCheckboxes = function () {
    let markup = ``;
    let optionCount = 0;
    for (let eachOption in this.options) {
    markup += `<input type="checkbox" name="${"question" + String(count)}" id="${"question" + String(count) + "option" + String(optionCount)}" value="${this.options[eachOption].value}" class="checkbox">
                        <label for="${"question" + String(count) + "option" + String(optionCount)}" class="checkboxText">${this.options[eachOption].label} </label>
                        <br><br>
                        `;

    optionCount++;
    }
    this.question.innerHTML += markup;
}

let all_questions = [];
let questionIndex = 0;
let count = 0;
let questionsContainer = document.getElementById("questionsContainer");
for (let each in data.document.content) {
    let question = document.createElement("div");
    question.className = "questionDiv";
    question.style.display = "none";
    question.id = "question" + String(count);

    let questionHeader = document.createElement("P");
    let questionHeaderContent = document.createTextNode(
        count + 1 + ")  " + data.document.content[each].label
    );
    questionHeader.className = "questionText"; // Class for styling
    questionHeader.appendChild(questionHeaderContent);
    question.appendChild(questionHeader);
    let sub_bool = data.document.content[each].subquestion;
    let subID = data.document.content[each].id;

    question.setAttribute("data-ref-id", subID);

    if (sub_bool) {
        question.className = "sub";
    }

    let option = new Question(
        data.document.content[each].input.options,
        question,
        data.document.content[each].id,
        data.document.content[each].required
    );

    if (data.document.content[each].input.type === "select") {
        // displaying questions that are type select
        question.className += " questionRadioDiv";
        option.createRadios();
        all_questions.push(question);
    } else if (data.document.content[each].input.type === "text") {
        // diplaying questions that are type text
        // currently using textareas for each "text" type question
        option.createText();
        all_questions.push(question);
    } else if (data.document.content[each].input.type === "date") {
        option.createDate();
        all_questions.push(question);
    } else if (data.document.content[each].input.type === "checkbox") {
        option.createCheckboxes();
        all_questions.push(question);
    }

    questionsContainer.appendChild(question);

    count++;
}

showIndexedQuestion();
updateProgressBar();

let question_order = ["question0"];

function updateProgressBar() {
    document
        .getElementById("progressBarFill")
        .setAttribute(
            "width",
            String((60 * (questionIndex + 1)) / count) + "%"
        );
}

function showIndexedQuestion() {
    console.log("Tried to show index " + questionIndex);
    document.getElementById(
        "question" + String(questionIndex)
    ).style.display = "block"; // Show question div.
}


function showIndexedQuestion2(questionId) {
    console.log("Tried to show index " + questionIndex);
    document.getElementById(questionId).style.display = "block"; // Show question div.
}

function hideIndexedQuestion() {
    document.getElementById(
        "question" + String(questionIndex)
    ).style.display = "none"; // Hides question div.
}

function hideIndexedQuestion2(questionId) {
    document.getElementById(questionId).style.display = "none"; // Hides question div.
}

function back() {
    let submit = document.getElementById("submit");
    submit.style.visibility = "hidden";
    if (questionIndex == 0) {
        console.log("Can't go back");
    } else {
        hideIndexedQuestion();
        console.log(question_order);

        //showIndexedQuestion2(all_questions[questionIndex - 1].id);
        let current_question_id = "question" + String(questionIndex);
        console.log("current question", current_question_id);

        questionIndex--;

        let prev_question_id = "question0";

        
            if (question_order.includes(current_question_id) == true) {
                let current_index = question_order.indexOf(current_question_id);
                prev_question_id = question_order[current_index - 1];
                showIndexedQuestion2(prev_question_id);
            } 
        

        updateProgressBar();
    }
}

function forward() {
    if (questionIndex == data.document.content.length - 1) {
        let submit = document.getElementById("submit");
        submit.style.visibility = "visible";
        console.log("Can't go Forward");
    } else {
        hideIndexedQuestion();

        let current_question = document.getElementById("question" + String(questionIndex));
        //console.log(current_question); 


        if (current_question.className == "questionDiv questionRadioDiv") {
            let ele = document.getElementsByName("question" + String(questionIndex));

            for (i = 0; i < ele.length; i++) {
                if (ele[i].checked) {
                    if (ele[i].getAttribute("data-sqid")) {
                        for (q in all_questions) {
                            if (all_questions[q].getAttribute("data-ref-id") == ele[i].getAttribute(
                                    "data-sqid")) {
                                        console.log("next - in data-squid if statement");
                                showIndexedQuestion2(all_questions[q].id);
                                questionIndex++;
                                if (question_order.includes(all_questions[q].id) == false) {
                                    question_order.push(all_questions[q].id);
                                }
                                return;
                            }
                        }
                    }
                }
            }
        }
        questionIndex++;
        console.log("normal next");
        let tmp_quest = document.getElementById("question" + String(questionIndex));
        if (tmp_quest.className == "sub") {
            console.log("next - skip sub");
            questionIndex++;
        }
        showIndexedQuestion();
        let cur_id = "question" + String(questionIndex);

        if (question_order.includes(cur_id) == false) {
            question_order.push(cur_id);

        }
        console.log(question_order);
        

        updateProgressBar();
    }
}

let backArrow = document.getElementById("backArrow");
let frontArrow = document.getElementById("frontArrow");
backArrow.onclick = back;
frontArrow.onclick = forward;

function ValidationEvent() {
    let required = document.getElementsByClassName("true");
    let orginalEmail;
    let doubleCheckEmail;
    if (required.length > 0) {
    for (let i=0;i< required.length;i++){
        if (required[i].id == "emailAddress" || required[i].id == "verifyEmailAddress"){
        // let emailReg = "/^([w-.]+@([w-]+.)+[w-]{2,4})?$/";
        console.log(required[i].value);
        if (! required[i].value.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)) {
            alert(required[i].id + " is not email format!");
            return false;
        }
        }
        if(required[i].value == '') {

        alert(required[i].id + " is required!");
        return false;
        }
    }
    }
}