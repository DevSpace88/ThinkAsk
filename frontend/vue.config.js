// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "/static/dist/"
      : "http://127.0.0.1:8080",
  outputDir: "../static/dist",
  indexPath: "../../templates/index.html",
  pages: {
    index: {
      entry: "src/main.js",
      title: "ThinkAsk",
    },
  },
  devServer: {
    devMiddleware: {
      publicPath: "http://127.0.0.1:8080",
      writeToDisk: (filePath) => filePath.endsWith("index.html"),
    },
    hot: "only",
    headers: { "Access-Control-Allow-Origin": "*" },
  },
};