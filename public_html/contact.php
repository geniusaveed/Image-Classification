<?php
// Display all errors for debugging (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set response headers
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Log file for debugging
$logFile = 'contact_log.txt';

// Function to log messages
function logMessage($message) {
    global $logFile;
    file_put_contents($logFile, date('Y-m-d H:i:s') . ': ' . $message . PHP_EOL, FILE_APPEND);
}

logMessage('Script started');

// Handle preflight OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Check if it's a POST request
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    logMessage('Not a POST request');
    echo json_encode(['success' => false, 'message' => 'Only POST requests are allowed']);
    exit;
}

// Get POST data
$input = file_get_contents('php://input');
logMessage('Received data: ' . $input);

// Try to decode JSON data first
$data = json_decode($input, true);

// If JSON decode fails, try to get regular form data
if ($data === null) {
    logMessage('JSON decode failed, trying form data');
    $data = [
        'name' => $_POST['name'] ?? '',
        'email' => $_POST['email'] ?? '',
        'subject' => $_POST['subject'] ?? '',
        'message' => $_POST['message'] ?? ''
    ];
}

// Validate required fields
if (empty($data['name']) || empty($data['email']) || empty($data['message'])) {
    logMessage('Missing required fields');
    echo json_encode(['success' => false, 'message' => 'Name, email, and message are required']);
    exit;
}

// Validate email
if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
    logMessage('Invalid email: ' . $data['email']);
    echo json_encode(['success' => false, 'message' => 'Invalid email address']);
    exit;
}

// Your email address
$to = 'Aveedali222@gmail.com';
$subject = 'Portfolio Contact: ' . ($data['subject'] ?? 'New message');

// Create email content
$emailContent = "Name: " . $data['name'] . "\n";
$emailContent .= "Email: " . $data['email'] . "\n\n";
if (!empty($data['subject'])) {
    $emailContent .= "Subject: " . $data['subject'] . "\n\n";
}
$emailContent .= "Message:\n" . $data['message'] . "\n";

// Set email headers
$headers = 'From: ' . $data['name'] . ' <' . $data['email'] . ">\r\n";
$headers .= "Reply-To: " . $data['email'] . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

// Try to send the email
try {
    logMessage('Attempting to send email');
    $success = mail($to, $subject, $emailContent, $headers);
    
    if ($success) {
        logMessage('Email sent successfully');
        echo json_encode(['success' => true, 'message' => 'Message sent successfully']);
    } else {
        logMessage('Failed to send email');
        echo json_encode(['success' => false, 'message' => 'Failed to send message. Please try again later.']);
    }
} catch (Exception $e) {
    logMessage('Exception: ' . $e->getMessage());
    echo json_encode(['success' => false, 'message' => 'An error occurred: ' . $e->getMessage()]);
}
