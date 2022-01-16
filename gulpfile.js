const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require('gulp-autoprefixer');


gulp.task('sass', function() {
   return gulp.src('static/sass/styles.sass')
      .pipe(sass({style: 'compressed'}))
      .pipe(autoprefixer('last 10 version'))
      .pipe(gulp.dest('static/css/'))
});

gulp.task('default', function(){
    gulp.watch('static/sass/**/*.sass', gulp.series('sass'))
  return
});