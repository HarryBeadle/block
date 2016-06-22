# block
A simple, hackable static site generator for portfolio websites.

## The Idea

Many static site genorators are available but they are mostly focused on blogs. I wanted a genorator that would support my project based portfolio website.

Heres how `block` works; each subdirectory genorates its own block. These block are essentially `<li>` elements in a `<ul>`. You can customise the content of each block with local block aliases and the layout and style in `html` and `css`. Aliases are in the form `%tag%`. A file inside the directory called `-block-local` defines these and looks like this:

    %date% => date
    %name% => echo "Harry Beadle"

Each alias will be replaced when the site is genorated. This allows you to specify proect names and descriptions, as well as dynamic aliases in your own scripting language or in the shell.

The layout and style of the block are defined in `block.html` and `style.css`. Above and below the blocks are the header and footer, defined in `header.html` and `footer.html` respectivly.

There are also global aliases that are applied to the final `index.html`, these are defined in a file `-block-global` that is in the main directory. This file also contains `-block-` directives. These are settings that effect how your site is genorated. These will be documented shortly.
