<?php
// DIC configuration
use Slim\Container;
use Symfony\Component\Cache\Simple\FilesystemCache;

$container = $app->getContainer();

// view renderer
$container['renderer'] = function (Container $c) {
    $settings = $c->get('settings')['renderer'];
    return new Slim\Views\PhpRenderer($settings['template_path']);
};

// monolog
$container['logger'] = function (Container $c) {
    $settings = $c->get('settings')['logger'];
    $logger = new Monolog\Logger($settings['name']);
    $logger->pushProcessor(new Monolog\Processor\UidProcessor());
    $logger->pushHandler(new Monolog\Handler\StreamHandler($settings['path'], $settings['level']));
    return $logger;
};

$container['s3'] = function (Container $c) {
    $setting = $c->get('settings')['aws'];
    return new \Aws\S3\S3Client($setting);
};

$container['aliyun'] = function (Container $c) {
    $setting = $c->get('settings')['aliyun'];
    
    return new \OSS\OssClient($setting['credentials']['key'], $setting['credentials']['secret'], $setting['endpoint']);
};

$container['cache'] = function (Container $c) {
    $settings = $c->get('settings')['cache'];
    $cache = new FilesystemCache($settings['namespace'], $settings['lifetime'], $settings['directory']);
    return $cache;
};