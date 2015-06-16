/*global module:false*/
module.exports = function(grunt) {

  grunt.initConfig({
    sprite:{
      all: {
        src: 'todaqui/static_src/sprites/sites/*.png',
        dest: 'todaqui/static/img/sitespritesheet.png',
        destCss: 'todaqui/static/css/sprites.css'
      }
    },
  });

  grunt.loadNpmTasks('grunt-spritesmith');

  grunt.registerTask('default', ['sprite']);
};
