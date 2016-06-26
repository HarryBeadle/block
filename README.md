# Block
A simple, hackable static site generator for portfolio websites.

## How does it work?

Many static site genorators are available but they are mostly focused on blogs. I wanted a genorator that would support my project based portfolio website.

Heres how `block` works; each subdirectory genorates its own block, a `div` on the page. You can customise the content of each block with local aliases in the form `%tag%`. The tag is replaced with the output of the shell command following it in the `block-local` file in the subdirectory:

    %date%: date
    %name%: echo "Harry Beadle"
    %lang$: echo "Python"
    %desc%: echo "My Project"

Each alias will be replaced when the site is genorated. This allows you to specify proect names and descriptions, as well as dynamic aliases in your own scripting language or in the shell.

The layout and style of the blocks are defined in `block.html` and `style.css`. Above and below the blocks are the header and footer, defined in `header.html` and `footer.html` respectivly.

There are also global aliases that are applied to the final `index.html`, these are defined in a file `block-global` that is in the main directory.

## How do I set it up?

Simply put the `block-theme`, `block-global`, `block-ignore` and `block.py` files and folders into the directory you want to serve from. Run `block.py` for the first time and it will create `block-local` files in each of the directories.

All you have to do is fill in the information for each directory and the global aliases and add any folders you do not want to index into the `block-ignore` file.

Then run it once more to genorate your finished site.

## How do I customise it?

You can build your theme by changing the files in the `block-theme` directory.