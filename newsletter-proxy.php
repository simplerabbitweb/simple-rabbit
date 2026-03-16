<?php
/**
 * newsletter-proxy.php — Flodesk subscriber proxy
 * Keeps the API key server-side. Called alongside Formspree on newsletter signup.
 * ⚠️  This file is gitignored. Do not commit it. Deploy via FTP only.
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://simplerabbit.studio');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(200); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST')    { http_response_code(405); echo json_encode(['error' => 'Method not allowed']); exit; }

// ── FLODESK ────────────────────────────────────────────────────────────────
$FLODESK_KEY_B64 = 'ZmRfa2V5XzBkNjA1NDFhM2RiODRiOTA5ZTdjZThlODEzZGY1ZDEyLjhXeDVmSXJXOUxnTmtrcUlvbzQ3elhXd1RxSHhYelpkUXE4RXlsWnFvYklHNFZ1aDRFajNacElwOGZGdWtUN2JCRDJZdjE3UHNjdklXNUNleGhCYVhER1JITkwwRnFkTHA4MXJ4NUlJaVJmc0FaVXpWMTNhWGFidUtod25tQTRrcm5GblI0Y0h2ZFZHN2RmS3lxSkN5NVpWdGI3bWtDclV5S3ZKeEpHdGVKNFhqZjM0N0c2RkxpUlZEaXhwbU40Zzo=';
$SEGMENT_ID      = '69a105de219d2456af91f067'; // segment: simplerabbit.studio
// ──────────────────────────────────────────────────────────────────────────

$input = json_decode(file_get_contents('php://input'), true);
$email = isset($input['email']) ? trim($input['email']) : '';

if (!$email || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid email']);
    exit;
}

$ch = curl_init('https://api.flodesk.com/v1/subscribers');
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 8,
    CURLOPT_HTTPHEADER     => [
        'Content-Type: application/json',
        'Authorization: Basic ' . $FLODESK_KEY_B64,
    ],
    CURLOPT_POSTFIELDS => json_encode([
        'email'    => $email,
        'segments' => [$SEGMENT_ID],
    ]),
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

http_response_code($httpCode >= 200 && $httpCode < 300 ? 200 : $httpCode);
echo $response;
