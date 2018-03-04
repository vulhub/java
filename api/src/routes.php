<?php

use Slim\Http\Request;
use Slim\Http\Response;

// Routes

$app->get('/download/{type:jdk|jre}/{version:6|7|8|9}', function (Request $request, Response $response, array $args) {
    $op = ['Bucket' => 'vulhub', 'Prefix' => "{$args['type']}/java{$args['version']}/", 'Delimiter' => '/'];
    $key = md5($op['Prefix']);
    if($this->cache->has($key)) {
        return $response->withJson($this->cache->get($key));
    }

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

    $list = iterator_to_array($list);
    $this->cache->set($key, $list);
    return $response->withJson($list);
});

$app->get('/download/{type:jdk|jre}/{version:6|7|8|9}/{name:[a-z0-9_\.\-]+}', function (Request $request, Response $response, array $args) {
    $url = $this->s3->getObjectUrl('vulhub', "{$args['type']}/java{$args['version']}/{$args['name']}");
    return $response->withRedirect($url);
});
