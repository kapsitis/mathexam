//require("load-grunt-tasks")(grunt); // npm install --save-dev load-grunt-tasks

module.exports = function(grunt) {

    require("load-grunt-tasks")(grunt);

    grunt.initConfig({
        "babel": {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    "dist_myjs/menu.js": "myjs/menu.js"
                }
            }
        }
    });

    grunt.registerTask("default", ["babel"]);

};