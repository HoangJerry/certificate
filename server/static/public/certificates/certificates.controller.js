angular
    .module('certificateManager')
    .controller('CertificatesController', CertificatesController);

CertificatesController.$inject = ['$scope', '$http', '$location', '$timeout'];

function CertificatesController($scope, $http, $location, $timeout) {
    var vm = this;
    var today = new Date();
    $scope.certificates = [];
    loaddata();

    $scope.thatday = today.getTime()+2592000000; //30days

    // Let us open a web socket
    var ws = new WebSocket("ws://localhost:8000/");
    ws.onopen = function()
    {
        let data = {
                stream: "status",
                payload: {
                  action: "subscribe",
                  data: {
                    action:"update"
                  },
                }
            }
        let mgs = JSON.stringify(data)
        ws.send(mgs);
    };

    ws.onmessage = function (evt) 
    { 
        var obj = JSON.parse(evt.data);
        angular.forEach($scope.certificates, function(v, k) {

            if (v.id == obj.payload.data.id) {
                $timeout(function() {
                    $scope.certificates[k] = obj.payload.data;
                });
            }
        });
    };

    ws.onclose = function()
    { 
        alert("Connection is closed..."); 
    };
        
    window.onbeforeunload = function(event) {
      socket.close();
    };

    function loaddata(){
        $http({
            method: 'GET',
            url: '/api/certificates'
        }).then(function (certificates) {
            // vm.data = certificates.data;
            $scope.certificates = certificates.data;
        });
    }

    $scope.go = function(id) {
        $location.path( "/"+id );
    }

    $scope.status = function(e,certificate) {
        e.preventDefault();
        if (certificate.expires < $scope.thatday){
        	$http({
                method: 'POST',
                data:{
                    'id':certificate.id
                },
                url: '/api/certificates/renew/'
            }).then(function (certificates) {
            });
        }
    }
};