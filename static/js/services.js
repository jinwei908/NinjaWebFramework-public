// SERVICES
securityApp.service('accountService', ['$resource', function($resource){
    this.username = "admin"; //default value
    this.password = ""; //default value
    
    //query server
    this.AuthenticateAccount = function(username, password){
        var ninjaAPI = $resource("http://webninja.reversethatshell.com/api-get/user-auth", { //JSON CALLBACK = make sure no browsers complain about hack attempts
        callback: "JSON_CALLBACK" }, {get: {method: "JSONP"}});
        return ninjaAPI.get({user: username, name:password}); //go out     
    }
}]);

securityApp.service('dashboardService', ['$resource', function($resource){
    //Variables
    this.dataPackets = 1234;
    this.numHosts = 5;
    
    //carousel variables
    this.carouselVariables = [];
    this.totalImages = 1234;
    this.hostClickCount = 12345678;
    this.hostClick = "JIAJINPANEL";
    this.hostPacketCount = 1234;
    this.hostPacket = "JIAJINPANEL";
    
    //Interesting discoveries
    this.interestingDiscoveries = [];
    
    //word cloud
    this.wordCloudData = [];
    
    //Host activities
    this.hostActivity = [];
    this.hostMax = 0
    
    //Image Carousell
    this.screenshotActivity = [];
    
    this.scriptsLoaded = false;
    
    this.GetDashboardData = function(){
        var webFrameworkAPI = $resource("http://127.0.0.1:8000/api-auth/get/getdashboard/", { //JSON CALLBACK = make sure no browsers complain about hack attempts
        /*callback: "JSON_CALLBACK" }, {get: {method: "get"}*/})
        //this is the issue!
        var response = webFrameworkAPI.get({username: "jinwei3000"});
        return response;
    }
    
    //Morris Line Dashboard
    this.CreateLineDashboard =function(elementID){
        Morris.Line({
          element: elementID,
          data: [
            { y: '2014-10-10', a: 2,b: 4},
            { y: '2014-10-11', a: 4,b: 6},
            { y: '2014-10-12', a: 7,b: 10},
            { y: '2014-10-13', a: 5,b: 7},
            { y: '2014-10-14', a: 6,b: 9},
            { y: '2014-10-15', a: 9,b: 12},
            { y: '2014-10-16', a: 18,b: 20}
          ],
          xkey: 'y',
          ykeys: ['a','b'],
          labels: ['Sales','Event'],
          resize: true,
          hideHover: true,
          xLabels: 'day',
          gridTextSize: '10px',
          lineColors: ['#1caf9a','#33414E'],
          gridLineColor: '#E5E5E5'
        }); 
    }
    
    this.CreateBarDashboard = function(elementID){
        Morris.Bar({
            element: elementID,
            data: [
                {
                    y: 'Oct 10',
                    a: 75,
                    b: 35
                            },
                {
                    y: 'Oct 11',
                    a: 64,
                    b: 26
                            },
                {
                    y: 'Oct 12',
                    a: 78,
                    b: 39
                            },
                {
                    y: 'Oct 13',
                    a: 82,
                    b: 34
                            },
                {
                    y: 'Oct 14',
                    a: 86,
                    b: 39
                            },
                {
                    y: 'Oct 15',
                    a: 94,
                    b: 40
                            },
                {
                    y: 'Oct 16',
                    a: 96,
                    b: 41
                            }
            ],
            xkey: 'y',
            ykeys: ['a', 'b'],
            labels: ['New Users', 'Returned'],
            barColors: ['#33414E', '#1caf9a'],
            gridTextSize: '10px',
            hideHover: true,
            resize: true,
            gridLineColor: '#E5E5E5'
        });
    }
    
    this.CreateDonutDashboard = function(elementID){
        Morris.Donut({
            element: elementID,
            data: [
                {
                    label: "Returned",
                    value: 2513
                            },
                {
                    label: "New",
                    value: 764
                            },
                {
                    label: "Registred",
                    value: 311
                            }
            ],
            colors: ['#33414E', '#1caf9a', '#FEA223'],
            resize: true
        });
    }
    
    
}]);

