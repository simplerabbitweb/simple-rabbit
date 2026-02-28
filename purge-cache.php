<?php
// Purge SiteGround Nginx cache for all HTML pages
$urls = [
    'http://127.0.0.1/',
    'http://127.0.0.1/index.html',
    'http://127.0.0.1/about.html',
    'http://127.0.0.1/portfolio.html',
    'http://127.0.0.1/articles.html',
    'http://127.0.0.1/contact.html',
    'http://127.0.0.1/thank-you.html',
    'http://127.0.0.1/404.html',
];

foreach ($urls as $url) {
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PURGE');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Host: simplerabbit.studio']);
    $result = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    echo "$url → $code\n";
}
echo "Done.\n";
