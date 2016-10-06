#! /bin/bash

pandoc -t revealjs -s README.md -o presentation.html --standalone -V revealjs-url:https://cdn.rawgit.com/hakimel/reveal.js/master/ --variable theme="solarized"
