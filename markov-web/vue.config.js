module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/markov/'
    : '/',

  chainWebpack: (config) => {
    config.plugin('html').init((Plugin, args) => {
      const newArgs = {
        ...args[0],
      };
      newArgs.minify.removeAttributeQuotes = false;
      return new Plugin(newArgs);
    });
  },
}
