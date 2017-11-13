

app = angular.module('app', []);

// Interpolate provider for replace {{ }} template syntax 
// with // // in AngularJS (Python - AngularJS templates compatibility)
app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//').endSymbol('//');
});

app.controller("TasksCtrl", Tasks);

function Tasks($scope, $http, $timeout) {
	$scope.placeholder = "Insert a task and press enter to add";
	$scope.taskName = "";
	$scope.tasks = [];

	$scope.addTask = function() {
		if ($scope.taskName != "") {
			$scope.tasks.push($scope.taskName);
		    $scope.taskName = "";
		};

		if ($scope.tasks.length > 0) {
		    $scope.placeholder = "";
		};
	};

	$scope.deleteTask = function() {
		$scope.tasks.splice(this.$index, 1);

		if ($scope.tasks.length == 0) {
		    $scope.placeholder = "Insert a task and press enter to add";
		};
	};
};
