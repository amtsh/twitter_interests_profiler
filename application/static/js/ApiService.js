angular.module('app').factory('apiService', ['$http', function($http) {

  var urlBase = '/api'

  // this is service object with list of methods that will be used by controller
  var service = {
    getFavorites: getFavorites,
    getInterests: getInterests
  };

  function getFavorites(username) {
    return $http.get(urlBase + '/favorites/' + username)
  }
  
  function getInterests(username) {
    return $http.get(urlBase + '/interests/' + username)
  }

  return service

}])
