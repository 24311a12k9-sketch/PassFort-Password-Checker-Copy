
function togglePassword() {
    let password = document.querySelector(
        'input[name="password"]'
    );

    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
}
