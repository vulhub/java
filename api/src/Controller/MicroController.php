<?php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\HttpFoundation\JsonResponse;

class MicroController extends Controller
{
    /**
     * @Route("/random/{limit}")
     */
    public function randomAction($limit)
    {
        return new JsonResponse(array(
            'number' => rand(0, $limit)
        ));
    }
}