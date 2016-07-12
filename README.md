# Block: A Hackable Static Portfolio Site Genorator

Information about block is available on it's website.

> Block is a static site generator geared towards portfolio websites. I started it when I got annoyed that most static site generators are all blog based and wouldn't do what I want them to do without some serious hacking, so I made one myself, which as well as being better for portfolios is also easier to hack with built-in scripting and shell support.
How is it different?
Block is a different take on static site generation. It's geared towards portfolios rather then blogs. It's meant to be a list of the things that you're proud of. The way block achieves this is by creating an index of all the subdirectories in your server's directory. You can see it working here.

## Getting Started
Getting started is easy, all you need to do is drop each of your project's folders into the server's directory and run the following.

    python block.py

That will generate an `index.html` in that same directory. It may look a little bear at the moment, this is because you have to fill in the data about each page in a `block-local` file. They look like this:

    %tag%: echo "Command Goes Here"

In this example alias all occurrences of `%tag%` will be replaced with `Command Goes Here`. You can use more than just `echo` though, for example you can make a `%date%` tag that will replace the tag with the date and time when the script was run:

    %date%: date

There are two types of block-aliases: `block-local` and `block-global`. `block-local` alias files are applied to only a single block in a directory, whereas the `block-global` aliases are applied to the whole document.

## What if I want to link to a page that isn't on my server?

Then you can use block link files. Instead of a directory with a `block-local` file you can also use `.bl` files. These have the same format but specify a `%link%` and are in the root directory of the server.

    %link%: echo "http://url.com"

## Themes and customisation

Because Block is a relatively new piece of software there aren't many themes available. However, if you know HTML/CSS you can customise it yourself with the documents in the `block-theme` directory - remember to run the script again each time you make a change.

## Can I help?

Yes! Block is open source so the best help you can give is some code. You can also make themes (which if you [email me](mailto:harry.beadle@gmail.com) I can put on this website for you. If you find anything wrong, or think of an improvement then please add it to the issues part of the GitHub page.
