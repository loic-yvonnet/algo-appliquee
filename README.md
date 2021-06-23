# Course: Introduction to Applied Algorithms with Python (in French)

<div style="margin: auto; text-align: center;">
  <a href="https://loic-yvonnet.github.io/algo-appliquee/">
    <img src="https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/logo.png" width="50%" />
  </a>
</div>

This is the source code of the website for the Applied Algorithms with Python course targetting undergraduate students with a computer networks major. This course is written in French and targets more specifically BTS SIO SISR "Algorithme Appliquée".

The source code may be used as a template for creating other open source courses.

## Technologies

The course uses Markdown extensively in the following areas:
* **Website**: 11ty (Eleventy) and Nunjucks are used to generate the website, with Bootstrap 5 for the layout.
* **Slides**: Marp is used to generate the slides and PDFs.
* **Exercises**: Jupyter Notebook is used to generate the notebooks for the exercises and homework.

The website is deployed to [GitHub Pages](https://loic-yvonnet.github.io/algo-appliquee/).

The source code was initially generated and adapted from the [yhatt/marp-cli-example](https://github.com/yhatt/marp-cli-example) template.

## Build

On a system with `bash`, the following script may be used to install the dependencies and setup the work environment:
```sh
bin/bootstrap.sh
```

Please note that `npm` is required. If not available, the `bootstrap.sh` script will try to install it with `nvm`, if found.

To build a local development version of the website that may be run on a local webserver, the following script is available:
```sh
bin/compile.sh
```

A local webserver that serves the local website and watches for changes may be run with:
```sh
bin/run.sh
```

## Deploy

The [yhatt/marp-cli-example](https://github.com/yhatt/marp-cli-example) template uses Continuous Integration and Continuous Deployment thanks to GitHub Actions. Whenever a Pull Request is merged to the `master` branch, the CI runs and deploys the website to the `gh-pages` branch. In turn, the [GitHub Pages](https://loic-yvonnet.github.io/algo-appliquee/) are automatically updaded with the content of this branch.

## Known bugs

The following minor bugs are known and may be fixed later:
* The `run.sh` script uses `elventy --serve` and therefore does not watch for changes in CSS, assets or slides. You need to execute the `compile.sh` script to work around this limitation.
* When the Eleventy local webserver is running, the Marp PDF generation from Markdown fails (apparently) due to some obscure puppeteer issue. This issue has not been investigated (yet). Rebooting allows working around the issue.

## Contributions

If you speak both Python and French, and if you are willing to improve the course, please feel free to submit Pull Requests.