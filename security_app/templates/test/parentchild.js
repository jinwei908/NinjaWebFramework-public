var myApp = angular.module('myApp', []);

myApp.controller('parent1Controller', ['$scope', function($scope){
    //handling childs,
    //put everything you need to a containing object
    $scope.parent1vm = {}; //must be unique to this browser. After which all variables defined will use this object.
    $scope.parent1vm.message = 'Parent 1 Message!';
}]);

myApp.controller('child1Controller', ['$scope', function($scope){
    $scope.child1vm = {}; //THIS ISS GOOD BECAUSE YOU HAVE TO ACCESS THIS CONTAINING OBJECT (unique name) thus, no two values will clash
    $scope.child1vm.message = 'Child 1 Message!';
}]);

//Parent 2 and Child 2 no need anything $scope --- Another approach
//Cleaner solution
//EVERYTHING OK, except if you want to use custom watchers (then you have to inject $scope)
myApp.controller('parent2Controller', [function(){
    this.message = 'Parent 2 Message!'; //attaching directly to THIS controller.
}]);

myApp.controller('child2Controller', [function(){
    this.message = 'Child 2 Message!'; //attaching directly to THIS controller.
}]);

///DEFAULT nothing configured
myApp.controller('parent3Controller', ['$scope', function($scope){
    $scope.message = 'Parent 3 Message!';
}]);

myApp.controller('child3Controller', ['$scope', function($scope){
    $scope.message = 'Child 3 Message!';
}]);