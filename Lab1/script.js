var generate = document.getElementById('generate')
var symmetry = document.getElementById('symmetry')
var antisymmetry = document.getElementById('antisymmetry')
var asymmetry = document.getElementById('asymmetry')
var reflexivity = document.getElementById('reflexivity')
var antireflexivity = document.getElementById('antireflexivity')
var closure = document.getElementById('closure')

var arr
var anti = false

generate.onclick = () => {
    arr = generateRandom()
    console.table(arr)
}

function generateRandom() {
    const size = parseFloat(prompt('Введите размер матрицы'))
    const arr = new Array(size).fill().map(() => new Array(size).fill().map(() => Math.round(Math.random())));
    return arr
}

symmetry.onclick = () => {
    const arrT = _.zip(...arr)
    console.group('Транспонированная матрица')
    console.table(arrT)
    console.groupEnd()
    const res = arr.every((v, i) => arr[i].every((v, j) => v === arrT[i][j]))
    if (res) { console.log('Данное отношение является симметричным') } else {
        console.log('Данное отношение не является симметричным')
    }
}
antisymmetry.onclick = () => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (j !== i && arr[j][i] === 1 && arr[i][j] === 1) anti = true
        }
    }
    if (anti) {
        console.log('Отношение не антисимметрично')
    } else {
        console.log('Отношение антисимметрично');
    }
}

asymmetry.onclick = () => {
    let asim = true
    if (anti) {
        console.log('Отношение не асимметрично')
    } else {
        for (let i = 0; i < arr.length; i++) {
            for (let j = 0; j < arr.length; j++) {
                if (j === i && arr[j][i] === 1) asim = false
            }
        }
        if (asim) {
            console.log('Отношение асимметрично')
        } else {
            console.log('Отношение не асимметрично')
        }
    }
}
reflexivity.onclick = () => {
    let reflexiv = true
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (j === i && arr[j][i] === 0) reflexiv = false
        }
    }
    if (reflexiv) {
        console.log('Данное отношение является рефлексивным');
    } else {
        console.log('Данное отношение не является рефлексивным');
    }
}
antireflexivity.onclick = () => {
    let antireflexiv = true
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (j === i && arr[j][i] === 1) antireflexiv = false
        }
    }
    if (antireflexiv) {
        console.log('Отношение обладает свойством антирефлексивности');
    } else {
        console.log('Отношение не обладает свойством антирефлексивности');
    }
}

closure.onclick = () => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (arr[i][j] === 1) {
                for (let k = 0; k < arr.length; k++) {
                    arr[i][k] = Number(arr[i][k] || arr[j][k])
                }
            }
        }
    }
    console.group('Матрица транзитивного замыкания')
    console.table(arr)
    console.groupEnd()
}