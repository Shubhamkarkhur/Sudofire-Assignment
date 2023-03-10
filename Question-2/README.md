# Step one
Install Webpack and necessary loaders:
```
npm install webpack webpack-cli css-loader style-loader file-loader url-loader image-webpack-loader terser-webpack-plugin mini-css-extract-plugin --save-dev
```
# Step two
Create a webpack.config.js file in your project's root directory 
# Step Three
Add your static files (JS, CSS, images) to the src directory.
# Step Four
Run the following command to bundle and minify the files:
```
npx webpack
```