/*global module:false*/
module.exports = function(grunt) {

  grunt.initConfig({
    sprite:{
      index: {
        src: 'todaqui/static_src/sprites/sites/*.png',
        dest: 'todaqui/static/img/sitespritesheet.png',
        destCss: 'todaqui/static/css/sprites.css'
      },
      simple: {
        src: 'todaqui/static_src/sprites/simple/*.png',
        dest: 'todaqui/static/img/spritesimple.png',
        destCss: 'todaqui/static/css/spritessimple.css'
      }
    },
  });

  grunt.loadNpmTasks('grunt-spritesmith');

  grunt.registerTask('default', ['sprite']);
};
