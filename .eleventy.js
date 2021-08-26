const htmlmin = require("html-minifier");
const markdownIt = require("markdown-it");
const markdownItKatex = require("@iktakahiro/markdown-it-katex");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const options = {
    html: true,
    breaks: false,
    linkify: true,
    typographer: true
};

// Avoid parsing things around $s
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

    // Markdown engine
    config.setLibrary("md", markdownLib);

    // Syntax highlighting
    config.addPlugin(syntaxHighlight);

    // Passthrough for images: copy all images in "assets" directories (and filter out others)
    config.addPassthroughCopy("assets/*.png");
    config.addPassthroughCopy("assets/*.jpg");
    config.addPassthroughCopy("assets/*.jpeg");
    config.addPassthroughCopy("assets/*.ico");
    config.addPassthroughCopy("assets/*.svg");
    config.addPassthroughCopy("assets/*.gif");
    config.addPassthroughCopy("cours/**/assets/*.png");
    config.addPassthroughCopy("cours/**/assets/*.jpg");
    config.addPassthroughCopy("cours/**/assets/*.jpeg");
    config.addPassthroughCopy("cours/**/assets/*.ico");
    config.addPassthroughCopy("cours/**/assets/*.svg");
    config.addPassthroughCopy("cours/**/assets/*.gif");

    // At this point, SCSS is not (yet) used and the CSS is fairly simple (mostly Bootstrap)
    config.addPassthroughCopy("assets/*.css");

    // The ico files are special
    config.addPassthroughCopy("cours/**/*.ico");

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