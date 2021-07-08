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

    // LaTeX support via KaTeX
    config.setLibrary("md", markdownLib);

    // Passthrough for images: copy all images in "assets" directories (and filter out others)
    config.addPassthroughCopy("**/assets/*.png");
    config.addPassthroughCopy("**/assets/*.jpg");
    config.addPassthroughCopy("**/assets/*.jpeg");
    config.addPassthroughCopy("**/assets/*.ico");
    config.addPassthroughCopy("**/assets/*.svg");
    config.addPassthroughCopy("**/assets/*.gif");

    // At this point, SCSS is not (yet) used and the CSS is fairly simple (mostly Bootstrap)
    config.addPassthroughCopy("**/assets/*.css");

    // The ico files are special
    config.addPassthroughCopy("**/*.ico");

    return {
        templateFormats: [
            "md",
            "njk"
        ],
        htmlTemplateEngine: "njk",
        markdownTemplateEngine: "njk",
        dir: {
            input: "cours",
            output: "dist",
            includes: "../includes"
        }
    };
};