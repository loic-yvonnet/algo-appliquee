const htmlmin = require("html-minifier");
const markdownIt = require("markdown-it");
const markdownItKatex = require("markdown-it-katex");
const options = {
    html: true,
    breaks: false,
    linkify: true
};
const markdownLib = markdownIt(options).use(markdownItKatex);

module.exports = function (config) {
    // HTML minification
    config.addTransform("htmlmin", function(content, outputPath) {
        if (outputPath.endsWith(".html")) {
            return htmlmin.minify(content, {
                useShortDoctype: true,
                removeComments: true,
                collapseWhitespace: true
            });
        }

        return content;
    });

    // Latex support
    config.setLibrary("md", markdownLib);

    return {
        templateFormats: [
            "md",
            "njk",
            "png",
            "jpg",
            "ico",
            "svg"
        ],
        passthroughFileCopy: true,
        htmlTemplateEngine: "njk",
        markdownTemplateEngine: "njk",
        dir: {
            input: "cours",
            output: "dist",
            includes: "../includes"
        }
    };
};