angular
    .module('certificateManager', ['ngRoute'])
    .config(function($routeProvider, $locationProvider) {
        $routeProvider
            .when('/:id', {
                templateUrl: 'public/certificate/certificate.html'
            })
            .when('/', {
                templateUrl: 'public/certificates/certificates.html'
            })
            .otherwise({
                redirectTo: '/'
            });

        $locationProvider.html5Mode({required: true})
    });