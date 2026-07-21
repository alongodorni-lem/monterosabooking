<?php
/**
 * Same-origin CORS proxy for the booking REST API (static + PHP hosting).
 * Forwards only safe read methods. API key comes from the client query string
 * (js/planyo-config.js) or optionally from api/planyo-secrets.php.
 */
header('Content-Type: application/json; charset=UTF-8');
header('Cache-Control: private, max-age=0');

$allowed = array('resource_search', 'list_resources', 'get_event_times', 'get_resource_info', 'api_test');
$method = isset($_GET['method']) ? (string) $_GET['method'] : '';
if (!in_array($method, $allowed, true)) {
  http_response_code(400);
  echo json_encode(array('response_code' => 3, 'response_message' => 'Method not allowed via proxy'));
  exit;
}

$params = $_GET;
if (empty($params['api_key']) && is_readable(__DIR__ . '/planyo-secrets.php')) {
  include __DIR__ . '/planyo-secrets.php';
  if (!empty($PLANYO_API_KEY)) {
    $params['api_key'] = $PLANYO_API_KEY;
  }
}

$url = 'https://www.planyo.com/rest/?' . http_build_query($params);
$ctx = stream_context_create(array(
  'http' => array(
    'method' => 'GET',
    'timeout' => 25,
    'header' => "Accept: application/json\r\n",
  ),
));
$body = @file_get_contents($url, false, $ctx);
if ($body === false) {
  http_response_code(502);
  echo json_encode(array('response_code' => 6, 'response_message' => 'Upstream request failed'));
  exit;
}
echo $body;
