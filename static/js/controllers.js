// CONTROLLERS
securityApp.controller('homeController', ['$scope', '$location', '$log', 'accountService', function ($scope, $location, $log, accountService) {

    $scope.username = accountService.username; //defining the scope which is the same thing in the service
    //Add this to scope in submit
    $scope.submit = function () {
        //query server and see if got things
        $location.path("/dashboard");
    }
    //Inside here, you want to watch this because we need to change it
    $scope.$watch('username', function () { //setters
        accountService.username = $scope.username;
    })

    $scope.$watch('password', function () { //setters
        accountService.password = $scope.password;
    })

}]);

securityApp.controller('dashboardController', ['$scope', '$stateParams', '$state', '$log', '$timeout', 'accountService', 'dashboardService', function ($scope, $stateParams, $state, $log, $timeout, accountService, dashboardService) {
    //functions
    function CalculateActivityText(percent) {
        if (percent < 20) {
            return {
                activity: "Low",
                barStyle: "progress-bar-warning",
                labelStyle: "label-warning",
                width: percent + "%"
            }
        } else if (percent < 60) {
            return {
                activity: "Medium",
                barStyle: "progress-bar-success",
                labelStyle: "label-success",
                width: percent + "%"
            }
        } else {
            return {
                activity: "High",
                barStyle: "progress-bar-danger",
                labelStyle: "label-danger",
                width: percent + "%"
            }
        }
    }

    //Initializing Variables from Service
    $log.info("testing");
    $scope.dataPackets = dashboardService.dataPackets;
    $scope.numHosts = dashboardService.numHosts;

    $scope.carouselVariables = dashboardService.carouselVariables;
    $scope.totalImages = dashboardService.totalImages;
    $scope.hostClickCount = dashboardService.hostClickCount;
    $scope.hostClick = dashboardService.hostClick;
    $scope.hostPacketCount = dashboardService.hostPacketCount;
    $scope.hostPacket = dashboardService.hostPacket;
    $scope.words = dashboardService.wordCloudData;
    $scope.hostActivity = dashboardService.hostActivity;
    $scope.hostMax = dashboardService.hostMax;
    $scope.interestingDiscoveries = dashboardService.interestingDiscoveries;
    $scope.screenshotActivity = dashboardService.screenshotActivity;
    //WATCHERS
    $scope.$watch(['dataPackets', 'numHosts', 'totalImages', 'hostClickCount', 'hostClick', 'hostPacketCount', 'hostPacket', 'interestingDiscoveries', 'words', 'hostActivity', 'hostMax', 'screenshotActivity', 'carouselVariables'], function () { //setters
        dashboardService.dataPackets = $scope.dataPackets;
        dashboardService.numHosts = $scope.numHosts;

        dashboardService.totalImages = $scope.totalImages;
        dashboardService.hostClickCount = $scope.hostClickCount;
        dashboardService.hostClick = $scope.hostClick;
        dashboardService.hostPacketCount = $scope.hostPacketCount;
        dashboardService.hostPacket = $scope.hostPacket;
        dashboardService.interestingDiscoveries = $scope.interestingDiscoveries;
        dashboardService.wordCloudData = $scope.words;
        dashboardService.hostActivity = $scope.hostActivity;
        dashboardService.hostMax = $scope.hostMax;
        dashboardService.screenshotActivity = $scope.screenshotActivity;
        dashboardService.carouselVariables = $scope.carouselVariables;
    }, true);

    //get dashboard data
    dashboardResult = dashboardService.GetDashboardData();
    //after getting the values, work on them here
    dashboardResult.$promise.then(function (response) {
        //Cancel Load

        //assign values
        dashboardGetResult = response.results[0];
        $scope.dataPackets = dashboardGetResult.dataPackets.count;
        $scope.numHosts = dashboardGetResult.hostActivity.length;

        $scope.totalImages = dashboardGetResult.totalImages.count;
        $scope.hostClickCount = dashboardGetResult.mostClicks.count;
        $scope.hostClick = dashboardGetResult.mostClicks._id;
        $scope.hostPacketCount = dashboardGetResult.mostPackets.count;
        $scope.hostPacket = dashboardGetResult.mostPackets._id;

        //Edit carousel inner HTML
        $scope.carouselVariables = [
            {
                headerText: "Total Images",
                middleText: "in the last 7 days",
                count: $scope.totalImages
            },
            {
                headerText: "Most Clicks",
                middleText: $scope.hostClick + " (7 days)",
                count: $scope.hostClickCount
            },
            {
                headerText: "Most Packets",
                middleText: $scope.hostPacket + " (7 days)",
                count: $scope.hostPacketCount
            }
        ];


        //interesting discoveries
        $scope.interestingDiscoveries = dashboardGetResult.interestingDiscoveries;

        //word cloud
        var dictCount = 0;
        var allWordObjects = [];
        for (var key in dashboardGetResult.wordCloudData) {
            allWordObjects.push({
                id: dictCount + 1,
                word: key,
                size: dashboardGetResult.wordCloudData[key]
            });
            dictCount++;
        }
        $scope.words = allWordObjects;

        $log.info("BEFORE: " + $scope.hostActivity);
        //getting the highest and sorting hosts
        $scope.hostMax = 0;
        for (var i = 0; i < dashboardGetResult.hostActivity.length; i++) {
            if (dashboardGetResult.hostActivity[i].count > $scope.hostMax) {
                $scope.hostMax = dashboardGetResult.hostActivity[i].count;
            }
        }
        var hostActivityCache = [];
        for (var i = 0; i < dashboardGetResult.hostActivity.length; i++) {
            var percentage = dashboardGetResult.hostActivity[i].count / $scope.hostMax * 100;
            hostActivityCache.push({
                "name": dashboardGetResult.hostActivity[i]._id,
                "percent": percentage,
                "style": CalculateActivityText(percentage)
            })
        }
        $scope.hostActivity = hostActivityCache;
        $log.info("AFTER: " + $scope.hostActivity);

        //handles screenshots
        dashboardService.screenshotActivity = dashboardGetResult.imageCarousel;
        for (var i = 0; i < dashboardService.screenshotActivity.length; i++) {
            var insertIndex = dashboardService.screenshotActivity[i].image_secure_url.indexOf("/upload/") + 8;
            var editString = dashboardService.screenshotActivity[i].image_secure_url;
            dashboardService.screenshotActivity[i].image_secure_url = editString.substring(0, insertIndex) + "w_280,h_157,c_scale/" + editString.substring(insertIndex, editString.length);
            dashboardService.screenshotActivity[i].username = editString.substring(0, insertIndex) + "w_1600,h_899,c_scale/" + editString.substring(insertIndex, editString.length); //use username as a placeholder
        }
        $scope.screenshotActivity = dashboardService.screenshotActivity;
        //data-lazy="https://res.cloudinary.com/www-reversethatshell-com/image/upload/w_280,h_157,c_scale/v1504380349/JIAJINPANEL/User/ib26gpl0ilxcvxfgqlyy.jpg"

        if ($(".scroll").length > 0) {
            $(".scroll").mCustomScrollbar({
                axis: "y",
                autoHideScrollbar: true,
                scrollInertia: 20,
                advanced: {
                    autoScrollOnFocus: false
                }
            });
        }

        $log.info(response.results[0]);
        $log.info($scope.dataPackets);
        $log.info($scope.interestingDiscoveries);
    });


    //pass data into scope


    // BEGINNING OF JQUERY
    $(document).ready(function () {
        // var $owlInstance = $owl.data('owlCarousel');
        //$owlInstance.reinit();
        //insert all your ajax callback code here. 
        //Which will run only after page is fully loaded in background.
        var $owl = $("#owl-example");
        $owl.trigger('destroy.owl.carousel');
        $owl.owlCarousel({
            // your initial option here, again.
        });
        if ($(".owl-carousel").length > 0) {
            $(".owl-carousel").owlCarousel({
                mouseDrag: false,
                touchDrag: true,
                slideSpeed: 300,
                paginationSpeed: 400,
                singleItem: true,
                navigation: false,
                autoPlay: true
            });
        }
        $owl.addClass('owl-carousel owl-loaded');
        $owl.trigger('refresh.owl.carousel');


        $(document).resize();
        if (document.createEvent) {
            window.dispatchEvent(new Event('resize'));
        } else {
            document.body.fireEvent('onresize');
        }


        function tp_clock_time() {
            var now = new Date();
            var hour = now.getHours();
            var minutes = now.getMinutes();

            hour = hour < 10 ? '0' + hour : hour;
            minutes = minutes < 10 ? '0' + minutes : minutes;

            $(".plugin-clock").html(hour + "<span>:</span>" + minutes);
        }
        tp_clock_time();
        if ($(".plugin-clock").length > 0) {

            tp_clock_time();

            window.setInterval(function () {
                tp_clock_time();
            }, 10000);
        }

        //Initializing scroll
        if ($(".scroll").length > 0) {
            $(".scroll").mCustomScrollbar({
                axis: "y",
                autoHideScrollbar: true,
                scrollInertia: 20,
                advanced: {
                    autoScrollOnFocus: false
                }
            });
        }

        //Initializing word cloud


        function tp_date() {
            if ($(".plugin-date").length > 0) {

                var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
                var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

                var now = new Date();
                var day = days[now.getDay()];
                var date = now.getDate();
                var month = months[now.getMonth()];
                var year = now.getFullYear();

                $(".plugin-date").html(day + ", " + month + " " + date + ", " + year);
            }
        }
        tp_date();

        //encapsulate
        dashboardService.CreateLineDashboard('dashboard-line-1');

    });

}]);
