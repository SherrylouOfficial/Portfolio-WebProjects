<?php

session_start();


$errors = [
    'login' => '',
    'register' => ''
];

//specific error messages 
if (isset($_SESSION['login_error'])) {
    $errors['login'] = $_SESSION['login_error'];
    unset($_SESSION['login_error']);
}

if (isset($_SESSION['register_error'])) {
    $errors['register'] = $_SESSION['register_error'];
    unset($_SESSION['register_error']);
}

$activeform = isset($_SESSION['active_form']) ? $_SESSION['active_form'] : 'login';


function showError($error)
{
    return !empty($error) ? "<p class='error-message'>$error</p>" : '';
}

function isActiveForm($formName, $activeform)
{
    return $formName === $activeform ? 'active' : '';
}

?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">

    <title>With Xampp</title>
</head>

<body>

    <div class="container">

        <div class="form-box <?= isActiveForm('login', $activeform); ?>" id="login-form">

            <form action="login_register.php" method="post">

                <h2>Login</h2>
                <?= showError($errors['login']); ?>
                
                <input type="text" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" name="login">Login</button>

                <p>Don't have an account? <a href="#" onclick="showForm('register-form')">Register</a></p>

            </form>
        </div>

        <div class="form-box <?= isActiveForm('register', $activeform); ?>" id="register-form">

            <form action="login_register.php" method="post">

                <h2>Register</h2>
                <?= showError($errors['register']); ?>
                
                <input type="text" name="name" placeholder="Name" required>
                <input type="text" name="lastname" placeholder="Last Name (Optional)">
                <input type="text" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>

                <select name="role" required>
                    <option value="">--Select Option--</option>
                    <option value="student">Student</option>
                    <option value="teacher">Teacher</option>
                    <option value="parent/guardian">Parent/Guardian</option>
                    <option value="admin">Administrator</option>
                </select>

                <button type="submit" name="register">Register</button>

                <p>Already have an account? <a href="#" onclick="showForm('login-form')">Login</a></p>

            </form>
        </div>
    </div>

    <script src="script.js"></script>

</body>

</html>