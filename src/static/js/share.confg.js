var pro_dir='D:/coblan/web/first'
var path = require( 'path' );

module.exports = {
	//context:__dirname,
    entry: {
	    share:'./share.js',
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