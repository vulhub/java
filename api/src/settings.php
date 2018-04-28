<?php
return [
    'settings' => [
        'displayErrorDetails' => boolval($_ENV['DEBUG']), // set to false in production
        'addContentLengthHeader' => false, // Allow the web server to send the content-length header

        // Renderer settings
        'renderer' => [
            'template_path' => __DIR__ . '/../templates/',
        ],

        // Monolog settings
        'logger' => [
            'name' => 'slim-app',
            'path' => isset($_ENV['docker']) ? 'php://stdout' : __DIR__ . '/../var/logs/app.log',
            'level' => \Monolog\Logger::DEBUG,
        ],

        'aws' => [
            'version' => 'latest',
            'region' => 'sgp1',
            'endpoint' => 'https://sgp1.digitaloceanspaces.com',
            'credentials' => [
                'key' => $_ENV['API_KEY'],
                'secret' => $_ENV['API_SECRET']
            ]
        ],

        'aliyun' => [
            'endpoint' => 'oss-cn-shanghai.aliyuncs.com',
            'credentials' => [
                'key' => $_ENV['API_KEY'],
                'secret' => $_ENV['API_SECRET']
            ]
        ],

        'cache' => [
            'namespace' => 'vulhub',
            'lifetime' => 60 * 60 * 24,
            'directory' => __DIR__ . '/../var/cache',
        ]
    ],
];
