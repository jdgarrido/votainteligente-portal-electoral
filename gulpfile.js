var gulp = require('gulp'),
    shell = require('gulp-shell'),
    watch = require('gulp-watch'),
    gutil = require('gulp-util'),
    plumber = require('gulp-plumber');

gulp.task('compilescss', function(){
	shell.task(['python manage.py compilescss'])
})

gulp.task('watch_compilescss', function () {
    
    watch('votai_general_theme/static/sass/**/*.scss', function (vynil) {
                                               gulp.src('votai_general_theme/static/sass/**/*.scss')
                                               	   .pipe(plumber())
                                                   .pipe(shell(['python manage.py compilescss',]));
    });
});

gulp.task('default', ['compilescss','watch_compilescss']);
