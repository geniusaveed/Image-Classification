<?php
// This is a simple PHP server that will handle your contact form submissions
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"] ?? '';
    $email = $_POST["email"] ?? '';
    $subject = $_POST["subject"] ?? '';
    $message = $_POST["message"] ?? '';
    
    // Recipient email address (your email)
    $to = "Aveedali222@gmail.com";
    
    // Build email content
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Subject: $subject\n\n";
    $email_content .= "Message:\n$message\n";
    
    // Set email headers
    $headers = "From: $name <$email>";
    
    // Send the email
    $success = mail($to, "Portfolio Contact: $subject", $email_content, $headers);
    
    // Return JSON response
    header('Content-Type: application/json');
    
    if ($success) {
        echo json_encode(["success" => true]);
    } else {
        echo json_encode(["success" => false, "message" => "Failed to send email"]);
    }
    exit;
}

// If not a POST request, redirect to homepage
header("Location: /");
?>
