<?php

use Slim\Http\Request;
use Slim\Http\Response;
use \Slim\Exception\NotFoundException;

// Routes
$app->get('/download/{type:jdk|jre}/{version:6|7|8|9|10|11|12|13|14|15}', function (Request $request, Response $response, array $args) {
    $op = ['prefix' => "{$args['type']}/{$args['version']}/", 'delimiter' => '/', 'max-keys' => 1000];
    $key = md5($op['prefix']);
    if($this->cache->has($key)) {
        return $response->withJson($this->cache->get($key));
    }

    $listObjectInfo = $this->aliyun->listObjects('vulhub', $op);
    $list = $listObjectInfo->getObjectList();
    array_walk($list, function(&$object, $key) {
        $object = basename($object->getKey());
    });
    $list = array_filter($list, function($name) use ($args) {
        return $args['version'] != $name;
    });
    $list = array_values($list);

    $this->cache->set($key, $list);
    return $response->withJson($list);
});

$app->get('/download/{type:jdk|jre}/{version:6|7|8|9|10|11|12|13|14|15}/{name:[a-z0-9_\.\-]+}', function (Request $request, Response $response, array $args) {
    $object = "{$args['type']}/{$args['version']}/{$args['name']}";
    $key = md5($object);
    if($this->cache->has($key)) {
        return $response->withRedirect($this->cache->get($key));
    }

    try {
        $meta = $this->aliyun->getObjectMeta('vulhub', $object);
    } catch (\OSS\Core\OssException $e) {
        throw new NotFoundException($request, $response);
    }

    $url = $meta['info']['url'];
    $pattern = '/^http:/i';
    if (preg_match($pattern, $url)) {
        $url = preg_replace($pattern, 'https:', $url);
    }

    $this->cache->set($key, $url);
    return $response->withRedirect($url);
});