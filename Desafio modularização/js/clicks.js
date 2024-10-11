import calculate from "./calculate.js"

const input = document.getElementById("input")
const allowedKeys = ["(", ")", "/", "*", "-", "+", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", ".", "%", " "]

function input_update(ev) {
    const value = ev.currentTarget.dataset.value
    input.value += value
}

function clear_input() {
    input.value = ""
    input.focus()
}

function copy_result(ev) {
    const button = ev.currentTarget
    if (button.innerText === "Copy") {
        button.innerText = "Copied!"
        button.classList.add("success")
        navigator.clipboard.writeText(document.getElementById("result").value)
    } else {
        button.innerText = "Copy"
        button.classList.remove("success")
    }
}

function keyboard_click(ev) {
    ev.preventDefault()
    if (allowedKeys.includes(ev.key)) {
      input.value += ev.key
      return
    }
    if (ev.key === "Backspace") {
      input.value = input.value.slice(0, -1)
    }
    if (ev.key === "Enter") {
      calculate()
    }
}

export { input_update, clear_input, copy_result, keyboard_click }