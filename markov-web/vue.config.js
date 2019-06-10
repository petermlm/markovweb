module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/'
    : '/',

  chainWebpack: (config) => {
    config.plugin('html').init((Plugin, args) => {
      const newArgs = {
        ...args[0],
      };
      if(newArgs.minify) {
        newArgs.minify.removeAttributeQuotes = false;
      }
      return new Plugin(newArgs);
    });
  },
}
