var pro_dir='D:/coblan/web/first'
var path = require( 'path' );

module.exports = {
	//context:__dirname,
    entry: {
	    blog:'./blog.js',
	    blog_ck:'./blog_ck.js'
	    },
    output: {
	    //path:pro_dir,
        filename: '[name].pack.js'
    },
   
    resolve: {
	  root: [
	    path.resolve('D:/coblan/webcode/js'),
	  ],
	  extensions: ['', '.js']
	},
	externals: {
    	'angular': true,
    	'jquery':true,
	},
	watch: true,
};