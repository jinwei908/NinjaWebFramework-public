// ROUTES
securityApp.config(['$stateProvider', '$locationProvider', '$urlRouterProvider', function($stateProvider, $locationProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/");
    
var homePage = {
    name: 'home',
    url: '/',
    templateUrl: '/static/html/login-page.html',
    controller: 'homeController'
  }

  var forecastPage = {
    name: 'dashboard',
    url: '/dashboard?days', //do url/forecast?days=100
    templateUrl: '/static/html/dashboard.html',
    controller: 'dashboardController'
  }
  
  //$locationProvider.html5Mode(true);
  $stateProvider.state(homePage);
  $stateProvider.state(forecastPage);
}]);