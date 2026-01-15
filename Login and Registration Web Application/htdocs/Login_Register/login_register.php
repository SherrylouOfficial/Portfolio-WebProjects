<?php

session_start();
require_once 'config.php';

//REGISTER PROCESS
if (isset($_POST['register'])) {
    $name = $_POST['name'];
    $lastname = $_POST['lastname']; // Get the value, even if it's empty
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    $role = $_POST['role'];

    //Validation email 
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['register_error'] = 'Invalid email format.';
        $_SESSION['active_form'] = 'register';
        header("Location: index.php");
        exit();
    }

    $checkemail = $conn->query("SELECT email FROM users WHERE email = '$email'");

    if ($checkemail->num_rows > 0) {
        $_SESSION['register_error'] = 'Email is already registered!';
        $_SESSION['active_form'] = 'register';
    } else {
        if (empty($lastname)) { // Check if the last name is empty
            $lastname = NULL;
        }

        try {
             $sql = "INSERT INTO users (name, last_name, email, password, role) VALUES (?, ?, ?, ?, ?)"; // ? as placeholders before binding 
             $stmt = $conn->prepare($sql);

            // Bind parameters
            $stmt->bind_param("sssss", $name, $lastname, $email, $password, $role);

            // Execute the query
            if ($stmt->execute()) {
            // Success
                $_SESSION['active_form'] = 'login'; //make login the active form
                header("Location: index.php");
                exit();
            } else {
                error_log("Registration Error: " . $stmt->error); // Log the error
                $_SESSION['register_error'] = 'Registration failed. Please try again.'; // Generic error message
                $_SESSION['active_form'] = 'register';
                header("Location: index.php");
                exit();
        }
    }   finally { 
            if (isset($stmt)){
            $stmt->close();}
        }
    } 
    
    header("Location: index.php");
    exit();
}


//LOGIN PROCESS
if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    //SECURE CODE FOR PASSWORD
    $sql = "SELECT * FROM users WHERE email = ?"; // Corrected table name
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])) {
            $_SESSION['name'] = $user['name'];
            $_SESSION['email'] = $user['email'];

            if ($user['role'] === 'admin') {
                header("Location: admin_page.php");
            } else {
                header("Location: user_page.php");
            }
            exit();
        }
       
    }
    //incorrect password and username
    $_SESSION['login_error'] = 'Incorrect Email or Password';
    $_SESSION['active_form'] = 'login';
    header("location: index.php");
    exit();
}