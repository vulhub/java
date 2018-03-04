<?php

use Slim\Http\Request;
use Slim\Http\Response;

// Routes

$app->get('/download/{type:jdk|jre}/{version:6|7|8}', function (Request $request, Response $response, array $args) {
    $op = ['Bucket' => 'vulhub', 'Prefix' => "{$args['type']}/java{$args['version']}/", 'Delimiter' => '/'];
    $list = \Aws\flatmap(
        $this->s3->getPaginator('ListObjects', $op),
        function (\Aws\Result $result) {
            $contentsAndPrefixes = $result->search('[Contents[], CommonPrefixes[]][]');
            // Filter out dir place holder keys and use the filter fn.
            return array_map(function ($object) {
                return basename($object['Key']);
            }, $contentsAndPrefixes);
        }
    );
    return $response->withJson(iterator_to_array($list));
});

$app->get('/download/{type:jdk|jre}/{version:6|7|8}/{name}', function (Request $request, Response $response, array $args) {
    $url = $this->s3->getObjectUrl('vulhub', "{$args['type']}/java{$args['version']}/{$args['name']}");
    return $response->withRedirect($url);
});
