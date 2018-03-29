angular
    .module('certificateManager', ['ngRoute'])
    .config(function($routeProvider, $locationProvider) {
        $routeProvider
            .when('/:id', {
                templateUrl: "static/public/certificate/certificate.html"
            })
            .when('/', {
                templateUrl: "static/public/certificates/certificates.html"
            })
            .otherwise({
                redirectTo: '/'
            });

        $locationProvider.html5Mode({required: true})
    })