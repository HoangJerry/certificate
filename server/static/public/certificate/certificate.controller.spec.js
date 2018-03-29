describe('CertificateController', function() {
  var $httpBackend, createController;

  // Set up the module
  beforeEach(function() {
    angular.mock.module('certificateManager')
  });

  beforeEach(inject(function($injector, $rootScope) {
    // Set up the mock http service responses
    $httpBackend = $injector.get('$httpBackend');

    // backend definition common for all tests
    apiCertificatesServerHandler = $httpBackend.when('GET', '/api/certificates/1')
        .respond({"id":1,"name":"example.com","issuer":"Cert Corp.","expires":1469565860612});

    // The $controller service is used to create instances of controllers
    var $controller = $injector.get('$controller');

    createController = function() {
      return $controller('CertificateController', {'$rootScope' : $rootScope, '$scope': $rootScope.$new() '$routeParams': {id: 1}});
    };
  }));

  afterEach(function() {
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });


  it('should fetch certificate', function() {
    $httpBackend.expectGET('/api/certificates/1');
    var vm = createController();
    $httpBackend.flush();
    expect(vm.data).toEqual({"id":1,"name":"example.com","issuer":"Cert Corp.","expires":1469565860612});
  });


  it('should fail if the server returns a 401', function() {
    apiCertificatesServerHandler.respond(401, '');

    $httpBackend.expectGET('/api/certificates/1');
    var vm = createController();
    $httpBackend.flush();
    expect(vm.data).toBeUndefined();
  });
});
