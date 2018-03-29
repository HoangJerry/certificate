angular
    .module('certificateManager')
    .controller('CertificateController', CertificateController);

CertificateController.$inject = ['$http', '$routeParams'];

function CertificateController($http, $routeParams) {
    var vm = this;
    $http({
        method: 'GET',
        url: '/api/certificates/' + $routeParams.id
    }).then(function (certificate) {
        vm.data = certificate.data;
    });
};