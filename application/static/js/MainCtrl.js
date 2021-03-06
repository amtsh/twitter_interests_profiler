angular.module('app').controller('MainCtrl', ['apiService', function(apiService) {
  var MainCtrl = this;

  MainCtrl.getInterests = function() {
    var twitter_username = MainCtrl.twitter_username;

    if (!twitter_username) {
      MainCtrl.errors = 'Enter twitter username.';
      return;
    }
    MainCtrl.errors = '';

    apiService.getInterests(twitter_username).then(function (response) {

      if (response.status == 200) {
        MainCtrl.interests = response.data.entities.filter(function(entity) {
           if (entity && entity.metadata && entity.metadata.wikipedia_url) {
             console.log(entity); return true} else {return false;
           }
        });
      }
      
    }, function(error) {
         MainCtrl.errors = "Error occurred while fetching data."
    });

  }

}])
