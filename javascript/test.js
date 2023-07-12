console.log("hi")

let a = [1, 2, 3]
a.push(4)

console.log(a)

// primitive value
    // null: 의도 포함(일부러 빈 값을 주고 싶을 때)
    // undefined
    // bullean: false/true(소문자)

let age = 30

const id = "ken";

switch (id) {
    case "hi": {
        console.log("여기는?");
    }
    case "admin": {
        console.log("관리자님, 환영합니다!");
    }
    case "manager": {
        console.log("매니저님 환영합니다!");
    }
    default: {
        console.log(`${id}님 환영합니다!`);
    }
}

const nums = [1, 2, 3, 4, 5];

for (const num of nums) {
    console.log(num, typeof num);
}

for (const num in nums) {
    console.log(num, typeof num);
}

const person = {name: "ken", adress: "suwon"};

for (const key in person) {
    console.log(key, person[key], typeof key)
}

console.log(person.adress)