<?php
/**
 * contact-handler.php — Inquiry form processor
 * Sends auto-reply to lead + notification to Leann.
 * ⚠️  This file is gitignored. Deploy via FTP only.
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://simplerabbit.studio');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(200); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST')    { http_response_code(405); echo json_encode(['success' => false]); exit; }

$input = json_decode(file_get_contents('php://input'), true);

// ── Sanitize ────────────────────────────────────────────────────────────────
function s($val) { return htmlspecialchars(trim((string)$val), ENT_QUOTES, 'UTF-8'); }

$email         = filter_var(trim($input['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$first_name    = s($input['first_name']    ?? '');
$last_name     = s($input['last_name']     ?? '');
$business_name = s($input['business_name'] ?? '');
$years         = s($input['years_in_business'] ?? '');
$website       = s($input['website']       ?? '');
$referral      = s($input['referral']      ?? '');
$project_type  = s($input['project_type']  ?? '');
$client_source = s($input['client_source'] ?? '');
$timeline      = s($input['timeline']      ?? '');
$message       = s($input['message']       ?? '');

// Required fields
if (!$email || !$first_name || !$last_name || !$business_name || !$referral || !$project_type || !$client_source) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Missing required fields']);
    exit;
}

$from    = 'Simple Rabbit <hello@simplerabbit.studio>';
$replyto = 'hello@simplerabbit.studio';

// ── Auto-reply to lead ───────────────────────────────────────────────────────
$lead_subject = 'We received your inquiry — Simple Rabbit';
$lead_body    = <<<EOT
Hi {$first_name},

Thank you for reaching out to Simple Rabbit.

We review every inquiry personally and will be in touch within 48 hours.

— Leann
Simple Rabbit
hello@simplerabbit.studio
simplerabbit.studio
EOT;

$lead_headers  = "From: {$from}\r\n";
$lead_headers .= "Reply-To: {$replyto}\r\n";
$lead_headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$lead_headers .= "X-Mailer: PHP/" . phpversion();

mail($email, $lead_subject, $lead_body, $lead_headers);

// ── Notification to Leann ────────────────────────────────────────────────────
$notif_subject = "New inquiry: {$first_name} {$last_name} — {$business_name}";
$notif_body    = <<<EOT
New inquiry from simplerabbit.studio

Name:            {$first_name} {$last_name}
Email:           {$email}
Business:        {$business_name}
Years in biz:    {$years}
Website:         {$website}

Heard about us:  {$referral}
Interested in:   {$project_type}
Timeline:        {$timeline}

Getting clients via:
{$client_source}

Additional notes:
{$message}
EOT;

$notif_headers  = "From: {$from}\r\n";
$notif_headers .= "Reply-To: {$email}\r\n";
$notif_headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$notif_headers .= "X-Mailer: PHP/" . phpversion();

mail('hello@simplerabbit.studio', $notif_subject, $notif_body, $notif_headers);

// ── Flodesk ──────────────────────────────────────────────────────────────────
$FLODESK_KEY_B64  = 'ZmRfa2V5Xzc4ZGE2YjFlZmQxOTQ5ZTVhMmM4N2ZjZjgwNzUwMTg4LjVLbk9ZNWMwS1l1YzlYZExCTlAyNzQ3UDZwQzdMWTR3NHFZRlR2bHRxMGFCelhSRmpVdzlBVnRVUU1QOGM3N21ZQ1Z6ejFmeEJvMXBRZmVvRU1CSXJSbEZYdVNVdHlLVFFBRklhd0thZVVvMU96bVZQbklUdkttWURIVkJleTZOaUtrNEhVSkk4akhXYlVOUDNDaXNZSlBydTU2dHFVUkE1OGRWNEFLa3h4Vjl5MUhLenQ5TUU3QlU2d0lqaXMxcTo=';
$SEG_SITE         = '69a105de219d2456af91f067'; // simplerabbit.studio

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
        'email'      => $email,
        'first_name' => $first_name,
        'last_name'  => $last_name,
        'segments'   => [$SEG_SITE],
    ]),
]);
curl_exec($ch);
curl_close($ch);

echo json_encode(['success' => true]);
