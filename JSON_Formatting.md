# General JSON Overview

JSON stands for JavaScript Object Notation. This means we'll be dealing with "objects" as we write this code. Objects are comprised of properties, expressed as **key/value pairs** (a.k.a. name/value pairs), formatted like this:

```js
{
    "key": "value",
    "anotherKey": "another value",
    "oneMoreKey": 1234
}
```

## Key/Value Restrictions

Each key *must be a string*, and be surrounded by double quotes (`""`).

Each value can be any valid JSON data type.

## Data Types

**String**: a string of characters (i.e., just some text) – formatted like `"this is a string"`

**Number**: a floating point or integer number – formatted like `1234` or `123.456`

**Boolean**: true or false – formatted like `true` or `false`

**Null**: the absence of a value – formatted like `null`

**Array**: a list of any valid JSON data type (including Object) – formatted like `["apple", "orange", "banana"]`

**Object**: a list of key/value pairs – formatted like `{ "key": "value" }`

---

Here's an example showing all of the data types in use:
```js
{
    "itemType": "backpack",              // string
    "id": 12,                            // number
    "contents": [                        // array (of objects, in this case)
        {
            "itemType": "egg sandwich",
            "id": 72,
            "expired": false,            // boolean
            "contents": null             // null
        },
        {
            "itemType": "water bottle",
            "id": 23,
            "percentageFilled": 0.95,
            "contents": null
        }
    ],
    "journal": {                         // object
        "pageCount": 200,
        "pagesWritten": 86,
        "private": true
    }
}
```
(Note that comments, like `// string`, are not actually supported in JSON.)

# JSON Structure in Our Templates

## Template Structure

At a high level, templates are formatted as such:

```js
{
    "id": "dash-separated-template-id",
    "name": "Full Template Name",

    "document": {
        "content": [
            // questions go here
        ]
    }
}
```
(Note that comments, like `// questions go here`, are not actually supported in JSON.)

## Question Structure

Individual questions are formatted as such:

```js
{
    "id": "questionId",
    "subquestion": false,
    "label": "Question label to display",
    "resultLabel": "Concise Question Label",
    "autoSubmit": true,
    "required": true,
    "input": {
        // input description goes here
    }
}
```

`id`: Must be unique! No duplicate question IDs.

`subquestion`: If true, the question will only show to the user *according to another one of their answers*. You'll need to link this question ID to another question's answer.

`label`: The question description that the user will see.

`resultLabel`: A more concise label for handling the response.

`autoSubmit`: Currently always `true`; for compatibility with other developer's format.

`required`: Whether or not the question is required.

`input`: A description of the input. See Question Inputs below.

## Question Input Structure

Each question has an "input" object. Here are our current options, with example options where applicable:

Text:
```js
{
    "type": "text"
}
```
Date:
```js
{
    "type": "date"
}
```
Select (pick one):
```js
{
    "type": "select",
    "options": [
        {
            "label": "Yes",                          // the value to show
            "value": "Yes",                          // the (internal) value to save
            "subquestionReferenceId": "questionId"   // the follow-up question to show, if they choose this option
        },
        {
            "label": "No",
            "value": "No"
        }
    ]
}
```
Checkbox (pick one or more):
```js
{
    "type": "checkbox",
    "options": [
        {
            "label": "Option A",  // the value to show
            "value": "A",         // the (internal) value to save
            "subquestionReferenceId": "questionId"
        },
        {
            "label": "Option B",
            "value": "B"
        },
        {
            "label": "Option C",
            "value": "C"
        }
    ]
}
```

## Conditional Questions (Subquestions)

Questions that are only presented depending on answers to other questions are "subquestions."

### Subquestion behaviour:
- Questions marked as `"subquestion": true` will not be presented by default, but will only be presented according to the user's answer to a different question
- Currently, only `select` and `checkbox` question input types can trigger subquestions 

### To create a subquestion:
1. Mark your target subquestion with the property `"subquestion": true`
2. Copy your target subquestion's ID
3. Inside the question that will (potentially) trigger the subquestion, inside the answer (option) that triggers the subquestion, add `"subquestionReferenceId": "questionId"`, replacing `questionId` with the subquestion's ID

Don't forget to test it out!
